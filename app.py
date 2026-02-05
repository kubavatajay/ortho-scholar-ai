import streamlit as st
from google import genai
from google.genai import types

# --- 1. CONFIGURATION & PERSONA ---
st.set_page_config(page_title="OrthoScholar AI", page_icon="🎓", layout="wide")

# Custom CSS to make it look clinical and clean
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main-header {
        font-family: 'Helvetica Neue', sans-serif;
        color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. AUTHENTICATION ---
# We grab the key from the "Safe" (Streamlit Secrets)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    st.error("⚠️ CRITICAL: API Key missing. Please configure Secrets on Streamlit Cloud.")
    st.stop()

# --- 3. THE UI (The Face of the App) ---
st.title("🎓 OrthoScholar AI")
st.caption("Designed by Dr. Ajay Kubavat for Residents & Orthodontists")

with st.sidebar:
    st.header("Clinical Parameters")
    st.info("This tool uses AI to synthesize orthodontic literature and biomechanical principles.")
    st.warning("For educational use only. Always verify with primary literature.")

# The Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome, Doctor. I am ready to discuss treatment planning, biomechanics, or literature. What is your query?"}
    ]

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 4. THE BRAIN (The Logic) ---
if prompt := st.chat_input("Enter clinical scenario or query..."):
    
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            client = genai.Client(api_key=api_key)
            
            # *** DR. KUBAVAT'S SYSTEM PROMPT ***
            # This instruction forces the AI to behave like a specialist.
            system_instruction = """
            You are a Senior Orthodontist and Academic Professor. 
            Audience: Orthodontic Residents and Specialists.
            Tone: Professional, Academic, Evidence-Based, Concise.
            
            Guidelines:
            1. Use proper terminology (e.g., 'Class II div 1', 'Center of Resistance').
            2. When discussing treatment, mention biomechanics.
            3. If a question is controversial (e.g., extraction vs non-extraction), present both viewpoints.
            4. Always include a disclaimer if the case sounds complex.
            """

            # We use the standard 'gemini-1.5-flash' which is the safest alias
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.3, # Low temperature = More factual/less creative
                ),
                contents=prompt
            )
            
            answer = response.text
            message_placeholder.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

        except Exception as e:
            st.error(f"System Error: {e}")
