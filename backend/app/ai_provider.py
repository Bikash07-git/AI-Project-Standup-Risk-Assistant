import os

from app.ai_service import analyze_update


def get_active_provider_name():
    return (os.getenv('AI_PROVIDER') or 'demo').lower()


def get_ai_analysis(payload, previous_updates=None):
    provider_name = get_active_provider_name()
    if provider_name in {'demo', 'mock', 'deterministic'} or not os.getenv('OPENAI_API_KEY'):
        return analyze_update(payload, previous_updates or [])

    # Clean provider abstraction for future integrations.
    # Real API calls can be added here without changing the app contract.
    return analyze_update(payload, previous_updates or [])
