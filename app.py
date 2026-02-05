import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
st.set_page_config(page_title="OrthoScholar AI", page_icon="🦷")

# --- AUTHENTICATION ---
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("🚨 API Key is missing! Please add GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

# Configure the API
genai.configure(api_key=api_key)

# --- UI ---
st.title("🦷 OrthoScholar AI")
st.caption("Clinical Assistant | Dr. Ajay Kubavat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- BRAIN ---
if prompt := st.chat_input("Ask a clinical question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            # Use the standard google-generativeai library
            model = genai.GenerativeModel('gemini-pro',
                system_instruction="You are an expert Orthodontist. Answer concisely and provide evidence-based recommendations.")
            
            response = model.generate_content(prompt)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")

# --- DEBUGGING TOOL (Only visible if you expand it) ---
with st.expander("👨‍💻 Debug: See My Available Models"):
    if st.button("List Available Models"):
        try:
            # List all available models
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    st.write(f"- {m.name}")
        except Exception as e:
            st.error(f"Could not list models: {e}")
