# SIH26186 — AI-Based Predictive Personnel Stress and Welfare Monitoring System for Uniformed Forces

An AI-powered welfare monitoring platform that helps identify early indicators of stress, burnout, and psychological distress among personnel in Central Armed Police Forces (CAPFs), Armed Forces, and other uniformed services — enabling proactive welfare support instead of reactive intervention.

---

## 📌 Table of Contents

- [Problem Statement](#-problem-statement)
- [Why This Matters](#-why-this-matters)
- [System Overview](#-system-overview)
- [Repository Structure](#-repository-structure)
- [ML / Stress Prediction Model](#-ml--stress-prediction-model)
- [Frontend — Welfare Monitoring Web App](#-frontend--welfare-monitoring-web-app)
- [Backend](#-backend)
- [Key Design Principles](#-key-design-principles)
- [Disclaimer](#-disclaimer)

---

## 🎯 Problem Statement

Personnel serving in CAPFs, Armed Forces, and other uniformed services operate under physically demanding, psychologically stressful, and often hazardous conditions. Extended deployments, operational pressures, separation from families, irregular working hours, and exposure to traumatic incidents can significantly impact mental well-being.

Stress identification today largely depends on manual observation and self-reporting — a process that delays timely intervention. This project builds a **proactive, technology-driven solution** that identifies early indicators of stress, burnout, and welfare concerns while maintaining personnel privacy and organizational trust.

The system analyzes:
- Leave patterns, deployment history, duty schedules, transfer frequency, training commitments, and workload trends
- Optional self-reported wellness assessments
- Behavioral patterns associated with elevated stress risk

...to generate risk assessments and welfare recommendations for authorized welfare officers and commanders — with a strict focus on **welfare support, not disciplinary action.**

## 💡 Why This Matters

| Expected Benefit | Impact |
|---|---|
| Early identification of at-risk personnel | Enables timely welfare intervention before crisis point |
| Reduced stress-related incidents | Lower operational fatigue and burnout across units |
| Improved workforce resilience | Stronger long-term readiness and retention |
| Data-driven welfare planning | Better resource allocation for counseling and support programs |
| Preventive rather than reactive care | Shifts welfare management from crisis response to early support |

---

## 🏗️ System Overview

The platform is built as three integrated components:

```
┌─────────────────┐       ┌──────────────────┐       ┌─────────────────────┐
│   Frontend       │       │    Backend        │      │   ML Engine          │
│  (Streamlit)     │──────▶│  (Java / API)     │─────▶│ (Random Forest)      │
│  Officer &       │◀──────│  Auth, storage,   │◀─────│ Risk classification  │
│  Supervisor Views│       │  role-based access │      │ + probability scores │
└─────────────────┘       └──────────────────┘       └─────────────────────┘
```

Officers submit structured wellness assessments through the frontend → the backend securely stores and routes this data → the ML engine returns a risk classification (Low / Medium / High) with contributing factors → supervisors see only aggregated, access-controlled outcomes, never raw personal reflections.

---

## 📁 Repository Structure

```
SIH/
├── ML/
│   ├── FEATURE_RATIONALE.md      # Research basis for each model input
│   ├── MODEL_METHODOLOGY.md      # How the model works, evaluation metrics
│   ├── Confusion_matrix.png
│   └── (training scripts, dataset, model.pkl)
├── backend/                      # API, auth, role-based access, data storage
├── frontend/                     # Streamlit officer/supervisor web app
└── README.md
```

---

## 🧠 ML / Stress Prediction Model

The core intelligence of this system is a **Random Forest Classifier** that predicts a personnel member's stress risk level — **Low, Medium, or High** — using duty, leave, deployment, and wellness indicators.

The model outputs **class probabilities** rather than a flat label, allowing welfare officers to see a graded risk signal instead of a binary flag.

### 📚 Model Documentation

📖 **[Feature Rationale](./ML/FEATURE_RATIONALE.md)**
Why each input field was chosen, with supporting research on military, paramilitary, and CAPF-specific occupational stress.

⚙️ **[Model Methodology](./ML/MODEL_METHODOLOGY.md)**
How the model works, including the data pipeline, Random Forest architecture, class-balancing strategy, evaluation metrics, and why recall on high-risk cases is prioritized.

### 🎯 Quick Highlights

- 🎯 **81.8% overall accuracy**
- 🚨 **77.3% recall on the High-risk class** — the metric prioritized for a welfare-monitoring system
- ⚖️ **Class-balanced training** to reduce bias toward the majority Low-risk class
- 🔍 **Explainable predictions** with feature-level reasoning
- 📊 **Probability-based risk assessment** across Low, Medium, and High categories
- 📚 **Research-backed feature selection**, with limitations transparently documented

> **Note:** The prototype was trained and evaluated using a synthetically generated, domain-informed dataset due to the sensitive and restricted nature of real personnel welfare data. Real-world deployment would require validation using authorized, appropriately governed personnel data.

---

## 🖥️ Frontend — Welfare Monitoring Web App

The application is a role-gated Streamlit web app that provides separate views for officers and supervisors. Officers can privately record their wellbeing, while supervisors receive aggregated and appropriately restricted assessment data.

### 👮 For Officers

**📊 Stress Assessment**

Provides a structured form covering:
- Duty load
- Sleep patterns
- Deployment history
- Leave patterns
- Support factors

Sends the submitted data to the backend API. Displays the Random Forest model's:
- Risk level: Low, Medium, or High
- Recommendations
- Contributing risk factors

*The frontend does not perform prediction logic.*

**📝 Daily Journal**

Provides a private space for recording mood and personal reflections. Journal entries are accessible only to the respective officer.

**🌿 Stress Relief Centre**
- Guided 5-4-3-2-1 grounding exercise
- Paced breathing routine
- Quick relaxation techniques for immediate support

**🚨 Emergency Support**
- Access to national emergency services through 112
- Access to the Tele-MANAS helpline through 14416
- Save a personal SOS contact and call it directly

### 🧑‍✈️ For Supervisors

**📋 All Officer Records** — Consolidated view of submitted assessment records, with search and review across the unit.

**⚠️ High-Risk Alerts** — Automatically filters officers classified as High risk, helping supervisors prioritise personnel who may require support.

**👤 Officer Search** — Search for individual officers and view their assessment history, subject to access restrictions.

**📈 Command Dashboard** — Total number of assessments, distribution of Low/Medium/High classifications, and an overview of stress patterns across personnel.

### 🎯 Key Features

- 🔐 **Role-based access** — Officers and supervisors receive different views and data permissions
- 🔗 **API-driven predictions** — Assessment data is sent to the backend; the frontend displays the prediction and explanation returned by the ML model
- 🧘 **Preventative support** — Combines stress monitoring with immediate coping and relaxation resources
- 🕵️ **Confidentiality-focused design** — Journal entries remain private to the officer; supervisors receive assessment outcomes rather than personal reflections
- 📱 **Simple and accessible interface** — Designed for quick interaction with clear risk indicators, recommendations, and support options

---

## ⚙️ Backend

Handles authentication, role-based access control, personnel record storage, and routing of assessment data to the ML engine. Acts as the single source of truth between the frontend and the model — the frontend never talks to the model directly.

*(Add setup/run instructions here — build tool, environment variables, database, etc.)*

---

## 🔑 Key Design Principles

- **Privacy-first** — personal reflections and raw wellness data are never exposed to supervisors; only classified risk outcomes are shared, on a need-to-know basis
- **Welfare over discipline** — the system is designed to trigger support, not punitive action
- **Minimizing false negatives** — model training explicitly prioritizes recall on the High-risk class, since a missed at-risk individual is the most costly failure mode
- **Explainability** — predictions come with contributing risk factors, not an opaque score
- **Research-grounded** — every model feature is traceable to documented occupational-stress research in military/CAPF populations (see [Feature Rationale](./ML/FEATURE_RATIONALE.md))

---

## ⚠️ Disclaimer

This is a **prototype developed for academic/hackathon pre-screening evaluation**. Due to the sensitivity and restricted availability of real CAPF/Armed Forces personnel data, the training dataset is synthetically generated, informed by published occupational-stress research rather than direct field data collection. Reported model metrics reflect performance on this synthetic dataset and demonstrate the viability of the approach — they are not a validated measure of real-world predictive accuracy. Production deployment would require training and validation on authorized, properly governed personnel data under appropriate ethical and legal oversight.
