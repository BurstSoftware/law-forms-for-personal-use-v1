import streamlit as st
import datetime

def main():
    # Page configuration
    st.set_page_config(page_title="Government Agency Complaint Form", layout="wide")
    st.title("Complaint Letter to a Government Agency")
    
    # Date field with default to today
    date = st.date_input("Date:", datetime.date.today())
    
    # Consumer protection office details
    st.text_input("To:", key="to_field")
    protection_office = st.text_area("Name and address of consumer protection office:", height=100)
    
    # Company information
    st.subheader("Company Information")
    company_name = st.text_input("Company Name:")
    company_address = st.text_area("Company Address:", height=100)
    company_phone = st.text_input("Company Phone Number:")
    company_website = st.text_input("Company Website:")
    person_dealt_with = st.text_input("Name of Person You Dealt With:")
    
    # Complaint details
    st.subheader("Complaint Details")
    complaint_details = st.text_area("Describe your complaint (attach additional sheets if necessary):", height=200)
    
    # Complainant information
    st.subheader("Your Information")
    col1, col2 = st.columns(2)
    with col1:
        signature = st.text_input("Signature:")
        printed_name = st.text_input("Printed Name:")
        email = st.text_input("Email:")
        home_phone = st.text_input("Home Phone:")
    with col2:
        address = st.text_area("Your Address:", height=100)
        cell_phone = st.text_input("Cell Phone:")
    
    # CC field
    cc = st.text_area("CC:", height=100)
    
    # Submit button
    if st.button("Submit Complaint"):
        # Display success message and summary
        st.success("Complaint submitted successfully!")
        st.subheader("Complaint Summary")
        st.write(f"**Date:** {date}")
        st.write(f"**To:** {protection_office}")
        st.write(f"**Company Name:** {company_name}")
        st.write(f"**Person Dealt With:** {person_dealt_with}")
        st.write("**Complaint Details:**", complaint_details)
        st.write(f"**Your Address:** {address}")
        st.write(f"**Email:** {email}")
        st.write(f"**Home Phone:** {home_phone}")
        st.write(f"**Cell Phone:** {cell_phone}")
        if cc:
            st.write("**CC:**", cc)

if __name__ == "__main__":
    main()
