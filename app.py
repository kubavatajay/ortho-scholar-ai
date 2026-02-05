import streamlit as st
from google import genai
from google.genai import types

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="OrthoScholar AI",
    page_icon="🦷",
    layout="centered"
)

# --- 2. AUTHENTICATION & SETUP ---
st.title("🦷 OrthoScholar AI")
st.caption("Clinical Decision Support | Dr. Ajay Kubavat")

# secure key retrieval
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("🚨 API Key is missing! Please add GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

# --- 3. CHAT HISTORY SETUP ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello. I am ready to assist with orthodontic literature, biomechanics, or treatment planning queries."}
    ]

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 4. THE AI LOGIC ---
if prompt := st.chat_input("Enter clinical scenario..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate answer
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            client = genai.Client(api_key=api_key)
            
            # SYSTEM PROMPT: Forces the AI to act like a professor
            sys_instruct = """
            You are an expert Orthodontist and Academic Professor.
            Provide evidence-based answers suitable for residents and specialists.
            Focus on biomechanics, biological limits, and cited literature where possible.
            Be concise but thorough.
            """

            # MODEL: We use 'gemini-1.5-flash' which is the current standard
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction=sys_instruct,
                    temperature=0.3, # Low creativity, high accuracy
                ),
                contents=prompt
            )
            
            answer = response.text
            message_placeholder.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

        except Exception as e:
            # Smart Error Handling
            error_msg = str(e)
            if "404" in error_msg:
                st.error("Error: Model not found. Please check the model name in code.")
            elif "429" in error_msg:
                st.warning("Traffic limit reached. Please wait 30 seconds and try again.")
            else:
                st.error(f"System Error: {error_msg}")
