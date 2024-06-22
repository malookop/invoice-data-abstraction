#command to run streamlit file
"""
syntax
streamlit run file_name.py

ex--streamlit run invoice_data_abstruction_verification.py"""


import streamlit as st
import pdfplumber
import re

def main():
    st.title("Invoice Data Extraction and Verification")

    uploaded_file = st.file_uploader("Upload Invoice File", type=["pdf", "jpg", "jpeg", "png"])

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            process_pdf_invoice(uploaded_file)
        else:
            st.image(uploaded_file)
            st.warning("Please upload a PDF file.")

def process_pdf_invoice(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    st.write("Extracted Text:")
    # st.text(text)

    # Extract email addresses
    emails = extract_emails(text)
    st.write("Extracted Emails:")
    st.write(emails)

    # Verify emails
    st.write("Email Verification Results:")
    for email in emails:
        if verify_email(email):
            st.write(f"{email}: Valid")
        else:
            st.write(f"{email}: Invalid")
            
    st.write("Processing complete!")

def extract_emails(text):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    emails = email_pattern.findall(text)
    return emails

def verify_email(email):
    # Basic email format validation using regex
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if re.match(pattern, email):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
