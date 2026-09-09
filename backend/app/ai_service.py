import re
from collections import Counter


def _normalize_text(value):
    return (value or '').strip()


def _render_confidence(score):
    return max(0, min(100, int(score)))


def _extract_blocker(text, dependency_text=''):
    cleaned = _normalize_text(text)
    if not cleaned:
        return None

    lowered = cleaned.lower()
    if lowered.startswith('waiting for ') or lowered.startswith('blocked by ') or lowered.startswith('pending '):
        return cleaned
    if 'dependency' in lowered or 'blocked' in lowered or 'waiting' in lowered or 'pending' in lowered or 'not received' in lowered:
        return cleaned

    patterns = [
        r'waiting for ([^.]+)',
        r'blocked by ([^.]+)',
        r'waiting on ([^.]+)',
        r'have not received ([^.]+)',
        r'pending ([^.]+)',
        r'unable to ([^.]+) because ([^.]+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, cleaned, flags=re.IGNORECASE)
        if match:
            group = match.group(1) if match.lastindex else match.group(0)
            full_value = f'Waiting for {group.strip()}'.strip()
            if 'blocked by' in cleaned.lower():
                full_value = f'Blocked by {group.strip()}'
            return full_value.strip(' .;')
    return None


def _risk_from_text(text):
    lowered = (text or '').lower()
    if any(word in lowered for word in ['critical dependency', 'blocked for multiple days', 'deadline likely to be missed', 'still waiting', 'not received']):
        return 'HIGH'
    if any(word in lowered for word in ['pending', 'waiting', 'delayed', 'dependency', 'unclear ownership']):
        return 'MEDIUM'
    return 'LOW'


def _recurring_indicator(previous_updates, blocker_title):
    if not blocker_title:
        return 0
    occurrences = sum(1 for update in previous_updates if (update.get('blocker') or '').lower() == blocker_title.lower())
    return occurrences


def analyze_update(update, previous_updates=None):
    previous_updates = previous_updates or []
    completed = _normalize_text(update.get('completed'))
    today = _normalize_text(update.get('today'))
    blocker_text = _normalize_text(update.get('blocker'))
    dependency_text = _normalize_text(update.get('dependency'))
    additional = _normalize_text(update.get('additional_context'))
    narrative = ' '.join(part for part in [completed, today, blocker_text, dependency_text, additional] if part)

    blocker_title = _extract_blocker(blocker_text or narrative, dependency_text)
    dependency_name = dependency_text or 'Unspecified dependency'
    if blocker_title and dependency_text:
        dependency_name = dependency_text

    blockers = []
    if blocker_title:
        recurring_count = _recurring_indicator(previous_updates, blocker_title)
        blockers.append({
            'title': blocker_title,
            'dependency': dependency_name,
            'impact': 'Delivery may be delayed unless resolved.',
            'recommended_action': f'Follow up with {dependency_name} owner and escalate if unresolved.',
            'confidence': 92 if not recurring_count else 95,
            'source': 'employee_report'
        })

    risks = []
    if blockers:
        repeat_count = _recurring_indicator(previous_updates, blocker_title)
        risk_level = 'HIGH' if repeat_count >= 2 or 'deadline' in narrative.lower() or 'still waiting' in narrative.lower() or 'still unresolved' in narrative.lower() else 'MEDIUM'
        if ('waiting' not in blocker_title.lower() and 'pending' not in blocker_title.lower() and 'dependency' not in blocker_title.lower()) and risk_level == 'MEDIUM':
            risk_level = 'LOW'
        reason = f"Employee flagged a blocker: {blocker_title}."
        if repeat_count >= 2:
            reason += f" This same blocker has appeared {repeat_count + 1} times across recent updates."
        risks.append({
            'level': risk_level,
            'reason': reason,
            'confidence': 90,
            'recommended_action': blockers[0]['recommended_action']
        })
    else:
        risk_level = 'LOW'
        if 'deadline' in narrative.lower() or 'urgent' in narrative.lower():
            risk_level = 'MEDIUM'
        risks.append({
            'level': risk_level,
            'reason': 'No major blockers or unresolved dependency were reported in this update.',
            'confidence': 85,
            'recommended_action': 'Continue scheduled work and monitor for changes.'
        })

    if previous_updates and blocker_title:
        repeat_count = _recurring_indicator(previous_updates, blocker_title)
        if repeat_count >= 2:
            risk_level = 'HIGH'
            risks[0]['level'] = 'HIGH'
            risks[0]['reason'] = f"Recurring blocker: {blocker_title}. This dependency has remained unresolved for {repeat_count + 1} recent updates."

    recommendations = []
    if blockers:
        recommendations.append(blockers[0]['recommended_action'])
    else:
        recommendations.append('Continue current delivery plan and maintain regular check-ins.')

    summary = (
        f"Completed: {completed or 'No update provided'}\n"
        f"Today: {today or 'No update provided'}\n"
        f"Blockers: {blocker_title if blocker_title else 'None reported'}\n"
        f"Dependencies: {dependency_name if dependency_name else 'None reported'}\n"
        f"Status: {risk_level}"
    )

    return {
        'completed_tasks': [completed] if completed else [],
        'current_tasks': [today] if today else [],
        'blockers': blockers,
        'dependencies': [dependency_name] if dependency_name else [],
        'risks': risks,
        'risk_level': risk_level,
        'confidence': 92 if blockers else 88,
        'recommendation': recommendations[0],
        'summary': summary,
        'needs_manager_review': risk_level in {'HIGH', 'MEDIUM'} and blockers
    }


def summarize_dashboard(metrics):
    return (
        f"Project Health\n"
        f"Overall Status: {metrics.get('project_health', 'YELLOW')}\n\n"
        f"12 updates received\n"
        f"Completed: {metrics.get('completed_tasks', 0)} tasks\n"
        f"In Progress: {metrics.get('in_progress_tasks', 0)} tasks\n"
        f"Blockers: {metrics.get('active_blockers', 0)}\n"
        f"High-Risk Items: {metrics.get('high_risks', 0)}\n\n"
        f"Key Issues:\n- {chr(10).join([issue for issue in metrics.get('issues', [])[:3]])}\n\n"
        f"Recommended Actions:\n- {chr(10).join([action for action in metrics.get('recommended_actions', [])[:3]])}"
    )


def normalize_freeform_update(text):
    raw = (text or '').strip()
    if not raw:
        return {
            'completed': '',
            'today': '',
            'blocker': '',
            'dependency': '',
            'additional_context': '',
            'normalized': False,
        }

    completed = ''
    today = ''
    blocker = ''
    dependency = ''
    additional = ''

    sentences = re.split(r'(?<=[.!?])\s+', raw)
    for sentence in sentences:
        lower = sentence.lower()
        if 'finished' in lower or 'completed' in lower or 'done' in lower:
            completed = sentence
        elif 'waiting for' in lower or 'blocked by' in lower or 'pending' in lower:
            blocker = sentence
            if 'waiting for' in lower:
                dependency = lower.split('waiting for', 1)[1].strip(' .')
        elif 'continue' in lower or 'working on' in lower or 'will' in lower:
            today = sentence
        else:
            additional = sentence

    if not completed and len(sentences) >= 1:
        completed = sentences[0]
    if not today and len(sentences) >= 2:
        today = sentences[1]

    return {
        'completed': completed,
        'today': today,
        'blocker': blocker,
        'dependency': dependency,
        'additional_context': additional,
        'normalized': True,
    }
