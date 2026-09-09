# AI Project Stand-up & Risk Assistant

## Project Name

AI Project Stand-up & Risk Assistant

## Problem Statement

Managers are losing valuable time collecting scattered project updates, identifying blockers, tracking dependencies, and preparing summary reports. The current process is manual, inconsistent, and slows decision-making across teams.

## Why This Problem Matters

When updates are fragmented, leadership cannot act quickly on risk. Small blockers become delivery delays, and teams waste time re-asking for status instead of resolving work.

## Proposed Solution

This prototype creates a focused AI-native workflow that collects structured updates, normalizes free-form input, detects blockers and dependencies, remembers recurring context, and produces manager-ready summaries with recommendation logic.

## Key Features

- Structured employee update form
- Free-form update normalization
- AI-based task, blocker, dependency, and risk extraction
- Historical context for recurring blockers
- Manager review and validation controls
- Project dashboard and leadership metrics
- Demo mode for live product walkthroughs
- AI copilot for operational queries

## Architecture

The solution uses a simple layered architecture:

- Frontend: React + Vite dashboard UI
- Backend: FastAPI API service
- AI layer: clean analysis abstraction with deterministic fallback logic
- Data layer: SQLite-ready schema and seeded demo dataset
- Demo mode: realistic sample data for presentations when no API key is available

## Tech Stack

- Frontend: React, Vite, CSS
- Backend: Python, FastAPI
- AI abstraction: isolated service layer
- Database: SQLite-ready schema
- Validation: pytest

## Setup Instructions

1. Open a terminal in the project root.
2. Create and activate the Python environment if needed.
3. Install backend dependencies:
   - cd backend
   - ../.venv/Scripts/python.exe -m pip install -r requirements.txt
4. Install frontend dependencies:
   - cd frontend
   - npm install
5. Copy and configure environment values if an LLM is later added:
   - copy .env.example to .env

## Environment Variables

See [.env.example](.env.example) for the environment template.

Required values for the current demo build:

- OPENAI_API_KEY: optional, currently not required for demo mode
- AI_PROVIDER: default value to keep provider logic isolated
- AI_MODEL: model name for future API integration
- FASTAPI_HOST: default 0.0.0.0
- FASTAPI_PORT: default 8000
- FRONTEND_URL: default http://localhost:5173

## Running the Backend

From the project root:

cd backend
../.venv/Scripts/python.exe -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

## Running the Frontend

From the project root:

cd frontend
npm run dev -- --host 0.0.0.0

## Demo Mode

The application is designed to work without an external AI API key. If no API key is configured, the app uses deterministic mock analysis and seeded realistic data.

## Testing Instructions

Run backend tests from the backend folder:

../.venv/Scripts/python.exe -m pytest -q

Run frontend build validation:

cd frontend
npm run build

## Known Limitations

- Current demo analysis is deterministic and local, not connected to a production LLM
- The app uses seeded data for a realistic demo rather than live enterprise data
- Human review is manually handled in the UI

## Future Improvements

- Add provider-based model integration for OpenAI or Azure OpenAI
- Save and persist manager review states in SQLite
- Add true API-level AI analysis with prompt engineering and evaluation
- Expand executive reporting and project-trend analytics

## Workflow Diagram

See [WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md).
