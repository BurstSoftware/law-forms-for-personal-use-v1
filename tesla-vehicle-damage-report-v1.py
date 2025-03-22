import streamlit as st
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

def generate_pdf(data):
    # Create a buffer to hold the PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Add title
    story.append(Paragraph("Tesla Vehicle Damage Report", styles['Title']))
    story.append(Spacer(1, 12))
    
    # Add form data
    normal_style = styles['Normal']
    for key, value in data.items():
        if value:  # Only include non-empty fields
            story.append(Paragraph(f"<b>{key}:</b> {value}", normal_style))
            story.append(Spacer(1, 6))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

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
        # Compile form data into a dictionary
        form_data = {
            "Date and Time of Incident": f"{incident_date} at {incident_time}",
            "Location": location_where,
            "Street/Intersection": street_intersection,
            "Business/Specific Location": business_location,
            "Damage Description": damage_description,
            "Suspect Description": suspect_description,
            "Witnesses": witnesses,
            "Camera Footage": camera_footage,
            "Owner": printed_name,
            "Signature": signature,
            "Vehicle Model": vehicle_model,
            "VIN": vin,
            "Email": email,
            "Phone": phone,
            "Address": address,
            "Additional Notes": additional_notes
        }
        
        # Display success message and summary
        st.success("Damage report submitted successfully!")
        st.subheader("Damage Report Summary")
        for key, value in form_data.items():
            if value:
                st.write(f"**{key}:** {value}")
        
        # Generate PDF
        pdf_buffer = generate_pdf(form_data)
        
        # Provide download button
        st.download_button(
            label="Download Report as PDF",
            data=pdf_buffer,
            file_name=f"Tesla_Damage_Report_{incident_date}.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
