import streamlit as st
import datetime

def main():
    st.title("Complaint Letter to a Government Agency")
    
    # Date field with default to today
    date = st.date_input("Date:", datetime.date.today())
    
    # Consumer protection office details
    st.text_input("To:", key="to_field")
    protection_office = st.text_area("[name and address of consumer protection office]", height=100)
    
    st.subheader("Company Information")
    company_name = st.text_input("Name:")
    company_address = st.text_area("Address:", height=100)
    company_phone = st.text_input("Phone number:")
    company_website = st.text_input("Website:")
    person_dealt_with = st.text_input("Name of person with whom I dealt:")
    
    # Complaint details
    st.subheader("Complaint Details")
    complaint_details = st.text_area("The details of my complaint are as follows (attach additional sheets if necessary):", height=200)
    
    # Complainant information
    st.subheader("Your Information")
    col1, col2 = st.columns(2)
    with col1:
        signature = st.text_input("Signature:")
        printed_name = st.text_input("Printed name:")
        email = st.text_input("Email:")
        home_phone = st.text_input("Home phone:")
    
    with col2:
        address = st.text_area("Address:", height=100)
        cell_phone = st.text_input("Cell phone:")
    
    # CC field
    cc = st.text_area("cc:", height=100)
    
    # Submit button
    if st.button("Submit Complaint"):
        # Here you would typically process the form data
        # For this example, we'll just show a success message
        st.success("Complaint submitted successfully!")
        
        # You could also display a summary of the submitted information
        st.subheader("Complaint Summary")
        st.write(f"Date: {date}")
        st.write(f"Company: {company_name}")
        st.write(f"Contact Person: {person_dealt_with}")
        st.write("Complaint Details:", complaint_details)

if __name__ == "__main__":
    st.set_page_config(page_title="Government Agency Complaint Form", layout="wide")
    main()
