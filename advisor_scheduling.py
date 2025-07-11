# Advisor Internal Scheduling Streamlit App
# Converts your provided HTML buttons into a professional, cloud-deployable Streamlit interface
# capturing URL parameters for Salesforce integration.

import streamlit as st
# 🚩 Password Protection Gate
st.title("Advisor Internal Scheduling Page")

password = st.text_input("Enter advisor password to access scheduling links:", type="password")

# Replace 'YourSecretPassword' with your preferred internal password
if password != "Foxgrove2025":
    st.warning("Please enter the correct password to proceed.")
    st.stop()

st.success("Access granted. Scroll down to schedule your client.")

import urllib.parse

# --- Page Config ---
st.set_page_config(page_title="Advisor Internal Scheduling", page_icon="📅", layout="centered")

# --- Retrieve URL parameters ---
query_params = st.query_params
name = query_params.get("name", [""])[0]
email = query_params.get("email", [""])[0]
phone = query_params.get("phone", [""])[0]
sfid = query_params.get("sfid", [""])[0]

# --- Title and Instruction ---
st.title("📅 Advisor Internal Scheduling Page")
st.write("Click the event you wish to schedule for your client.")

# --- Helper to generate Calendly link with pre-filled parameters ---
def generate_calendly_link(base_url):
    params = {}
    if name:
        params["name"] = name
    if email:
        params["email"] = email
    if phone:
        params["a1"] = phone  # or use "phone" depending on your Calendly mapping
    if sfid:
        params["sfid"] = sfid
    
    if params:
        return base_url + "?" + urllib.parse.urlencode(params)
    else:
        return base_url

# --- Buttons with links ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📅 30 Min Meeting"):
        url = generate_calendly_link("https://calendly.com/aaronmacd/30-min-meeting-private")
        st.markdown(f"[Click here if not redirected]({url})")
        js = f'window.open("{url}", "_blank")'
        st.components.v1.html(f"<script>{js}</script>", height=0)

with col2:
    if st.button("📅 60 Min Meeting"):
        url = generate_calendly_link("https://calendly.com/aaronmacd/60-min-meeting-private")
        st.markdown(f"[Click here if not redirected]({url})")
        js = f'window.open("{url}", "_blank")'
        st.components.v1.html(f"<script>{js}</script>", height=0)

with col3:
    if st.button("📅 Group Renewal Meeting"):
        url = generate_calendly_link("https://calendly.com/aaronmacd/group-renewal-meeting-private")
        st.markdown(f"[Click here if not redirected]({url})")
        js = f'window.open("{url}", "_blank")'
        st.components.v1.html(f"<script>{js}</script>", height=0)

# --- Display captured client info for confirmation/logging ---
st.write("---")
st.subheader("Captured Client Information")
st.write(f"**Name:** {name if name else 'Not provided'}")
st.write(f"**Email:** {email if email else 'Not provided'}")
st.write(f"**Phone:** {phone if phone else 'Not provided'}")
st.write(f"**Salesforce ID:** {sfid if sfid else 'Not provided'}")

st.info("This internal scheduling page allows you to book same-day or standard meetings instantly while retaining public restrictions.")
