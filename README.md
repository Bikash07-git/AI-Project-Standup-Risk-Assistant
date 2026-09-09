<div align="center">

# 🚀 AI Project Stand-up & Risk Assistant

### From scattered daily updates to actionable project insights — powered by AI

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Styling-38B2AC?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#-license)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#-contributing)

[🎥 Watch the Demo](https://www.loom.com/share/643ecf69a5f54f0295b27dc246950db5) · [📄 Report a Bug](../../issues) · [✨ Request a Feature](../../issues)

</div>

---

## 📌 Table of Contents

<details open>
<summary>Click to expand</summary>

- [Overview](#-overview)
- [The Problem](#-the-problem)
- [The Solution](#-the-solution)
- [How It Works — End-to-End Flow](#-how-it-works--end-to-end-flow)
- [Architecture / Workflow Diagram](#-architecture--workflow-diagram)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Design Principles](#-design-principles)
- [30-Day Pilot Review](#-30-day-pilot-review)
- [Roadmap](#-roadmap)
- [AI Design Log](#-ai-design-log)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

</details>

---

## 🧭 Overview

**AI Project Stand-up & Risk Assistant** turns messy, scattered daily stand-up updates into **structured, actionable project insights** — helping managers spot blockers, risks, and next actions in seconds instead of hours.

Built for the *NxtWave Associate Project Management Intern* assignment, this project simulates a real AI-Native operations workflow: employees submit updates, AI analyzes and structures them, and managers validate the output through a review dashboard — with AI accelerating the work while humans keep final decision-making authority.

---

## ❗ The Problem

> Project updates in Central Operations are scattered across different channels and shared in inconsistent formats.

This creates real friction:

| Pain Point | Impact |
|---|---|
| 🔀 Updates scattered across channels | Managers waste time hunting for status |
| 🕵️ Manual follow-ups | Slower detection of blockers |
| 📝 Inconsistent formats | Hard to consolidate into one report |
| ⏰ Delayed visibility | Risks surface too late to act on |

**Why it matters:** without a timely, reliable view of project health, small blockers become big delays — and leadership loses trust in the numbers.

---

## 💡 The Solution

An AI-powered pipeline that converts free-form or structured stand-up updates into **consistent, decision-ready insights**:

- ✅ Completed & ongoing tasks
- 🚧 Blockers & dependencies
- ⚠️ Risk level (Low / Medium / High) + reasoning
- 🎯 Recommended next action
- 📊 AI confidence score

Managers then **Confirm / Edit / Reject / Resolve** each insight from a centralized dashboard — so the AI acts as a *first-level analyst*, not the final decision-maker.

> **Core design principle:** uncertain information is flagged for manager review — never presented as a confirmed blocker.

---

## 🔄 How It Works — End-to-End Flow

```
Employee Update  →  AI Analysis  →  Structured Insights  →  Manager Validation  →  Project Health & Actions
```

<details>
<summary><strong>1️⃣ Employee Input</strong></summary>

Team members submit a daily stand-up via a web app (text or structured form):
- What I worked on
- What I'm working on
- Blockers / Issues
- Any risks or concerns
</details>

<details>
<summary><strong>2️⃣ Backend Processing</strong></summary>

- **FastAPI** handles incoming API requests
- Input is cleaned and pre-processed into a common structure
</details>

<details>
<summary><strong>3️⃣ AI Analysis (LLM / OpenAI)</strong></summary>

- Extracts completed & ongoing tasks
- Detects blockers and roadblocks
- Classifies risk level (Low / Medium / High)
- Suggests next-step actions
- Attaches a confidence score to its own analysis
</details>

<details>
<summary><strong>4️⃣ Structured Output</strong></summary>

A clean, standardized report containing tasks, blockers/issues, risk level + reason, an AI-generated summary, and a confidence score (e.g. 0.87 / 87%).
</details>

<details>
<summary><strong>5️⃣ Manager Review</strong></summary>

Managers view the AI-analyzed report and can:
- Validate or edit insights
- Track project health
- Take necessary action

All of this feeds a **Project Health Dashboard** — team progress, risk trends, blocker overview, and action tracking.
</details>

<details>
<summary><strong>6️⃣ Continuous Improvement</strong></summary>

Manager feedback (Confirm / Edit / Reject / Resolve) loops back to improve future AI analysis.
</details>

---

## 🏗 Architecture / Workflow Diagram

<div align="center">

*(Add the workflow diagram image to your repo, e.g. `docs/workflow-diagram.png`, then it will render below)*

```markdown
![Workflow Diagram](docs/workflow-diagram.png)
```

</div>

**Pipeline at a glance:**

```
┌────────────┐   ┌───────────────────┐   ┌───────────────┐   ┌──────────────────┐   ┌────────────────┐
│  Employee  │ → │ Backend Processing │ → │  AI Analysis  │ → │ Structured Output │ → │ Manager Review │
│   Input    │   │  (FastAPI + Prep)  │   │  (LLM/OpenAI) │   │  (Tasks/Risks)    │   │  (Dashboard)   │
└────────────┘   └───────────────────┘   └───────────────┘   └──────────────────┘   └────────────────┘
                                                                                              │
                                                                                              ▼
                                                                                 ┌─────────────────────────┐
                                                                                 │ Continuous Improvement  │
                                                                                 │  (Feedback → Better AI) │
                                                                                 └─────────────────────────┘
```

---

## ✨ Key Features

- 🧠 **AI-Powered Extraction** — tasks, blockers, dependencies, and risks pulled automatically from raw updates
- 🚦 **Risk Classification** — Low / Medium / High with a plain-language reason
- 📈 **Confidence Scoring** — every AI insight is scored, not blindly trusted
- 🧑‍💼 **Human-in-the-loop Validation** — Confirm / Edit / Reject / Resolve on every insight
- 📊 **Project Health Dashboard** — team progress, risk trends, blocker overview, action tracking
- 🔁 **Feedback Loop** — manager decisions continuously improve future AI analysis
- 🧩 **Format-agnostic input** — structured form or free-form text, standardized by AI

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?logo=fastapi&logoColor=white) |
| AI / LLM | ![OpenAI](https://img.shields.io/badge/-OpenAI%20API-412991?logo=openai&logoColor=white) |
| Frontend | ![React](https://img.shields.io/badge/-React-61DAFB?logo=react&logoColor=black) ![TailwindCSS](https://img.shields.io/badge/-TailwindCSS-38B2AC?logo=tailwindcss&logoColor=white) |
| Versioning | ![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- An OpenAI API key

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/ai-standup-risk-assistant.git
cd ai-standup-risk-assistant

# 2. Backend setup
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # add your OPENAI_API_KEY here
uvicorn main:app --reload

# 3. Frontend setup (in a new terminal)
cd frontend
npm install
npm run dev
```

The app will be available at `http://localhost:5173` (frontend) and `http://localhost:8000` (API).

> ⚠️ Replace commands/paths above with your actual project structure and scripts before publishing.

---

## 📂 Project Structure

```
ai-standup-risk-assistant/
├── backend/
│   ├── main.py              # FastAPI entry point
│   ├── routes/               # API routes
│   ├── services/              # AI analysis & preprocessing logic
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/              # Dashboard, Submit Update, etc.
│   │   └── App.jsx
│   └── package.json
├── docs/
│   └── workflow-diagram.png
└── README.md
```

---

## 🎯 Design Principles

1. **AI assists, humans decide.** The AI never auto-confirms a blocker or risk — managers hold final authority.
2. **Uncertainty is surfaced, not hidden.** Low-confidence insights are routed for review instead of being presented as fact.
3. **Standardize without adding friction.** Any input format (form or free text) is normalized by AI, not by forcing rigid templates on employees.
4. **Feedback compounds.** Manager actions (Confirm/Edit/Reject/Resolve) become training signal for better future analysis.

---

## 📈 30-Day Pilot Review

After piloting across three teams, five key challenges emerged:

| # | Challenge | Likely Cause |
|---|---|---|
| 1 | Adoption ~65% | Feels like an extra reporting step |
| 2 | AI misses context / misclassifies blockers | Insufficient historical/project context |
| 3 | Inconsistent reporting styles | Teams use different formats & terminology |
| 4 | Workflow bypassing via chat | Chat feels faster and more familiar |
| 5 | Unreliable leadership metrics | Data & insight definitions aren't standardized |

**Top 3 prioritized (Trust → Adoption → Complete Data):**
1. 🎯 **AI Accuracy & Context** — managers must trust outputs before acting on them
2. 📉 **Workflow Adoption** — low usage starves the system of data
3. 🔀 **Workflow Bypassing** — off-workflow updates create blind spots

**Improved solution highlights:**
- AI now factors in historical updates, unresolved blockers, and past manager decisions
- **Confidence-based validation:** `AI Analysis → Confidence Check → Manager Review → Confirm/Edit/Reject/Resolve`
- Flexible input (structured *or* free-form), normalized by AI
- **Escalation ladder:** `Informational → Needs Review → Confirmed Risk → Escalation` — only validated high-priority risks reach leadership

**Success metrics to track:**

- [ ] Workflow Adoption Rate
- [ ] AI Insight Accuracy (manager-confirmed rate)
- [ ] Manager Validation Rate
- [ ] Blocker Resolution Time
- [ ] Reporting Completeness

---

## 🗺 Roadmap

- [ ] Deeper historical context modeling for higher AI accuracy
- [ ] Stronger feedback loop from Confirm/Edit/Reject/Resolve actions
- [ ] Native integration with existing chat tools (e.g., Slack/Teams) to reduce bypassing
- [ ] Org-wide rollout with standardized metric definitions
- [ ] Automated executive briefing generation

---

## 🤖 AI Design Log

<details>
<summary><strong>Click to expand full AI collaboration log</strong></summary>

**AI Tools Used**
- ChatGPT — problem framing, workflow design, prompt refinement, architecture planning, testing & documentation
- Antigravity — application development & implementation
- VS Code — code editing, debugging, local testing

**Initial Prompt**
> Build an AI-powered project stand-up assistant that collects employee updates, identifies completed tasks, ongoing work, blockers, dependencies and risks, and generates actionable summaries for managers.

**Refined Prompt**
> Build a context-aware AI Project Stand-up & Risk Assistant where employee updates are analyzed for tasks, blockers, dependencies and risks. Include confidence scoring, recommended actions, historical context, manager validation through Confirm/Edit/Reject/Resolve, project health monitoring, escalation logic and leadership metrics. Do not treat uncertain information as a confirmed blocker; surface low-confidence cases for human review.

**Iterations:** ~8–12, covering workflow design, UI improvements, AI behavior, validation logic, context retention, dashboard functionality, testing and documentation.

**Knowledge Sources:** assignment brief & business scenario, project requirements/assumptions, seeded demo data, iterative testing observations.

**Validation & Learning**
- Validated end-to-end using seeded demo data, reviewing blockers/risks/actions through the manager dashboard
- AI suggestions lacking sufficient context were **not** treated as confirmed blockers — routed for manager review instead
- Adding human validation + confidence-based decision logic was the single biggest improvement, ensuring AI assists rather than decides unilaterally

</details>

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👤 Author

**Bikash Sagar Koiri**

[![Loom Demo](https://img.shields.io/badge/Watch-Demo-8B5CF6?logo=loom&logoColor=white)](https://www.loom.com/share/643ecf69a5f54f0295b27dc246950db5)

<div align="center">

⭐ If this project helped you think about AI-native operations workflows, consider giving it a star!

</div>
