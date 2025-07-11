import streamlit as st

# Title and password protection
st.title("Advisor Internal Scheduling Page")

password = st.text_input("Enter advisor password to access scheduling links:", type="password")

if password != "Foxgrove2025":
    st.warning("Please enter the correct password to proceed.")
    st.stop()

st.success("Access granted. Scroll down to schedule your client.")

# Capture URL parameters from Salesforce
query_params = st.query_params

client_name = query_params.get("name", "Not provided")
client_email = query_params.get("email", "Not provided")
client_phone = query_params.get("phone", "Not provided")
client_sfid = query_params.get("sfid", "Not provided")

# Display captured client information
st.header("📄 Captured Client Information")
st.write(f"**Name:** {client_name}")
st.write(f"**Email:** {client_email}")
st.write(f"**Phone:** {client_phone}")
st.write(f"**Salesforce ID:** {client_sfid}")

st.markdown("---")

# Calendly scheduling buttons using HTML
st.header("📅 Advisor Internal Scheduling Page")
st.write("Click the event you wish to schedule for your client:")

# Create HTML-styled buttons
button_html = """
<style>
.button {
    display: inline-block;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    color: white;
    background-color: #0072ce;
    border: none;
    border-radius: 8px;
    text-decoration: none;
    margin: 10px;
}
.button:hover {
    background-color: #005bb5;
}
</style>

<a href="https://calendly.com/aaronmacd/30-min-meeting-private" target="_blank" class="button">📅 30 Min Meeting</a>
<a href="https://calendly.com/aaronmacd/60-min-meeting-private" target="_blank" class="button">📅 60 Min Meeting</a>
<a href="https://calendly.com/aaronmacd/group-renewal-meeting-private" target="_blank" class="button">📅 Group Renewal Meeting</a>
"""

st.markdown(button_html, unsafe_allow_html=True)
