# 🤖 AI Project Stand-up & Risk Assistant

<p align="center">
  <strong>From daily project updates to actionable project intelligence — powered by AI</strong>
</p>

<p align="center">
  An AI-native project operations assistant that helps managers collect updates,
  identify blockers and risks, validate AI-generated insights, and improve project visibility.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Prototype-success?style=for-the-badge" alt="Project Status">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react" alt="React">
  <img src="https://img.shields.io/badge/Vite-Build-646CFF?style=for-the-badge&logo=vite" alt="Vite">
  <img src="https://img.shields.io/badge/SQLite-Ready-003B57?style=for-the-badge&logo=sqlite" alt="SQLite">
  <img src="https://img.shields.io/badge/Testing-pytest-0A9EDC?style=for-the-badge&logo=pytest" alt="pytest">
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-problem-statement">Problem</a> •
  <a href="#-solution">Solution</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-setup">Setup</a> •
  <a href="#-demo-mode">Demo Mode</a> •
  <a href="#-testing">Testing</a> •
  <a href="#-limitations">Limitations</a>
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [How It Works](#-how-it-works)
- [Features](#-features)
- [Architecture](#-architecture)
- [Workflow Diagram](#-workflow-diagram)
- [Application Modules](#-application-modules)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup](#-setup)
- [Environment Variables](#-environment-variables)
- [Running the Application](#-running-the-application)
- [Demo Mode](#-demo-mode)
- [Testing](#-testing)
- [AI Design Principles](#-ai-design-principles)
- [Known Limitations](#-known-limitations)
- [Future Improvements](#-future-improvements)
- [Documentation](#-documentation)
- [Demo](#-demo)
- [Repository](#-repository)
- [Author](#-author)

---

# 📌 Overview

> **AI Project Stand-up & Risk Assistant**  
> *From daily updates to actionable project insights — powered by AI.*

The **AI Project Stand-up & Risk Assistant** is an AI-powered project management workflow designed to transform employee stand-up updates into **structured, actionable project intelligence**.

Instead of requiring managers to manually collect and consolidate updates, the system analyzes employee inputs and surfaces important information such as:

- 📝 Completed and ongoing tasks
- 🚧 Blockers and issues
- 🔗 Dependencies
- ⚠️ Potential project risks
- 💡 Recommended next actions
- 🎯 AI confidence levels

### 🎯 Project Goal

The goal is to help project managers **understand project health faster, identify potential risks earlier, and reduce repetitive information-collection effort**.

The system follows a **Human-in-the-Loop** approach:

```text
Employee Update
       ↓
   AI Analysis
       ↓
Structured Insights
       ↓
 Manager Review
       ↓
Confirm / Edit / Reject / Resolve
       ↓
Project Health & Actions

### 🧩 Problem Statement

Project updates in Central Operations are often **scattered across multiple channels** and shared in **inconsistent formats**.

Managers spend significant time:

- 📥 Collecting updates from employees
- 🔄 Following up for missing information
- 🚧 Identifying blockers and dependencies
- ⚠️ Understanding project risks
- 📊 Consolidating project status
- 📑 Preparing stakeholder reports

Because information is fragmented and reporting styles vary, managers may not get a **timely and consistent view of project health**.

### ❗ Core Problem

> **Managers need a faster and more reliable way to convert scattered daily project updates into structured information that highlights progress, blockers, dependencies, risks, and required actions.**

### 🎯 Problem to Solve

The solution should reduce the manual effort involved in:

```text
Collecting Updates
       ↓
Consolidating Information
       ↓
Finding Blockers
       ↓
Identifying Risks
       ↓
Understanding Project Health
       ↓
Deciding What Needs Attention

# 💡 Solution

## 🤖 AI Project Stand-up & Risk Assistant

The proposed solution is an **AI-powered stand-up and project-risk assistant** that converts employee daily updates into structured, actionable project insights.

Employees submit their updates through a centralized web application. The AI then analyzes the information and identifies important project signals such as tasks, blockers, dependencies, risks, and recommended actions.

### 🔄 Solution Flow

```text
┌──────────────────────┐
│  👤 Employee Update  │
│                      │
│ • Completed Work     │
│ • Current Work       │
│ • Blockers           │
│ • Dependencies       │
│ • Risks / Concerns   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   🤖 AI Analysis     │
│                      │
│ • Task Extraction    │
│ • Blocker Detection  │
│ • Risk Assessment    │
│ • Action Suggestions │
│ • Confidence Score   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 📋 Structured Output │
│                      │
│ Tasks                │
│ Blockers             │
│ Dependencies         │
│ Risks                │
│ Recommended Actions  │
│ Confidence           │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 👤 Manager Review    │
│                      │
│ Confirm / Edit       │
│ Reject / Resolve     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 📊 Project Health    │
│                      │
│ Risks • Blockers     │
│ Progress • Actions   │
└──────────────────────┘
