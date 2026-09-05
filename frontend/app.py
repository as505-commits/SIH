
import streamlit as st
import pandas as pd
import time
from datetime import datetime

import requests
import streamlit as st

JAVA_API_URL = "http://10.79.49.90:8080/api/personnel/analyze"


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Personnel Welfare Monitoring System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# SESSION STATE INITIALIZATION
# =========================================================

if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "Dark Mode"  # DEFAULT SET TO DARK MODE

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "username" not in st.session_state:
    st.session_state.username = None

if "officer_records" not in st.session_state:
    st.session_state.officer_records = []

if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

if "emergency_contact_name" not in st.session_state:
    st.session_state.emergency_contact_name = ""

if "emergency_contact_phone" not in st.session_state:
    st.session_state.emergency_contact_phone = ""


# =========================================================
# CLINICAL BIOME PALETTE & UPGRADED STYLING ENGINE
# =========================================================

is_dark = st.session_state.theme_mode == "Dark Mode"

bg_app = "#090d16" if is_dark else "#F8FAFC"
card_bg = "#0f172a" if is_dark else "#FFFFFF"
card_border = "#1e293b" if is_dark else "#E2E8F0"
text_main = "#f8fafc" if is_dark else "#0F172A"
text_sub = "#94a3b8" if is_dark else "#64748B"
input_bg = "#1e293b" if is_dark else "#FFFFFF"
input_text = "#ffffff" if is_dark else "#0F172A"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: {text_main};
    }}

    .stApp {{
        background-color: {bg_app} !important;
    }}

    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 1280px;
    }}

    div[data-testid="column"] {{
        padding: 0 0.35rem !important;
    }}

    .stVerticalBlock {{
        gap: 0.95rem !important;
    }}

    /* SIDEBAR STYLING */
    [data-testid="stSidebar"] {{
        background-color: #0F172A !important;
        border-right: 1px solid #1E3A5F !important;
    }}

    [data-testid="stSidebar"] * {{
        color: #F8FAFC !important;
    }}

    [data-testid="stSidebar"] .stRadio label {{
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        padding: 10px 14px !important;
        border-radius: 8px !important;
    }}

    /* ENHANCED & LARGER TYPOGRAPHY */
    h1 {{
        font-size: 2.6rem !important;
        font-weight: 800 !important;
        color: {text_main} !important;
        letter-spacing: -0.025em;
        margin-bottom: 0.5rem !important;
    }}

    h2 {{
        font-size: 2.0rem !important;
        font-weight: 700 !important;
        color: {text_main} !important;
        margin-top: 1.0rem !important;
        margin-bottom: 0.5rem !important;
    }}

    h3 {{
        font-size: 1.6rem !important;
        font-weight: 700 !important;
        color: {text_main} !important;
        margin-top: 0.75rem !important;
        margin-bottom: 0.5rem !important;
    }}

    p, span, label {{
        font-size: 1.1rem !important;
        color: {text_main};
        line-height: 1.55;
    }}

    .sub-text {{
        color: {text_sub} !important;
        font-size: 1.05rem !important;
    }}

    /* WELCOME BANNER */
    .welcome-banner {{
        background: linear-gradient(135deg, #0F172A 0%, #1E3A5F 100%);
        color: #FFFFFF !important;
        padding: 28px 34px;
        border-radius: 14px;
        border: 1px solid #1E3A5F;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.15);
        margin-bottom: 16px;
    }}

    .welcome-banner h1 {{
        color: #FFFFFF !important;
        font-size: 2.75rem !important;
        margin-bottom: 8px !important;
    }}

    .welcome-banner p {{
        color: #CBD5E1 !important;
        font-size: 1.25rem !important;
        margin-bottom: 0;
    }}

    /* SECTION CARDS */
    .section-box {{
        background: {card_bg};
        padding: 24px 28px;
        border-radius: 12px;
        border: 1px solid {card_border};
        margin-bottom: 12px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
    }}

    .section-box h3 {{
        margin-top: 0;
        font-size: 1.6rem !important;
    }}

    .section-box p {{
        font-size: 1.08rem !important;
        color: {text_sub} !important;
    }}

    /* METRIC DISPLAY CARDS */
    .dashboard-card {{
        background: {card_bg};
        padding: 22px;
        border-radius: 12px;
        border: 1px solid {card_border};
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}

    .dashboard-card .card-title {{
        color: {text_sub};
        font-size: 1.0rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 8px;
    }}

    .dashboard-card .value {{
        color: {text_main};
        font-size: 2.2rem;
        font-weight: 800;
    }}

    .card-blue {{ border-left: 6px solid #1E3A5F; }}
    .card-green {{ border-left: 6px solid #2D6A4F; }}
    .card-yellow {{ border-left: 6px solid #D97706; }}
    .card-coral {{ border-left: 6px solid #DC2626; }}

    /* STATUS BADGES */
    .status-low {{
        background-color: #E8F5E9;
        color: #2D6A4F;
        border: 1px solid #A5D6A7;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 1.15rem;
        font-weight: 700;
        display: inline-block;
    }}

    .status-medium {{
        background-color: #FEF3C7;
        color: #B45309;
        border: 1px solid #FDE68A;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 1.15rem;
        font-weight: 700;
        display: inline-block;
    }}

    .status-high {{
        background-color: #FEE2E2;
        color: #991B1B;
        border: 1px solid #FECACA;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 1.15rem;
        font-weight: 700;
        display: inline-block;
    }}

    /* FORM INPUTS & LABELS */
    label, [data-testid="stWidgetLabel"] p {{
        color: {text_main} !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }}

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    input, textarea {{
        background-color: {input_bg} !important;
        color: {input_text} !important;
        border-radius: 8px !important;
        border: 1.5px solid {card_border} !important;
        font-size: 1.1rem !important;
    }}

    /* BUTTONS */
    .stButton > button, div.stFormSubmitButton > button {{
        border-radius: 8px !important;
        border: 1px solid #1E3A5F !important;
        background: #1E3A5F !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 1.15rem !important;
        padding: 12px 24px !important;
        transition: all 0.2s ease !important;
        width: 100%;
        box-shadow: 0 4px 10px rgba(30, 58, 95, 0.25);
    }}

    .stButton > button:hover, div.stFormSubmitButton > button:hover {{
        background: #0F172A !important;
        border-color: #0F172A !important;
    }}

    /* TABS */
    .stTabs [data-baseweb="tab"] {{
        background-color: {card_bg} !important;
        border: 1px solid {card_border} !important;
        border-radius: 8px 8px 0 0 !important;
        padding: 12px 24px !important;
        color: {text_main} !important;
        font-weight: 600 !important;
        font-size: 1.15rem !important;
    }}

    .stTabs [aria-selected="true"] {{
        border-bottom: 4px solid #1E3A5F !important;
        color: #1E3A5F !important;
    }}

    #MainMenu, footer, header {{
        visibility: hidden;
    }}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def calculate_demo_stress(data):
    score = 0
    score += {"Low": 0, "Medium": 2, "High": 4}.get(data["Work_Pressure_Level"], 0)
    score += {"Low": 4, "Medium": 2, "High": 0}.get(data["Work_Life_Balance"], 0)
    score += {"Low": 3, "Medium": 1, "High": 0}.get(data["Family_Support_Level"], 0)
    score += {"Low": 3, "Medium": 1, "High": 0}.get(data["Job_Satisfaction"], 0)

    if data["Working_Hours_per_Week"] > 60: score += 3
    elif data["Working_Hours_per_Week"] > 50: score += 2

    if data["Sleep_Hours"] < 5: score += 4
    elif data["Sleep_Hours"] < 7: score += 2

    if data["Consecutive_Duty_Days"] > 10: score += 3
    elif data["Consecutive_Duty_Days"] > 7: score += 2

    if data["Workload_Trend"] >= 2: score += 3

    if score <= 8: return "Low"
    elif score <= 17: return "Medium"
    else: return "High"


def display_stress_badge(stress_level):
    css_class = "status-low" if stress_level == "Low" else "status-medium" if stress_level == "Medium" else "status-high"
    st.markdown(f'<span class="{css_class}">{stress_level} Stress Risk</span>', unsafe_allow_html=True)


def display_metric_card(title, value, description, card_class):
    st.markdown(
        f"""
        <div class="dashboard-card {card_class}">
            <div>
                <div class="card-title">{title}</div>
                <div class="value">{value}</div>
            </div>
            <div style="color: #94a3b8; font-size: 1.0rem; margin-top: 8px;">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def display_officer_records_table(records, empty_message="No records logged yet."):
    """Shared renderer for supervisor views: summary table + expandable full Q&A per record."""
    if not records:
        st.info(empty_message)
        return

    summary_rows = [
        {
            "Date": r.get("Date", "N/A"),
            "Officer": r.get("Officer", "Unknown"),
            "Stress_Level": r.get("Stress_Level", "N/A"),
        }
        for r in records
    ]
    st.dataframe(pd.DataFrame(summary_rows), use_container_width=True, hide_index=True)

    st.markdown("### 🔍 Detailed Responses")
    for r in reversed(records):
        header = f"{r.get('Date', 'N/A')}  •  {r.get('Officer', 'Unknown')}  •  {r.get('Stress_Level', 'N/A')} Stress"
        with st.expander(header):
            st.markdown(f"**Officer:** {r.get('Officer', 'Unknown')}")
            st.markdown(f"**Date:** {r.get('Date', 'N/A')}")
            st.markdown(f"**Stress Result:** {r.get('Stress_Level', 'N/A')}")
            answers = r.get("Answers", {})
            if answers:
                st.markdown("---")
                st.markdown("**Full Assessment Q&A**")
                for question, answer in answers.items():
                    st.write(f"- **{question}:** {answer}")


# =========================================================
# LOGIN PAGE
# =========================================================

def login_page():
    st.markdown("""
    <div class="welcome-banner">
        <h1>🛡️ Personnel Welfare Monitoring System</h1>
        <p>An AI-driven proactive welfare platform for stress assessment, workload balancing, and psychological support for uniformed forces.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 1], gap="medium")

    with col1:
        st.markdown("""
        <div class="section-box">
            <h3 style="margin-bottom: 14px;">🌿 Force Well-being & Operational Security</h3>
            <p style="margin-bottom: 18px;">
                Designed specifically for Central Armed Police Forces (CAPFs) and Armed Forces personnel.
                This platform identifies operational stress early while strictly protecting officer confidentiality.
            </p>
            <p>🔒 <b>Role-Gated Access:</b> Redacted PII for authorized personnel</p>
            <p>📊 <b>Predictive Analytics:</b> Duty history & workload risk modeling</p>
            <p>📝 <b>Confidential Reflection:</b> Private mood & journal tracking</p>
            <p>🌱 <b>On-Demand Recovery:</b> Built-in respiration & grounding tools</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown("### 🔑 Authentication")
            st.markdown("<p class='sub-text'>Sign in with authorized service credentials.</p>", unsafe_allow_html=True)

            role = st.selectbox("Select Access Role", ["Officer", "Supervisor"])
            username = st.text_input("Username", placeholder="Service ID / Username")
            password = st.text_input("Password", type="password", placeholder="Password")

            if st.button("Sign In", use_container_width=True):
                if role == "Supervisor" and username == "Anya" and password == "anya123":
                    st.session_state.logged_in = True
                    st.session_state.role = "Supervisor"
                    st.session_state.username = username
                    st.rerun()
                elif role == "Officer" and username == "Officer01" and password == "officer123":
                    st.session_state.logged_in = True
                    st.session_state.role = "Officer"
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid service credentials.")

            st.caption("Demo accounts: Officer01 / officer123 or Anya / anya123")


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

def sidebar_navigation():
    with st.sidebar:
        st.markdown("### 🛡️ Welfare Portal")
        st.caption("Central Armed Police Forces")
        st.divider()

        st.markdown(f"**User:** {st.session_state.username}  \n**Role:** {st.session_state.role}")

        st.session_state.theme_mode = st.selectbox(
            "🎨 Theme Mode",
            ["Dark Mode", "Light Mode"],
            index=0 if st.session_state.theme_mode == "Dark Mode" else 1
        )

        st.divider()

        if st.session_state.role == "Officer":
            page = st.radio("Navigation", ["🏠 Dashboard", "📊 Stress Assessment", "📝 Daily Journal", "🌿 Stress Relief Centre", "🚨 Emergency Support"])
        else:
            page = st.radio("Navigation", ["🏠 Dashboard", "📋 All Officer Records", "⚠️ High-Risk Alerts", "👤 Officer Search"])

        st.divider()

        if st.button("Log out", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.role = None
            st.session_state.username = None
            st.rerun()

    return page


# =========================================================
# OFFICER DASHBOARD
# =========================================================

def officer_dashboard():
    records = st.session_state.officer_records
    latest_stress = records[-1]["Stress_Level"] if records else "N/A"
    latest_date = records[-1]["Date"] if records else "No records"

    st.markdown(f"""
    <div class="welcome-banner">
        <h1>Welcome back, {st.session_state.username} 👋</h1>
        <p>Track duty workload trends, log daily self-assessments, and access preventative welfare tools.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📊 Welfare Overview")

    col1, col2, col3, col4 = st.columns(4)
    with col1: display_metric_card("Check-ins", len(records), "Logged evaluations", "card-blue")
    with col2: display_metric_card("Current Risk", latest_stress, "Latest result", "card-green")
    with col3: display_metric_card("Last Assessment", latest_date, "Most recent date", "card-yellow")
    with col4: display_metric_card("Status", "Optimal" if latest_stress=="Low" else "Action Needed" if latest_stress=="High" else "Moderate", "System analysis", "card-coral")

    st.markdown("## Explore Your Wellbeing Tools")
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown("<div class='section-box'><h3>📊 Stress Assessment</h3><p>Record your workload, sleep, duty hours, and recovery factors to understand your stress level.</p></div>", unsafe_allow_html=True)
    with t2:
        st.markdown("<div class='section-box'><h3>📝 Daily Journal</h3><p>Reflect on your mood, log notes confidentially, and track thoughts affecting your wellbeing.</p></div>", unsafe_allow_html=True)
    with t3:
        st.markdown("<div class='section-box'><h3>🌿 Stress Relief Centre</h3><p>Try breathing exercises, grounding activities, and simple relaxation techniques.</p></div>", unsafe_allow_html=True)


# =========================================================
# STRESS ASSESSMENT FORM
# =========================================================

def stress_assessment():
    st.markdown("""
    <div class="welcome-banner">
        <h1>📊 Stress Assessment Form</h1>
        <p>Provide duty, shift, and wellness metrics. Results are processed for proactive welfare support.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("stress_assessment_form"):
        st.markdown("## 👤 Service & Demographics")
        c1, c2, c3 = st.columns(3)
        with c1: age = st.number_input("Age", min_value=18, max_value=70, value=25)
        with c2: experience = st.number_input("Service Experience (Years)", min_value=0, max_value=50, value=2)
        with c3: working_hours = st.number_input("Working Hours per Week", min_value=0, max_value=120, value=45)

        st.markdown("## 😴 Health & Rest Indicators")
        c1, c2, c3 = st.columns(3)
        with c1: sleep_hours = st.number_input("Sleep Hours per Day", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
        with c2: physical_activity = st.number_input("Physical Activity (Hours/Week)", min_value=0.0, max_value=50.0, value=3.0, step=0.5)
        with c3: recovery_days = st.number_input("Rest/Recovery Days (Past Month)", min_value=0, max_value=100, value=5)

        st.markdown("## 💼 Environment & Support Metrics")
        c1, c2, c3 = st.columns(3)
        with c1: work_pressure = st.selectbox("Perceived Duty Pressure", ["Low", "Medium", "High"])
        with c2: work_life_balance = st.selectbox("Work-Life Balance Rating", ["Low", "Medium", "High"])
        with c3: job_satisfaction = st.selectbox("Role Satisfaction", ["Low", "Medium", "High"])

        c1, c2 = st.columns(2)
        with c1: family_support = st.selectbox("Family Support System", ["Low", "Medium", "High"])
        with c2: training_opportunities = st.number_input("Skill/Training Programs Attended", min_value=0, max_value=50, value=2)

        st.markdown("## 🚨 Operational & Deployment Load")
        c1, c2, c3 = st.columns(3)
        with c1: annual_leaves = st.number_input("Annual Leaves Utilized", min_value=0, max_value=100, value=10)
        with c2: deployment_days = st.number_input("Field Deployment Days (Past Year)", min_value=0, max_value=365, value=60)
        with c3: night_shifts = st.number_input("Night Shifts (Past Month)", min_value=0, max_value=100, value=5)

        c1, c2, c3 = st.columns(3)
        with c1: consecutive_duty = st.number_input("Consecutive Duty Days", min_value=0, max_value=100, value=5)
        with c2: days_since_leave = st.number_input("Days Since Last Sanctioned Leave", min_value=0, max_value=365, value=20)
        with c3: transfer_count = st.number_input("Transfers in Last 3 Years", min_value=0, max_value=50, value=1)

        st.markdown("## 📈 Workload Trajectory")
        c1, c2 = st.columns(2)
        with c1:
            workload_trend = st.selectbox(
                "Recent Workload Trend",
                options=[-2, -1, 0, 1, 2],
                format_func=lambda x: {
                    -2: "-2 (Decreasing Significantly)",
                    -1: "-1 (Decreasing Slightly)",
                    0: "0 (Stable)",
                    1: "1 (Increasing Slightly)",
                    2: "2 (Increasing Significantly)"
                }[x]
            )
        with c2:
            duty_hours_avg = st.number_input("Average Shift Length (Hours/Day)", min_value=0.0, max_value=24.0, value=8.0, step=0.5)

        submitted = st.form_submit_button("Submit & Calculate Stress Level")

        if submitted:
            data = {
                "Work_Pressure_Level": work_pressure, "Work_Life_Balance": work_life_balance,
                "Family_Support_Level": family_support, "Job_Satisfaction": job_satisfaction,
                "Working_Hours_per_Week": working_hours, "Sleep_Hours": sleep_hours,
                "Consecutive_Duty_Days": consecutive_duty, "Workload_Trend": workload_trend
            }
            stress_level = calculate_demo_stress(data)

            # Full Q&A captured so supervisors can review exactly what was submitted
            full_answers = {
                "Age": age,
                "Service Experience (Years)": experience,
                "Working Hours per Week": working_hours,
                "Sleep Hours per Day": sleep_hours,
                "Physical Activity (Hours/Week)": physical_activity,
                "Rest/Recovery Days (Past Month)": recovery_days,
                "Perceived Duty Pressure": work_pressure,
                "Work-Life Balance Rating": work_life_balance,
                "Role Satisfaction": job_satisfaction,
                "Family Support System": family_support,
                "Skill/Training Programs Attended": training_opportunities,
                "Annual Leaves Utilized": annual_leaves,
                "Field Deployment Days (Past Year)": deployment_days,
                "Night Shifts (Past Month)": night_shifts,
                "Consecutive Duty Days": consecutive_duty,
                "Days Since Last Sanctioned Leave": days_since_leave,
                "Transfers in Last 3 Years": transfer_count,
                "Recent Workload Trend": workload_trend,
                "Average Shift Length (Hours/Day)": duty_hours_avg,
            }

            record = {
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Officer": st.session_state.username,
                "Stress_Level": stress_level,
                "Answers": full_answers,
            }
            st.session_state.officer_records.append(record)

            st.success("Assessment logged successfully.")
            st.markdown("### Estimated Stress Risk")
            display_stress_badge(stress_level)


# =========================================================
# DAILY JOURNAL
# =========================================================

def daily_journal():
    st.markdown("""
    <div class="welcome-banner">
        <h1>📝 Daily Reflection Journal</h1>
        <p>A private space for personnel to log personal observations and mental well-being notes.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("journal_form"):
        c1, c2 = st.columns([1, 2])
        with c1:
            mood = st.selectbox("How are you feeling today?", ["😫 Extremely Stressed", "😟 Stressed", "😐 Tired", "😌 Relieved", "🙂 Calm", "💪 Motivated"])
            mood_rating = st.slider("Mood Rating (1-10)", 1, 10, 5)
        with c2:
            journal_text = st.text_area("Write about your day", placeholder="Type thoughts or notes...", height=140)

        submitted = st.form_submit_button("Save Entry")
        if submitted and journal_text.strip():
            st.session_state.journal_entries.append({"Date": datetime.now().strftime("%Y-%m-%d %H:%M"), "Mood": mood, "Rating": mood_rating, "Text": journal_text})
            st.success("Journal entry saved.")

    if st.session_state.journal_entries:
        st.markdown("## Previous Logs")
        for entry in reversed(st.session_state.journal_entries):
            with st.expander(f"{entry['Date']}  •  {entry['Mood']} ({entry['Rating']}/10)"):
                st.write(entry["Text"])


# =========================================================
# STRESS RELIEF CENTRE
# =========================================================

def stress_relief_centre():
    st.markdown("""
    <div class="welcome-banner">
        <h1>🌿 Stress Relief Centre</h1>
        <p>Guided exercises and relaxation routines designed for fast operational reset.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🖐️ 5-4-3-2-1 Grounding", "🌬️ Guided Breathing", "🌱 Relaxation Tips"])

    with tab1:
        st.markdown("<div class='section-box'><h3>5-4-3-2-1 Grounding Exercise</h3><p>Focus your mind on immediate surroundings during overwhelming moments.</p></div>", unsafe_allow_html=True)

        with st.form("grounding_form"):
            c1, c2 = st.columns(2, gap="large")

            with c1:
                st.markdown("### 👀 5 Things You See")
                see1 = st.text_input("See 1", placeholder="Visible object 1...")
                see2 = st.text_input("See 2", placeholder="Visible object 2...")
                see3 = st.text_input("See 3", placeholder="Visible object 3...")
                see4 = st.text_input("See 4", placeholder="Visible object 4...")
                see5 = st.text_input("See 5", placeholder="Visible object 5...")

                st.markdown("### 👂 3 Things You Hear")
                hear1 = st.text_input("Sound 1", placeholder="Fan hum, traffic...")
                hear2 = st.text_input("Sound 2", placeholder="Footsteps, wind...")
                hear3 = st.text_input("Sound 3", placeholder="Voices, distant clock...")

                st.markdown("### 👅 1 Thing You Taste")
                taste1 = st.text_input("Taste 1", placeholder="Water, mint, coffee...")

            with c2:
                st.markdown("### ✋ 4 Things You Feel")
                feel1 = st.text_input("Sensation 1", placeholder="Ground under feet...")
                feel2 = st.text_input("Sensation 2", placeholder="Fabric on arms...")
                feel3 = st.text_input("Sensation 3", placeholder="Desk temperature...")
                feel4 = st.text_input("Sensation 4", placeholder="Airflow on skin...")

                st.markdown("### 👃 2 Things You Smell")
                smell1 = st.text_input("Smell 1", placeholder="Fresh air, tea...")
                smell2 = st.text_input("Smell 2", placeholder="Paper, soap...")

            grounding_submitted = st.form_submit_button("Submit Grounding Exercise")

        if grounding_submitted:
            st.success("✅ Grounding exercise completed. Well done — take a moment before returning to duty.")

    with tab2:
        st.markdown("<div class='section-box'><h3>Paced Respiration Protocol</h3><p><b>Routine:</b> Inhale 8s ➔ Hold 4s ➔ Release 8s. Repeat 3 times.</p></div>", unsafe_allow_html=True)
        if st.button("Start Breathing Exercise"):
            progress = st.progress(0)
            message = st.empty()
            for cycle in range(3):
                message.markdown(f"### Cycle {cycle + 1} of 3")
                for s in range(8, 0, -1):
                    message.info(f"🌬️ **Breathe IN slowly...** ({s}s remaining)")
                    time.sleep(1)
                for s in range(4, 0, -1):
                    message.warning(f"⏸️ **HOLD gently...** ({s}s remaining)")
                    time.sleep(1)
                for s in range(8, 0, -1):
                    message.success(f"🍃 **RELEASE slowly...** ({s}s remaining)")
                    time.sleep(1)
            progress.progress(1.0)
            message.success("✅ Breathing cycle completed.")

    with tab3:
        st.markdown("<div class='section-box'><h3>Quick Relaxation Tips</h3></div>", unsafe_allow_html=True)
        st.markdown("- 🚶 **Short Walk:** Take a 5-minute pacing walk to shift mental focus.")
        st.markdown("- 💧 **Hydration:** Drink a full glass of clean water.")
        st.markdown("- 🧘 **Shoulder Stretch:** Roll shoulders backward and release jaw tension.")
        st.markdown("- 🤝 **Peer Support:** Talk openly to a trusted peer officer.")


# =========================================================
# EMERGENCY SUPPORT
# =========================================================

def emergency_support():
    st.markdown("""
    <div class="welcome-banner">
        <h1>🚨 Emergency & Psychological Support</h1>
        <p>Direct helpline access and urgent intervention contacts for service personnel.</p>
    </div>
    """, unsafe_allow_html=True)

    st.error("If you or someone else is in immediate danger, contact emergency services immediately.")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("<div class='section-box'><h3>🚑 Emergency Response</h3><p>Immediate response for critical medical or safety situations.</p></div>", unsafe_allow_html=True)
        st.markdown("### Emergency Helpline: 112")
        st.link_button("Call Emergency Services", "tel:112", use_container_width=True)

    with c2:
        st.markdown("<div class='section-box'><h3>☎️ Tele-MANAS Hotline</h3><p>24/7 confidential psychological support by Govt of India.</p></div>", unsafe_allow_html=True)
        st.markdown("### Toll-Free: 14416")
        st.link_button("Call Tele-MANAS Hotline", "tel:14416", use_container_width=True)

    with c3:
        st.markdown("<div class='section-box'><h3>👤 Personal Emergency Contact</h3><p>Quick access contact saved for high-stress situations.</p></div>", unsafe_allow_html=True)

        name_input = st.text_input("Contact Name / Relation", value=st.session_state.emergency_contact_name, placeholder="e.g. Spouse, Brother, Unit Buddy")
        phone_input = st.text_input("Phone Number", value=st.session_state.emergency_contact_phone, placeholder="e.g. +91 9876543210")

        if st.button("Save Personal Contact"):
            st.session_state.emergency_contact_name = name_input
            st.session_state.emergency_contact_phone = phone_input
            st.success("Personal emergency contact saved.")

        if st.session_state.emergency_contact_phone:
            st.markdown(f"**Saved:** {st.session_state.emergency_contact_name}")
            st.link_button(f"Call {st.session_state.emergency_contact_name}", f"tel:{st.session_state.emergency_contact_phone}", use_container_width=True)


# =========================================================
# SUPERVISOR VIEWS
# =========================================================

def supervisor_dashboard():
    records = st.session_state.officer_records
    st.markdown("""
    <div class="welcome-banner">
        <h1>📊 Supervisor Dashboard & Command Analytics</h1>
        <p>Monitor force-wide welfare indicators and identify personnel needing support.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1: display_metric_card("Total Assessments", len(records), "Logged checks", "card-blue")
    with c2: display_metric_card("Low Stress", sum(1 for r in records if r["Stress_Level"] == "Low"), "Optimal readiness", "card-green")
    with c3: display_metric_card("Medium Stress", sum(1 for r in records if r["Stress_Level"] == "Medium"), "Requires monitoring", "card-yellow")
    with c4: display_metric_card("High Stress Risk", sum(1 for r in records if r["Stress_Level"] == "High"), "Requires support", "card-coral")


def all_officer_records():
    st.markdown("<h1>📋 All Officer Records</h1>", unsafe_allow_html=True)
    display_officer_records_table(st.session_state.officer_records, "No records logged yet.")


def high_risk_officers():
    st.markdown("<h1>⚠️ High-Risk Personnel Flags</h1>", unsafe_allow_html=True)
    highs = [r for r in st.session_state.officer_records if r["Stress_Level"] == "High"]
    display_officer_records_table(highs, "No high-stress assessments currently flagged.")


def officer_details():
    st.markdown("<h1>👤 Officer Profile Search</h1>", unsafe_allow_html=True)
    records = st.session_state.officer_records

    if not records:
        st.info("No records logged yet.")
        return

    officer_names = sorted(set(r.get("Officer", "Unknown") for r in records))
    selected_officer = st.selectbox("Select Officer", officer_names)

    filtered = [r for r in records if r.get("Officer", "Unknown") == selected_officer]
    st.markdown(f"### Records for **{selected_officer}**")
    display_officer_records_table(filtered, f"No records found for {selected_officer}.")


# =========================================================
# MAIN ROUTER
# =========================================================

if not st.session_state.logged_in:
    login_page()
else:
    selected_page = sidebar_navigation()

    if st.session_state.role == "Officer":
        if selected_page == "🏠 Dashboard": officer_dashboard()
        elif selected_page == "📊 Stress Assessment": stress_assessment()
        elif selected_page == "📝 Daily Journal": daily_journal()
        elif selected_page == "🌿 Stress Relief Centre": stress_relief_centre()
        elif selected_page == "🚨 Emergency Support": emergency_support()

    elif st.session_state.role == "Supervisor":
        if selected_page == "🏠 Dashboard": supervisor_dashboard()
        elif selected_page == "📋 All Officer Records": all_officer_records()
        elif selected_page == "⚠️ High-Risk Alerts": high_risk_officers()
        elif selected_page == "👤 Officer Search": officer_details()