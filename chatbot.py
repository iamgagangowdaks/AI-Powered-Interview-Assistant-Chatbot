from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = "AIzaSyCn7P9SoW4LkhAn4aFJlIttzu9WXkdCuzY"  # Load API key from the .env file
if not api_key:
    st.error("API key not found. Please set the GENAI_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=api_key)

# Streamlit page configuration
st.set_page_config(
    page_title="Interview Assistant",
    layout="centered",
    initial_sidebar_state="collapsed",
)
model = genai.GenerativeModel("gemini-1.5-flash") 

# Function to get response from Gemini
def get_gemini_response(question):
    try:
        # Generate text using the correct model name
        response = model.generate_content(question)
        if response:
            parts = response.candidates[0].content.parts
            text = ' '.join(part.text for part in parts)
            if not text:
                return "No response available.Try Again"
            else:
                return text
    except Exception as e:
        return f"Error: {e}"

# Main Title
st.markdown(
    """
    <div style='text-align: center;'>
        <h1>🔧 Interview Assistant</h1>
        <p>Select Interview Type</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Button options for Interview Types
col1, col2, col3 = st.columns(3)

with col1:
    tech_btn = st.button("💻 Technical Interview", use_container_width=True)
with col2:
    aptitude_btn = st.button("🧠 Aptitude Round", use_container_width=True)
with col3:
    hr_btn = st.button("👥 HR Interview", use_container_width=True)

# Placeholder for response
response_placeholder = st.empty()

# User Input
with st.form("user_input_form", clear_on_submit=False):
    user_question = st.text_input("Type your question here...")
    submit = st.form_submit_button("Send")

# Handle interview type selection
if tech_btn:
    st.session_state["selected_type"] = "Technical"
elif aptitude_btn:
    st.session_state["selected_type"] = "Aptitude"
elif hr_btn:
    st.session_state["selected_type"] = "HR"

# Display selected type
if "selected_type" in st.session_state:
    st.write(f"**Selected Interview Type:** {st.session_state['selected_type']}")

# Generate response when the form is submitted
if submit and user_question:
    if "selected_type" not in st.session_state:
        response_placeholder.error("Please select an interview type first!")
    else:
        # Get response from Gemini
        response = get_gemini_response(user_question)
        st.write(response)
