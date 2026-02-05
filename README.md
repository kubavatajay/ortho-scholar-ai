# 🦷 OrthoScholar AI

**Clinical Decision Support Tool for Orthodontists**

OrthoScholar AI is an intelligent clinical assistant designed to help orthodontic residents and practitioners access synthesized, evidence-based answers quickly.

## ✨ Features

- 🤖 Powered by Google's Gemini AI
- 💬 Interactive chat interface
- 🎯 Expert orthodontic knowledge
- 🔒 Secure API key management
- 📱 Responsive Streamlit interface

## 🚀 Deployment on Streamlit Cloud

### Prerequisites
- Google Gemini API Key ([Get it here](https://aistudio.google.com/app/apikey))
- GitHub account

### Steps to Deploy:

1. **Fork this repository** to your GitHub account

2. **Get your Google Gemini API Key**:
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key
   - Copy the key

3. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io/)
   - Sign in with GitHub
   - Click "New app"
   - Select your forked repository
   - Set the main file path: `app.py`
   - Click "Advanced settings"
   - Add your secrets:
     ```toml
     GOOGLE_API_KEY = "your-api-key-here"
     ```
   - Click "Deploy!"

## 💻 Local Development

```bash
# Clone the repository
git clone https://github.com/kubavatajay/ortho-scholar-ai.git
cd ortho-scholar-ai

# Install dependencies
pip install -r requirements.txt

# Create .streamlit/secrets.toml file
mkdir .streamlit
echo 'GOOGLE_API_KEY = "your-api-key-here"' > .streamlit/secrets.toml

# Run the app
streamlit run app.py
```

## 📋 Project Structure

```
ortho-scholar-ai/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini Pro
- **Language**: Python 3.9+

## 👨‍⚕️ Author

**Dr. Ajay Kubavat**
- Professor & Head of Orthodontics
- Sure Align Orthodontix n Dentistry, Ahmedabad
- Narsinhbhai Patel Dental College (NPDCH), Sankalchand Patel University

## 📝 License

This project is for educational and clinical support purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⚠️ Disclaimer

This tool is designed to assist clinical decision-making and should not replace professional medical judgment. Always consult with qualified healthcare professionals for medical decisions.
