# Problem Statement

Managers waste considerable time collecting project updates from multiple channels, identifying blockers, and preparing status reports. The process is manual, inconsistent, and slows the team’s ability to respond to operational risk.

# Proposed Solution

The solution is an AI Project Stand-up & Risk Assistant that captures structured employee updates, normalizes free-form input, analyzes tasks and blockers, tracks recurring issues, and produces actionable summaries for managers and leadership.

# Workflow Diagram

Employee -> Update Input -> Normalization -> AI Analysis -> Blocker / Dependency / Risk Detection -> Confidence Check -> Human Validation -> Database -> Project Health -> Manager Dashboard -> Recommended Actions -> Leadership Metrics

# Reflection

This solution focuses on one problem deeply: reducing the effort spent on status collection and blocker identification. The product uses guided updates, AI extraction, recurring blocker detection, and manager review to make the workflow faster and more reliable without turning into a large PM platform.

# 30-Day Business Review

## Challenges

- Scattered status updates
- Inconsistent reporting styles
- Slow blocker identification
- AI trust and quality concerns
- Weak operational measurement

## Priorities

1. Standardize updates and intake
2. Add human validation and confidence checks
3. Measure adoption and operational quality

## Improved Solution

The redesign adds structure, recurring-context analysis, and approval steps so that AI supports manager decision-making rather than replacing it. The workflow remains practical and usable without adding new hiring or software purchases.

## Success Metrics

- Adoption Rate
- Update Completion Rate
- Blocker Confirmation Rate
- AI Correction Rate
- Estimated Effort Reduction

# AI Design Log

The project uses a local deterministic analysis layer for demo mode, with a clear architecture for future provider-based AI integration. The design emphasizes human-in-the-loop validation and recurring-risk detection. The workflow was refined through several iterations and validated with real-style test scenarios.
