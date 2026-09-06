"""
Quick manual test script - run this AFTER starting the server (uvicorn main:app --reload)
in a separate terminal, to sanity-check every endpoint and role rule at once.

Run with: python3 test_api.py
"""
import requests

BASE = "http://localhost:8000"

def show(label, resp):
    print(f"\n{label}")
    print(f"  status: {resp.status_code}")
    print(f"  body:   {resp.json()}")

# 1. Predict a high-risk case
r = requests.post(f"{BASE}/predict", json={
    "personnel_id": "P001",
    "Age": 30,
    "Experience_Years": 8,
    "Working_Hours_per_Week": 60,
    "Sleep_Hours": 6,
    "Physical_Activity_Hours_per_Week": 3,
    "Work_Pressure_Level": "High",
    "Annual_Leaves_Taken": 5,
    "Work_Life_Balance": "Low",
    "Family_Support_Level": "Medium",
    "Job_Satisfaction": "Medium",
    "Training_Opportunities": "Yes",
    "Deployment_Days": 120,
    "Night_Shifts": 12,
    "Consecutive_Duty_Days": 14,
    "Days_Since_Last_Leave": 90,
    "Transfer_Count": 2,
    "Recovery_Days": 2,
    "Duty_Hours_Avg": 12,
    "Workload_Trend": 0.8
})
show("1. Predict (high-risk case)", r)

# 2. Self-report as personnel
r = requests.post(f"{BASE}/self-report", json={"self_report_score": 15, "notes": "feeling tired"},
                   headers={"X-Role": "personnel", "X-User-Id": "P001"})
show("2. Self-report as personnel", r)

# 3. Personnel viewing own history
r = requests.get(f"{BASE}/history/P001", headers={"X-Role": "personnel", "X-User-Id": "P001"})
show("3. Personnel viewing own history", r)

# 4. Personnel trying someone else's history - should be blocked
r = requests.get(f"{BASE}/history/P002", headers={"X-Role": "personnel", "X-User-Id": "P001"})
show("4. Personnel viewing SOMEONE ELSE's history (expect 403)", r)

# 5. Commander viewing dashboard summary (aggregated only)
r = requests.get(f"{BASE}/dashboard/summary", headers={"X-Role": "commander"})
show("5. Commander dashboard summary", r)

# 6. Commander trying individual history - should be blocked
r = requests.get(f"{BASE}/history/P001", headers={"X-Role": "commander"})
show("6. Commander viewing individual history (expect 403 - privacy rule)", r)

print("\nDone. If steps 4 and 6 both show 403, your privacy rules are working correctly.")
