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
