import streamlit as st
from google import genai
from google.genai import types

# --- CONFIGURATION ---
st.set_page_config(page_title="OrthoScholar AI", page_icon="🦷")

# --- AUTHENTICATION ---
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("🚨 API Key is missing! Please add GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

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
            client = genai.Client(api_key=api_key)
            
            # *** FIX: Using the universal 'gemini-1.5-flash' model ***
            # This is the V1.0 model that works everywhere
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction="You are an expert Orthodontist. Answer concisely.",
                    temperature=0.3,
                ),
                contents=prompt
            )
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

        except Exception as e:
            st.error(f"Error: {e}")

# --- DEBUGGING TOOL (Only visible if you expand it) ---
with st.expander("👨‍💻 Debug: See My Available Models"):
    if st.button("List Available Models"):
        try:
            client = genai.Client(api_key=api_key)
            # This asks Google: "What models can I use?"
            models = client.models.list() 
            for m in models:
                st.write(f"- {m.name}")
        except Exception as e:
            st.error(f"Could not list models: {e}")
