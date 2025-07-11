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

# Calendly scheduling buttons
st.header("📅 Advisor Internal Scheduling Page")
st.write("Click the event you wish to schedule for your client:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("30 Min Meeting"):
        calendly_link = "https://calendly.com/aaronmacd/30-min-meeting-private"
        st.markdown(f"[Click here to open the 30 Min Meeting Calendly link.]({calendly_link})", unsafe_allow_html=True)

with col2:
    if st.button("60 Min Meeting"):
        calendly_link = "https://calendly.com/aaronmacd/60-min-meeting-private"
        st.markdown(f"[Click here to open the 60 Min Meeting Calendly link.]({calendly_link})", unsafe_allow_html=True)

with col3:
    if st.button("Group Renewal Meeting"):
        calendly_link = "https://calendly.com/aaronmacd/group-renewal-meeting-private"
        st.markdown(f"[Click here to open the Group Renewal Meeting Calendly link.]({calendly_link})", unsafe_allow_html=True)

