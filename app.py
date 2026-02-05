import streamlit as st
from google import genai
from google.genai import types

# --- CONFIGURATION ---
st.set_page_config(page_title="OrthoScholar AI", page_icon="🎓")

# --- AUTHENTICATION ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    st.error("⚠️ CRITICAL: API Key missing. Please configure Secrets.")
    st.stop()

# --- UI ---
st.title("🎓 OrthoScholar AI")
st.caption("Dr. Ajay Kubavat's Clinical Assistant")

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
            client = genai.Client(api_key=api_key)
            
            # *** THE FIX IS HERE: WE USE 'gemini-1.5-flash-001' ***
            response = client.models.generate_content(
                model="gemini-1.5-flash-001",
                config=types.GenerateContentConfig(
                    system_instruction="You are an expert Orthodontist. Answer concisely and professionally.",
                    temperature=0.3,
                ),
                contents=prompt
            )
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

        except Exception as e:
            st.error(f"Error: {e}")
