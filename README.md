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

# 🎯 Overview

The **AI Project Stand-up & Risk Assistant** is a prototype designed to reduce the manual effort involved in collecting, consolidating, and interpreting project updates.

Employees submit their daily project updates through the application. The system then analyzes the information and converts it into structured project insights that managers can review and act upon.

The assistant focuses on identifying:

- ✅ Completed tasks
- 🔄 Ongoing tasks
- 🚧 Blockers and issues
- 🔗 Dependencies
- ⚠️ Potential risks
- 📊 Risk levels
- 💡 Recommended next actions
- 🎯 AI confidence

The solution is designed around a **human-in-the-loop approach**, where AI assists with analysis while managers retain final decision-making authority.

---

# ❗ Problem Statement

Project updates can be scattered across different communication channels and shared in inconsistent formats.

This creates several operational challenges:

- Managers spend significant time collecting updates.
- Blockers and dependencies may be identified late.
- Project health is difficult to assess quickly.
- Stakeholder reporting becomes repetitive and manual.
- Important project context can be missed.

The objective of this project is to create an AI-powered workflow that converts employee stand-up updates into **structured, actionable project insights**.

---

# 💡 Solution

## AI Project Stand-up & Risk Assistant

The solution creates a focused workflow for converting employee updates into manager-ready project intelligence.

Employees can provide updates through structured inputs or free-form text.

The system analyzes the submitted information and produces structured insights around tasks, blockers, dependencies, risks, recommended actions, and confidence.

### Core Workflow

```text
Employee Update
       ↓
AI Analysis
       ↓
Structured Insights
       ↓
Manager Validation
       ↓
Project Health
       ↓
Actions / Escalation
