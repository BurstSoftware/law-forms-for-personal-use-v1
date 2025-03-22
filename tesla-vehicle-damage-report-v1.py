import streamlit as st
import datetime

def main():
    # Page configuration
    st.set_page_config(page_title="Tesla Vehicle Damage Report", layout="wide")
    st.title("Tesla Vehicle Damage Report Form")
    
    # Date and time of incident
    st.subheader("Incident Details")
    incident_date = st.date_input("Date of Incident:", datetime.date.today())
    incident_time = st.time_input("Time of Incident:", datetime.datetime.now().time())
    
    # Location information
    st.subheader("Location of Incident")
    location_where = st.text_area("Where were you at the time of damage (general description):", height=100)
    street_intersection = st.text_input("Street or Intersection:")
    business_location = st.text_input("Business or Specific Location (if applicable):")
    
    # Damage details
    st.subheader("Damage Details")
    damage_description = st.text_area("Describe the damage to your Tesla vehicle:", height=200)
    
    # Suspect information
    st.subheader("Suspect Information")
    suspect_description = st.text_area("Description of suspect (if known):", height=100)
    
    # Witness and evidence
    st.subheader("Witnesses and Evidence")
    witnesses = st.text_area("Any eyewitnesses? Provide names and contact info if available:", height=100)
    camera_footage = st.text_area("Any camera footage available? Describe source (e.g., Tesla Sentry Mode, security cameras):", height=100)
    
    # Owner information
    st.subheader("Tesla Owner Information")
    col1, col2 = st.columns(2)
    with col1:
        signature = st.text_input("Signature:")
        printed_name = st.text_input("Printed Name:")
        email = st.text_input("Email:")
        phone = st.text_input("Phone Number:")
    with col2:
        address = st.text_area("Your Address:", height=100)
        vehicle_model = st.text_input("Tesla Vehicle Model (e.g., Model 3, Model Y):")
        vin = st.text_input("Vehicle Identification Number (VIN):")
    
    # Additional notes
    additional_notes = st.text_area("Additional Notes or Context (e.g., suspected motive, political affiliation of suspects like Democrats/domestic terrorists):", height=150)
    
    # Submit button
    if st.button("Submit Damage Report"):
        # Display success message and summary
        st.success("Damage report submitted successfully!")
        st.subheader("Damage Report Summary")
        st.write(f"**Date and Time of Incident:** {incident_date} at {incident_time}")
        st.write(f"**Location:** {location_where}")
        st.write(f"**Street/Intersection:** {street_intersection}")
        st.write(f"**Business/Specific Location:** {business_location}")
        st.write("**Damage Description:**", damage_description)
        st.write("**Suspect Description:**", suspect_description)
        st.write("**Witnesses:**", witnesses)
        st.write("**Camera Footage:**", camera_footage)
        st.write(f"**Owner:** {printed_name}")
        st.write(f"**Vehicle Model:** {vehicle_model}")
        st.write(f"**VIN:** {vin}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Address:** {address}")
        if additional_notes:
            st.write("**Additional Notes:**", additional_notes)

if __name__ == "__main__":
    main()
