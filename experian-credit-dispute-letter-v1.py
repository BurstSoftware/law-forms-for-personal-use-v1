import streamlit as st
from datetime import datetime

def generate_credit_dispute_letter(first_name, last_name, street_address, city, state, zip_code, dob, ssn, account_status, case_number):
    """Generates the credit dispute letter."""
    letter = f"""
{first_name} {last_name}
{street_address}
{city}, {state} {zip_code}

Date of Birth: {dob}
SS#: {ssn}

Experian
P.O. Box 4500
Allen, TX 75013

Date: {datetime.now().strftime('%B %d, %Y')}

Re: Letter to Remove Inaccurate Credit Information

To Whom It May Concern,

I received a copy of my credit report and found the following item(s) to be in error:

1. Validate Account
Current Account Status: {account_status}
Case Number or Account Number: {case_number}
Please supply information on how you have verified this item.

By the provisions of the Fair Credit Reporting Act, I demand that these items be investigated and removed from my report. It is my understanding that you will recheck these items with the creditor who has posted them. Please remove any information that the creditor cannot verify. I understand that under 15 U.S.C. Sec. 1681i(a), you must complete this reinvestigation within 30 days of receipt of this letter.

Please send an updated copy of my credit report to the above address.

According to the act, there shall be no charge for this updated report.

I also request that you please send notices of corrections to anyone who received my credit report in the past six months.

Thank you for your time and help in this matter.

Sincerely,

_____________________________________
{first_name} {last_name}
    """
    return letter

def main():
    st.title("Credit Dispute Letter Generator")
    st.write("Fill in the information below to generate your credit dispute letter.")

    # Input fields for user data
    first_name = st.text_input("First Name:")
    last_name = st.text_input("Last Name:")
    street_address = st.text_input("Street Address:")
    city = st.text_input("City:")
    state = st.text_input("State:")
    zip_code = st.text_input("Zip Code:")
    dob = st.text_input("Date of Birth (MM/DD/YYYY):")
    ssn = st.text_input("SSN (Last 4 Digits):")

    st.write("---")

    st.write("### Disputed Item Details")
    account_status = st.text_input("Current Account Status:")
    case_number = st.text_input("Case Number or Account Number:")

    if st.button("Generate Letter"):
        if not all([first_name, last_name, street_address, city, state, zip_code, dob, ssn, account_status, case_number]):
            st.error("Please fill in all fields to generate the letter.")
        else:
            letter = generate_credit_dispute_letter(
                first_name, last_name, street_address, city, state, zip_code, dob, ssn, account_status, case_number
            )
            st.success("Letter Generated Successfully!")
            st.download_button("Download Letter", letter, file_name="credit_dispute_letter.txt", mime="text/plain")

if __name__ == "__main__":
    main()
