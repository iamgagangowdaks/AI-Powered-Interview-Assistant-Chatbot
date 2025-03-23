![image](https://github.com/user-attachments/assets/dbbd857b-27a2-48e0-a0f0-45917bd5dd15)# AI-Powered-Interview-Assistant-Chatbot
"An AI-driven application built with Streamlit, leveraging the Gemini API to assist users in preparing for interviews. Supports technical, aptitude, and HR interview question generation with dynamic user input and seamless response generation."
# AI-Powered Interview Assistant with Streamlit and Gemini API  

An AI-driven application designed to help users prepare for interviews by generating intelligent responses for **Technical**, **Aptitude**, and **HR Interview** questions. Built with **Streamlit** and integrated with the **Gemini API**, this app provides dynamic, real-time assistance to enhance interview readiness.

---

## Features  
- 🎯 **Dynamic Interview Modes**:  
   - Technical Interview  
   - Aptitude Round  
   - HR Interview  

- 💬 **Intelligent Question Handling**:  
   - Submit your interview questions and receive AI-generated responses.  

- 📱 **Interactive Interface**:  
   - Simple, user-friendly interface powered by Streamlit.  

- 🔄 **Seamless API Integration**:  
   - Powered by the Gemini API for accurate and context-aware answers.  

---

## Setup and Installation  

### Prerequisites  
1. Python 3.8 or later  
2. A valid Gemini API Key  

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/ai-interview-assistant.git  
   cd ai-interview-assistant  
   ```  

2. Create and activate a virtual environment:  
   ```bash  
   python -m venv env  
   source env/bin/activate  # For Linux/macOS  
   env\Scripts\activate     # For Windows  
   ```  

3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Create a `.env` file in the project root directory and add your **Gemini API Key**:  
   ```bash  
   GENAI_API_KEY=your_gemini_api_key_here  
   ```  

5. Run the application:  
   ```bash  
   streamlit run app.py  
   ```  

6. Open your browser and navigate to:  
   ```
   http://localhost:8501  
   ```  

---

## Usage  

1. **Select an Interview Type**:  
   Choose from Technical, Aptitude, or HR Interviews using the provided buttons.  

2. **Enter Your Question**:  
   Use the input box to type your interview question and click "Send".  

3. **Receive AI Response**:  
   View the AI-generated response tailored to your chosen interview type.  

---

## Code Overview  

### Backend:  
- **`google.generativeai`**: Integrated Gemini API for generating responses.  
- **Environment Variables**: API key securely loaded using `python-dotenv`.  

### Frontend:  
- **Streamlit**: Provides an interactive, user-friendly dashboard.  
- **Dynamic Buttons**: Allow users to switch between interview types seamlessly.  

---

## Key Files  

- `app.py`: The main application file.  
- `.env`: Stores sensitive API keys.  
- `requirements.txt`: Contains Python dependencies.  

---

## Example Screenshot  
![image](https://github.com/user-attachments/assets/d9893331-aa8f-4928-8023-de6b8245f99c)

![image](https://github.com/user-attachments/assets/ce2368ff-cf66-4986-9ec8-d77b5745e3e0)


---

## Contributing  
Contributions are welcome! Please fork this repository and create a pull request for any changes or improvements.  

---
## Connect with Me 
https://www.linkedin.com/in/gagan-gowda-k-s-0712b7257?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app


## License  
This project is licensed under the [MIT License](LICENSE).  

---  

Feel free to customize the README further based on your repository's specifics! 😊  
