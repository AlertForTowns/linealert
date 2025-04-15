import streamlit as st
import json
from utils import decrypt_snapshot, parse_snapshot, detect_alerts

st.set_page_config(page_title="LineAlert Dashboard", layout="wide")

st.title("🚨 LineAlert Live Dashboard")

# Section 1: Display Alerts (Primary Focus)
st.markdown("### 🛡️ System Status")

if "alerts" not in st.session_state:
    st.info("Upload a `.lasnap` file using the sidebar to view alerts.")
else:
    alerts = st.session_state["alerts"]
    if alerts:
        st.markdown("### 🚨 Active Alerts")
        for alert in alerts:
            st.error(f"🔴 {alert}")
    else:
        st.success("✅ No alerts detected. All systems are behaving as expected.")

# Section 2: Sidebar Upload (Secondary Interaction)
with st.sidebar:
    st.markdown("### 📁 Upload Snapshot")
    uploaded_file = st.file_uploader("Upload a `.lasnap` file", type=["lasnap"])

    if uploaded_file:
        try:
            decrypted_data = decrypt_snapshot(uploaded_file.read())
            snapshot = parse_snapshot(decrypted_data)
            alerts = detect_alerts(snapshot)

            st.session_state["alerts"] = alerts
            st.success("Snapshot uploaded and analyzed successfully.")
        except Exception as e:
            st.error(f"⚠️ Failed to process file: {e}")
