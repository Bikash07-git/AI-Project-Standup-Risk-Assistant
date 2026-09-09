from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.ai_provider import get_ai_analysis
from app.ai_service import analyze_update, normalize_freeform_update
from app.database import get_connection, init_db, list_reviews, save_review
from app.seed_data import EMPLOYEES, PROJECTS, UPDATES

app = FastAPI(title='AI Project Stand-up & Risk Assistant API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class UpdatePayload(BaseModel):
    employee_name: str
    team: str
    project: str
    completed: str = ''
    today: str = ''
    blocker: str = ''
    dependency: str = ''
    additional_context: str = ''


class FreeformPayload(BaseModel):
    text: str


class ReviewPayload(BaseModel):
    update_id: int
    status: str
    reviewed_by: str = 'manager'
    edited_value: str | None = None


@app.get('/')
def read_root():
    return {'message': 'AI Project Stand-up & Risk Assistant API is running'}


@app.get('/health')
def health_check():
    return {'status': 'ok', 'demo_mode': True}


@app.get('/demo-data')
def get_demo_data():
    return {
        'employees': EMPLOYEES,
        'projects': PROJECTS,
        'updates': UPDATES,
        'metrics': {
            'adoption_rate': 68,
            'update_completion_rate': 91,
            'confirmation_rate': 86,
            'correction_rate': 14,
            'effort_reduction': 42,
            'demo_mode': True,
            'demo_label': 'Demo / Illustrative Data'
        }
    }


@app.get('/project-state')
def project_state():
    updates = [
        {
            'employee_id': 2,
            'project_id': 2,
            'date': '2026-09-09',
            'completed': 'Implemented dashboard filters',
            'today': 'Final QA for customer portal',
            'blocker': 'Waiting for database credentials',
            'dependency': 'Database/Admin team',
            'riskLevel': 'HIGH',
        },
        {
            'employee_id': 3,
            'project_id': 2,
            'date': '2026-09-08',
            'completed': 'Completed API contract updates',
            'today': 'Need to finalize data sync service',
            'blocker': 'Waiting for database credentials',
            'dependency': 'Database/Admin team',
            'riskLevel': 'HIGH',
        },
        {
            'employee_id': 9,
            'project_id': 2,
            'date': '2026-09-07',
            'completed': 'Finished regression suite',
            'today': 'Still waiting for customer data',
            'blocker': 'Customer data dependency',
            'dependency': 'Customer Data team',
            'riskLevel': 'HIGH',
        }
    ]
    return {'updates': updates}


@app.post('/normalize')
def normalize_update(payload: FreeformPayload):
    result = normalize_freeform_update(payload.text)
    return result


@app.post('/analyze')
def analyze_payload(payload: UpdatePayload):
    normalized = {
        'completed': payload.completed,
        'today': payload.today,
        'blocker': payload.blocker,
        'dependency': payload.dependency,
        'additional_context': payload.additional_context,
    }
    previous_updates = [
        {'blocker': 'Waiting for database credentials', 'dependency': 'Database/Admin team'},
        {'blocker': 'Customer data dependency', 'dependency': 'Customer Data team'},
    ]
    result = get_ai_analysis(normalized, previous_updates)
    return {
        'employee_name': payload.employee_name,
        'team': payload.team,
        'project': payload.project,
        'analysis': result,
        'demo_mode': True,
        'review_required': result.get('needs_manager_review', False),
        'created_at': datetime.utcnow().isoformat() + 'Z'
    }


@app.get('/dashboard')
def dashboard_summary():
    return {
        'updates_received': 12,
        'completed_tasks': 8,
        'active_blockers': 3,
        'high_risks': 2,
        'project_health': 'YELLOW',
        'project_health_reason': '2 unresolved dependencies are affecting delivery and validation work.',
        'issues': ['Database credentials pending', 'Customer data dependency unresolved'],
        'recommended_actions': ['Escalate database access request', 'Follow up with data owner', 'Confirm customer data delivery date'],
        'employees_needing_attention': ['Marcus Lee', 'Nina Gomez', 'Liam Chen'],
        'critical_blockers': [
            {'employee': 'Marcus Lee', 'blocker': 'Waiting for database credentials', 'dependency': 'Database/Admin team'},
            {'employee': 'Nina Gomez', 'blocker': 'Waiting for database credentials', 'dependency': 'Database/Admin team'},
            {'employee': 'Liam Chen', 'blocker': 'Customer data dependency', 'dependency': 'Customer Data team'}
        ],
        'risk_breakdown': {
            'HIGH': 2,
            'MEDIUM': 3,
            'LOW': 7
        },
        'escalation_rules': ['Blocker persists > 2 days', 'Risk = HIGH', 'Critical dependency unresolved'],
        'manager_attention_required': True,
    }


@app.get('/leadership')
def leadership_metrics():
    return {
        'demo_label': 'Demo / Illustrative Data',
        'adoption_rate': 65,
        'update_completion_rate': 91,
        'blocker_confirmation_rate': 86,
        'ai_correction_rate': 14,
        'manager_time_saved_hours': 18,
        'high_risk_escalation_rate': 32,
        'recurring_blocker_rate': 27,
        'updates_reviewed_percent': 74,
        'project_health': {
            'Project Alpha': 'YELLOW',
            'Customer Portal': 'RED',
            'Data Quality Initiative': 'GREEN'
        }
    }


@app.get('/updates')
def get_updates():
    return {'updates': UPDATES}


@app.post('/reviews')
def save_review_action(payload: ReviewPayload):
    return save_review(payload.update_id, payload.status, payload.reviewed_by, payload.edited_value)


@app.get('/reviews')
def get_reviews():
    return {'reviews': list_reviews()}


@app.get('/init-db')
def init_database():
    init_db()
    return {'message': 'database initialized'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
