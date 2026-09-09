# AI Design Log

## 1. AI Tools Used

- Local Python analysis logic for structured extraction and demo fallback rules
- FastAPI endpoints for AI-style analysis exposure
- Human review flow for validation and edits
- Demo mode with deterministic rules instead of live model calls

## 2. Initial Workflow Prompt

"Analyze daily employee project updates, extract tasks, blockers, dependencies, risks, and recommended actions, then summarize them for managers."

## 3. Refined Workflow Prompt

"Review each update as a structured operational record. Separate employee-provided facts from AI-inferred conclusions. Highlight blockers and risks only when evidence exists. If a blocker repeats across prior updates, increase risk and recommend escalation. Show confidence and allow human review."

## 4. Approximate Iterations

The project used a small number of iterations. The exact count can be updated by the user as needed, but the workflow was refined through:

- initial extraction logic
- recurrence handling for blockers
- risk classification review
- human validation and UI clarity tuning

## 5. Knowledge/Data Sources Used

- Assignment brief and scenario requirements
- Realistic operational update examples from project management workflows
- Seeded project and employee data modeled to mirror common internal operations scenarios

## 6. Architecture / Workflow

Employee update -> normalization -> AI analysis -> blocker/dependency/risk extraction -> confidence check -> manager validation -> dashboard and leadership metrics

## 7. Validation Approach

The backend logic was validated through targeted tests covering:

- healthy update behavior
- clear blocker detection
- recurring blocker escalation
- no false blocker creation
- dashboard summary integrity

## 8. One AI Suggestion Rejected

A larger feature proposal to fully automate risk decisions without human validation was rejected.

## 9. Why It Was Rejected

This would have removed the manager from the loop, which contradicts the assignment requirement for human confirmation and validation.

## 10. One Iteration That Significantly Improved the Solution

The recurring blocker logic was a major improvement because it allowed the system to treat repeated unresolved dependencies as high-risk operational issues rather than isolated status notes.
