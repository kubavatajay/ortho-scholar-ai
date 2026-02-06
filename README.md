# 🦷 OrthoAI Scholar

**AI-powered academic and clinical companion for orthodontists, residents, and scholars.**

---

## 📋 Step 1: Concept and Scope Definition

### 1.1 Core Definition

OrthoAI Scholar is an AI-powered educational assistant that helps orthodontists, residents, and PhD scholars understand concepts, prepare for exams, and structure research ideas in orthodontics. It is **not a diagnostic or treatment-planning tool**.

### 1.2 Primary Users

OrthoAI Scholar is designed for three main user types:

- **Postgraduate orthodontic residents (MDS / equivalent)** – Need synthesized answers for learning and exam preparation
- **PhD scholars in orthodontics / craniofacial sciences** – Require help structuring research ideas, outlines, and literature searches
- **Orthodontic teachers and faculty** – Want quick teaching prompts, viva questions, and educational content generation

**Not intended for:**
- General patients seeking direct treatment advice
- Non-dentists looking for clinical recommendations
- Automated clinical decision support at chairside (for now)

### 1.3 Problems OrthoAI Scholar Solves

Three core use cases drive the features:

1. **Learning** – "I don't understand this concept/mechanic; explain it at my level with structure."
2. **Exam prep** – "I need viva questions, short-note prompts, and essay stems for this topic."
3. **Research support** – "I have a rough idea/title and need help structuring questions, outlines, and keywords."

### 1.4 Clear Boundaries

OrthoAI Scholar will **NOT**:
- Decide treatment plans for individual patients
- Give numeric cephalometric cut-offs as clinical orders
- Replace supervision, guidelines, or formal orthodontic education
- Provide direct patient-facing diagnostic recommendations

### 1.5 Scope Statement

> **Scope of OrthoAI Scholar**  
> OrthoAI Scholar is designed as an educational companion for orthodontists, postgraduate residents, and academic scholars. It focuses on explaining orthodontic concepts, generating exam-oriented practice questions, and offering structured guidance for research ideas and outlines. It must not be used as a stand-alone tool for patient diagnosis, treatment planning, or medical decision-making.

### 1.6 Safety and Ethical Stance

- LLM outputs can be incomplete, biased, or outdated
- All clinical statements must be cross-checked with current orthodontic literature, guidelines, and supervisor advice
- The app is explicitly labelled "for education and research guidance only"
- Aligns with current orthodontic AI research positioning LLMs as adjunct educational tools, not replacements for clinical expertise

---

## ✨ Features

- 🤖 Powered by Google's Gemini AI
- 💬 Interactive chat interface
- 🎓 Expert orthodontic knowledge
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
   - Copy and save it securely

3. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your forked repository
   - Choose `app.py` as the main file
   - Add your Gemini API key in Secrets:
     ```toml
     GOOGLE_API_KEY = "your-api-key-here"
     ```
   - Click "Deploy"

## 💻 Local Development

```bash
# Clone the repository
git clone https://github.com/kubavatajay/ortho-scholar-ai.git
cd ortho-scholar-ai

# Install dependencies
pip install -r requirements.txt

# Create .streamlit/secrets.toml and add your API key
mkdir -p .streamlit
echo 'GOOGLE_API_KEY = "your-api-key-here"' > .streamlit/secrets.toml

# Run the app
streamlit run app.py
```

## 📝 Usage

1. Open the app in your browser
2. Type your orthodontic question in the chat interface
3. Get evidence-informed answers and educational guidance
4. Use for learning, exam preparation, or research ideation

## ⚠️ Disclaimer

OrthoAI Scholar uses large language models to generate educational content. Responses may be incomplete, outdated, or inaccurate and must not be used as sole guidance for patient diagnosis or treatment planning. Always verify information against current orthodontic literature and institutional protocols, and consult a qualified specialist before clinical application.

## 👨‍⚕️ About

Created by **Dr. Ajay Kubavat**  
Sure Align Orthodontix n Dentistry, Ahmedabad  
Professor and Head, Department of Orthodontics  
Narsinhbhai Patel Dental College, Sankalchand Patel University

---

## 📄 License

This project is open-source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

**Note:** This is an educational tool and part of ongoing research into AI applications in orthodontic education. It is not intended to replace formal training, textbooks, or clinical supervision.
