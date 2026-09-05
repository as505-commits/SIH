# SIH26186 - AI-Based Predictive Personnel Stress and Welfare Monitoring System for Uniformed Forces
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
>
> 🖥️ Frontend / Welfare Monitoring Web App

The application is a role-gated Streamlit web app that provides separate views for officers and supervisors. Officers can privately record their wellbeing, while supervisors receive aggregated and appropriately restricted assessment data.

👮 For Officers

📊 Stress Assessment

Provides a structured form covering:

Duty load

Sleep patterns

Deployment history

Leave patterns

Support factors

Sends the submitted data to the backend API.

Displays the Random Forest model’s:

Risk level: Low, Medium, or High

Recommendations

Contributing risk factors

The frontend does not perform prediction logic.

📝 Daily Journal

Provides a private space for recording mood and personal reflections.

Journal entries are accessible only to the respective officer.

🌿 Stress Relief Centre

Includes a guided 5-4-3-2-1 grounding exercise.

Provides a paced breathing routine.

Offers quick relaxation techniques for immediate support.

🚨 Emergency Support

Provides access to national emergency services through 112.

Provides access to the Tele-MANAS helpline through 14416.

Allows officers to save a personal SOS contact and call it directly.

🧑‍✈️ For Supervisors

📋 All Officer Records

Displays a consolidated view of submitted assessment records.

Supports searching and reviewing records across the unit.

⚠️ High-Risk Alerts

Automatically filters officers classified as High risk.

Helps supervisors prioritise personnel who may require support.

👤 Officer Search

Allows supervisors to search for individual officers.

Displays their assessment history and submitted responses, subject to access restrictions.

📈 Command Dashboard

Displays the total number of assessments.

Shows the distribution of Low, Medium, and High risk classifications.

Provides an overview of stress patterns across personnel.

🎯 Key Features

🔐 Role-based access

Officers and supervisors receive different views and data permissions.

🔗 API-driven predictions

Assessment data is sent to the backend.

The frontend displays the prediction and explanation returned by the ML model.

🧘 Preventative support

Combines stress monitoring with immediate coping and relaxation resources.

🕵️ Confidentiality-focused design

Journal entries remain private to the officer.

Supervisors receive assessment outcomes rather than personal reflections.

📱 Simple and accessible interface

Designed for quick interaction.

Provides clear risk indicators, recommendations, and support options.
