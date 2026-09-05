# SIH
🧠 ML / Stress Prediction Model

The core intelligence of this system is a Random Forest Classifier that predicts a personnel member's stress risk level — Low, Medium, or High — using duty, leave, deployment, and wellness indicators. The model outputs class probabilities rather than a flat label, allowing welfare officers to see a graded risk signal instead of a binary flag.

📖 ML/FEATURE_RATIONALE.md (./ML/FEATURE_RATIONALE.md): Why each input field was chosen — grounded in research on military, paramilitary, and CAPF-specific occupational stress (IIM Ahmedabad's paramilitary stress study, MHA task force findings, WHO/ILO long-working-hours research, and military sleep studies).

⚙️ ML/MODEL_METHODOLOGY.md (./ML/MODEL_METHODOLOGY.md): How the model actually works — the data pipeline, why Random Forest was chosen, class-balancing strategy, evaluation metrics, and why recall on high-risk cases is prioritized over raw accuracy.

Quick highlights:

🎯 81.8% overall accuracy, with 77.3% recall on the High-risk class — the metric that matters most for a welfare-monitoring tool.

⚖️ Class-balanced training to avoid the model defaulting to the majority (Low-risk) class.

🔍 Every feature is traceable to a specific research citation — see the rationale doc for the full breakdown, including an honest note on which fields still need stronger domain-specific backing.
