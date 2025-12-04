# app/upi_ui.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import datetime
from io import BytesIO
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(layout="wide", page_title="UPI Fraud Detector UI")

def color_severity(val):
    if pd.isna(val): return ''
    if val >= 3:
        return 'background-color: #ff4d4d'
    if val == 2:
        return 'background-color: #ffcc66'
    if val == 1:
        return 'background-color: #fff2cc'
    return ''

def convert_df_to_csv_bytes(df):
    return df.to_csv(index=False).encode('utf-8')

def send_email_gmail(recipient, subject, body):
    try:
        email_conf = st.secrets["email"]
        host = email_conf["host"]
        port = int(email_conf.get("port", 587))
        username = email_conf["username"]
        password = email_conf["password"]
        msg = MIMEMultipart()
        msg["From"] = username
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html"))
        server = smtplib.SMTP(host, port)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, recipient, msg.as_string())
        server.quit()
        return True, "Email sent"
    except Exception as e:
        return False, str(e)

st.title("UPI Fraud Detector — Dashboard")
col1, col2 = st.columns([3,1])
with col1:
    uploaded = st.file_uploader("Upload transactions CSV", type=["csv"])
with col2:
    from_cache = st.checkbox("Use sample data", value=True)

if uploaded is None and not from_cache:
    st.info("Upload a CSV or choose sample data to continue.")
    st.stop()

if uploaded:
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv("data/sample_txns.csv")
    if "severity" not in df.columns:
        df["severity"] = 0
    if "why" not in df.columns:
        df["why"] = ""

df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour

st.sidebar.header("Filters")
sev_filter = st.sidebar.multiselect("Severity", options=[0,1,2,3], default=[0,1,2,3])
vpa_search = st.sidebar.text_input("Search VPA (from/to)")
time_from = st.sidebar.date_input("From date", value=df['timestamp'].min().date())
time_to = st.sidebar.date_input("To date", value=df['timestamp'].max().date())

mask = df['severity'].isin(sev_filter) & (df['timestamp'].dt.date >= time_from) & (df['timestamp'].dt.date <= time_to)
if vpa_search:
    mask &= df['from_vpa'].str.contains(vpa_search, na=False) | df['to_vpa'].str.contains(vpa_search, na=False)
df_filtered = df[mask].copy()

total = len(df)
flagged = len(df[df['severity']>0])
high = len(df[df['severity']>=3])
c1, c2, c3 = st.columns(3)
c1.metric("Total txns", total)
c2.metric("Flagged", flagged)
c3.metric("Severity ≥3", high)

st.subheader("Summary Charts")
chart_col1, chart_col2 = st.columns(2)
with chart_col1:
    st.bar_chart(df_filtered['severity'].value_counts().sort_index())
with chart_col2:
    reasons = df_filtered['why'].str.split(';').explode().value_counts().head(10)
    st.write("Top reasons")
    st.dataframe(reasons)

st.subheader("Transactions (filtered)")
styled = df_filtered[['txn_id','timestamp','from_vpa','to_vpa','amount','severity','why']].copy()
styled['severity'] = styled['severity'].astype(int)
st.dataframe(styled.style.applymap(lambda v: color_severity(v) if isinstance(v,int) else '', subset=['severity']), height=350)

st.subheader("Actions on flagged transactions")
selected_txn = st.selectbox("Choose txn_id to view / alert", options=list(df_filtered['txn_id'].unique()))
if selected_txn:
    sel_row = df[df['txn_id'] == selected_txn].iloc[0]
    with st.expander("Transaction details"):
        st.write(sel_row.to_dict())
    st.write("Why flagged:", sel_row.get("why",""))
    if int(sel_row.get("severity",0)) >= 2:
        st.warning("This transaction is medium/high risk. You can notify the user or review it.")
    email_to = st.text_input("Send alert to (email)", value="")
    if st.button("Send Alert Email"):
        if not email_to:
            st.error("Provide recipient email")
        else:
            subject = f"ALERT: Suspicious UPI Transaction {sel_row['txn_id']}"
            body = f"""
            <p>Dear user,</p>
            <p>We detected a suspicious transaction:</p>
            <ul>
              <li>Txn ID: {sel_row['txn_id']}</li>
              <li>From: {sel_row['from_vpa']}</li>
              <li>To: {sel_row['to_vpa']}</li>
              <li>Amount: ₹{sel_row['amount']}</li>
              <li>Severity: {sel_row['severity']}</li>
              <li>Reason: {sel_row.get('why','')}</li>
            </ul>
            <p>If you did not authorize this, please contact your bank immediately.</p>
            """
            ok, msg = send_email_gmail(email_to, subject, body)
            if ok:
                st.success("Alert sent: " + msg)
            else:
                st.error("Failed to send: " + msg)

st.subheader("Download")
buf = convert_df_to_csv_bytes(df_filtered)
st.download_button("Download filtered CSV", data=buf, file_name="filtered_txns.csv", mime="text/csv")

