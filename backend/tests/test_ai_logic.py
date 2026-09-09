from app.ai_service import analyze_update, summarize_dashboard


def test_healthy_update():
    result = analyze_update(
        {
            'completed': 'Completed API contract review and deployment checklist.',
            'today': 'Working on QA regression and user acceptance testing.',
            'blocker': '',
            'dependency': '',
            'additional_context': 'Everything is on track.'
        },
        previous_updates=[]
    )
    assert result['risk_level'] in {'LOW', 'MEDIUM'}
    assert result['blockers'] == []


def test_blocker_detection():
    result = analyze_update(
        {
            'completed': 'Built dashboard mockup.',
            'today': 'Need to complete dashboard but waiting for database credentials.',
            'blocker': 'Waiting for database credentials',
            'dependency': 'Database/Admin team',
            'additional_context': 'Delivery may slip if not resolved soon.'
        },
        previous_updates=[]
    )
    assert len(result['blockers']) >= 1
    assert result['blockers'][0]['title'] == 'Waiting for database credentials'
    assert result['risk_level'] in {'HIGH', 'MEDIUM'}


def test_recurring_blocker_increases_risk():
    result = analyze_update(
        {
            'completed': 'Reviewed customer data issue.',
            'today': 'Still waiting for customer data and need escalation.',
            'blocker': 'Customer data dependency',
            'dependency': 'Customer Data team',
            'additional_context': 'This is still unresolved.'
        },
        previous_updates=[
            {'blocker': 'Customer data dependency', 'dependency': 'Customer Data team'},
            {'blocker': 'Customer data dependency', 'dependency': 'Customer Data team'},
        ]
    )
    assert result['risk_level'] == 'HIGH'


def test_no_blocker_invented():
    result = analyze_update(
        {
            'completed': 'Finished design review and sent summary.',
            'today': 'Working on the next sprint backlog and aligning on business requirements.',
            'blocker': '',
            'dependency': '',
            'additional_context': 'Everything is moving as planned.'
        },
        previous_updates=[]
    )
    assert result['blockers'] == []
    assert 'risk' not in result.get('summary', '').lower()


def test_dashboard_summary_has_key_sections():
    summary = summarize_dashboard({
        'updates_received': 12,
        'completed_tasks': 8,
        'active_blockers': 3,
        'high_risks': 2,
        'project_health': 'YELLOW',
        'issues': ['Database credentials pending'],
        'recommended_actions': ['Escalate database access request']
    })
    assert 'Project Health' in summary
    assert 'Recommended Actions' in summary
