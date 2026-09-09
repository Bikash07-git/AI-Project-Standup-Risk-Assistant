from datetime import datetime, timedelta

EMPLOYEES = [
    {'id': 1, 'name': 'Aisha Patel', 'team': 'Product', 'role': 'Product Manager'},
    {'id': 2, 'name': 'Marcus Lee', 'team': 'Engineering', 'role': 'Frontend Engineer'},
    {'id': 3, 'name': 'Nina Gomez', 'team': 'Engineering', 'role': 'Backend Engineer'},
    {'id': 4, 'name': 'Daniel Kim', 'team': 'Data', 'role': 'Data Analyst'},
    {'id': 5, 'name': 'Priya Shah', 'team': 'Design', 'role': 'UX Designer'},
    {'id': 6, 'name': 'Liam Chen', 'team': 'Operations', 'role': 'Project Analyst'},
    {'id': 7, 'name': 'Sara Ahmed', 'team': 'Security', 'role': 'Security Engineer'},
    {'id': 8, 'name': 'Ethan Brown', 'team': 'Customer Success', 'role': 'Customer Success Lead'},
    {'id': 9, 'name': 'Maya Singh', 'team': 'Engineering', 'role': 'QA Engineer'},
    {'id': 10, 'name': 'Omar Hassan', 'team': 'Data', 'role': 'Data Engineer'},
]

PROJECTS = [
    {'id': 1, 'name': 'Project Alpha', 'owner': 'Aisha Patel', 'team': 'Product'},
    {'id': 2, 'name': 'Customer Portal', 'owner': 'Marcus Lee', 'team': 'Engineering'},
    {'id': 3, 'name': 'Data Quality Initiative', 'owner': 'Daniel Kim', 'team': 'Data'},
]

UPDATES = [
    {
        'employee_id': 1,
        'project_id': 1,
        'date': (datetime.utcnow() - timedelta(days=0)).strftime('%Y-%m-%d'),
        'completed': 'Completed stakeholder summary and refreshed roadmap milestones.',
        'today': 'Reviewing sprint risks and aligning execution priorities with engineering.',
        'blocker': '',
        'dependency': '',
        'additional_context': 'No significant blockers.'
    },
    {
        'employee_id': 2,
        'project_id': 2,
        'date': (datetime.utcnow() - timedelta(days=0)).strftime('%Y-%m-%d'),
        'completed': 'Implemented dashboard filters and responsive layout refinements.',
        'today': 'Working on final QA fixes for the customer portal.',
        'blocker': 'Waiting for database credentials',
        'dependency': 'Database/Admin team',
        'additional_context': 'Environment access is still pending.'
    },
    {
        'employee_id': 3,
        'project_id': 2,
        'date': (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%d'),
        'completed': 'Completed API contract updates for portal integrations.',
        'today': 'Need to finalize data sync service after access is granted.',
        'blocker': 'Waiting for database credentials',
        'dependency': 'Database/Admin team',
        'additional_context': 'Same blocker persisted from yesterday.'
    },
    {
        'employee_id': 4,
        'project_id': 3,
        'date': (datetime.utcnow() - timedelta(days=0)).strftime('%Y-%m-%d'),
        'completed': 'Validated source data quality checks and cleaned duplicate records.',
        'today': 'Reviewing anomaly detection thresholds and dependency mapping.',
        'blocker': '',
        'dependency': 'Customer Data team',
        'additional_context': 'Data feed is only partially complete.'
    },
    {
        'employee_id': 5,
        'project_id': 1,
        'date': (datetime.utcnow() - timedelta(days=0)).strftime('%Y-%m-%d'),
        'completed': 'Updated onboarding flows and iterated on feedback from pilot users.',
        'today': 'Preparing handoff notes and visual QA for launch readiness.',
        'blocker': '',
        'dependency': '',
        'additional_context': 'On track for completion.'
    },
    {
        'employee_id': 6,
        'project_id': 1,
        'date': (datetime.utcnow() - timedelta(days=0)).strftime('%Y-%m-%d'),
        'completed': 'Compiled weekly risk summary and tracked milestone changes.',
        'today': 'Reviewing management escalations and cross-team dependencies.',
        'blocker': 'Customer data dependency',
        'dependency': 'Customer Data team',
        'additional_context': 'Dependency remains unresolved and needs escalation.'
    },
    {
        'employee_id': 7,
        'project_id': 2,
        'date': (datetime.utcnow() - timedelta(days=0)).strftime('%Y-%m-%d'),
        'completed': 'Security review passed for new portal endpoints.',
        'today': 'Reviewing access controls and confirming user-role matrix.',
        'blocker': '',
        'dependency': '',
        'additional_context': 'No blockers noted.'
    },
    {
        'employee_id': 8,
        'project_id': 1,
        'date': (datetime.utcnow() - timedelta(days=0)).strftime('%Y-%m-%d'),
        'completed': 'Captured customer feedback and coordinated issue triage.',
        'today': 'Preparing updated adoption summary and customer communication notes.',
        'blocker': '',
        'dependency': '',
        'additional_context': 'No operational risk.'
    },
    {
        'employee_id': 9,
        'project_id': 2,
        'date': (datetime.utcnow() - timedelta(days=2)).strftime('%Y-%m-%d'),
        'completed': 'Finished regression suite for authentication flows.',
        'today': 'Still waiting for customer data to validate end-to-end scenario coverage.',
        'blocker': 'Customer data dependency',
        'dependency': 'Customer Data team',
        'additional_context': 'This is a recurring blocker affecting validation.'
    },
    {
        'employee_id': 10,
        'project_id': 3,
        'date': (datetime.utcnow() - timedelta(days=0)).strftime('%Y-%m-%d'),
        'completed': 'Resolved staging data validation alerts and refreshed pipeline checks.',
        'today': 'Monitoring anomaly reports and preparing dashboard for leadership review.',
        'blocker': '',
        'dependency': '',
        'additional_context': 'Data quality trend is stable.'
    },
]
