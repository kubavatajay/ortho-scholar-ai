import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
st.set_page_config(page_title="OrthoAI Scholar", page_icon="🦷")

# Display logo
try:
    st.image("orthoai-scholar-logo.png", width=600)
except:
    st.title("🦷 OrthoAI Scholar")

# --- AUTHENTICATION ---
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("🚨 API Key is missing! Please add GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

# Configure the API
genai.configure(api_key=api_key)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🦷 OrthoAI Scholar")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Ask OrthoAI Scholar", "Exam & Viva Mode", "Research Helper (Basic)"]
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "Educational tool for orthodontists, residents, and scholars.\n"
    "Not for direct clinical decision-making."
)

# --- HOME PAGE ---
if page == "Home":
    st.title("🦷 OrthoAI Scholar")
    st.subheader("AI Mentor for Orthodontists, Residents, and PhD Scholars")
    
    st.markdown("""
    **What you can do here**
    
    - Ask conceptual and clinical questions in orthodontics
    - Generate viva-style questions and exam practice prompts
    - Get help structuring research ideas, outlines, and keywords
    
    OrthoAI Scholar is an educational companion and should not replace
    textbooks, guidelines, or supervision by qualified orthodontists.
    """)
    
    st.markdown("### ⚠️ Disclaimer")
    st.info(
        "This tool uses large language models and may occasionally produce "
        "incorrect or outdated information. Always verify with current orthodontic "
        "literature and institutional protocols before applying anything clinically."
    )
    
    st.markdown("---")
    st.caption(
        "Created by **Dr. Ajay Kubavat** | "
        "Sure Align Orthodontix n Dentistry, Ahmedabad | "
        "Professor and Head, Department of Orthodontics, NPDCH | Sankalchand Patel University, Visnagar, Gujarat, India"    )

# --- ASK ORTHOAI SCHOLAR ---
elif page == "Ask OrthoAI Scholar":
    st.title("💬 Ask OrthoAI Scholar")
    
    topic = st.text_area(
        "Ask any orthodontic question (concepts, mechanics, diagnosis frameworks, etc.)",
        placeholder="e.g., Biomechanical differences between intrusion with TADs and utility arches",
        height=100
    )
    
    col1, col2 = st.columns(2)
    with col1:
        level = st.selectbox("Target level", ["Resident (MDS)", "PhD/Faculty", "Beginner"])
    with col2:
        style = st.selectbox("Answer style", ["Short explanation", "Detailed with headings", "Bullet points"])
    
    if st.button("Get Answer", type="primary"):
        if not topic.strip():
            st.warning("Please type your question first.")
        else:
            with st.spinner("Thinking like an orthodontic mentor..."):
                try:
                    # Create system instruction based on level and style
                    system_prompt = f"""You are an expert Orthodontist and academic mentor. 
                    Answer questions at the {level} level.
                    Use {style} format.
                    Focus on evidence-based, educational content.
                    Do not provide specific patient treatment recommendations.
                    Always mention that clinical decisions require professional judgment."""
                    
                    model = genai.GenerativeModel('models/gemini-2.0-flash', system_instruction=system_prompt)
                    response = model.generate_content(topic)
                    
                    st.markdown("### Answer")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Error generating response: {e}")
    
    st.caption("💡 Tip: Always cross-check answers with standard orthodontic textbooks and current literature.")

# --- EXAM & VIVA MODE ---
elif page == "Exam & Viva Mode":
    st.title("📝 Exam & Viva Mode")
    
    exam_type = st.selectbox("Mode", ["Viva questions", "Short notes prompts", "Long essay prompts"])
    
    subject_block = st.selectbox(
        "Select block",
        [
            "Growth and Development",
            "Diagnosis and Cephalometrics",
            "Fixed Appliance Therapy",
            "Functional Appliances",
            "Clear Aligners",
            "Biostatistics & Research Methodology",
            "Cleft and Craniofacial Orthodontics"
        ]
    )
    
    extra = st.text_input(
        "Optional: narrow topic",
        placeholder="e.g., ANB angle, Class II division 1, anchorage mechanics, etc."
    )
    
    n_q = st.slider("Number of questions/prompts", 5, 30, 10)
    
    if st.button("Generate Exam Prompts", type="primary"):
        with st.spinner("Creating exam-style questions..."):
            try:
                focus = f" focusing on {extra}" if extra.strip() else ""
                
                system_prompt = f"""You are an experienced orthodontic examiner creating {exam_type}.
                Generate exactly {n_q} questions from {subject_block}{focus}.
                Make questions appropriate for MDS orthodontics examination level.
                For viva questions: include both theory and clinical scenario-based questions.
                For short notes: provide concise prompts that test core concepts.
                For long essays: create comprehensive prompts requiring detailed discussion."""
                
                user_prompt = f"Generate {n_q} {exam_type} on {subject_block}{focus}."
                
                model = genai.GenerativeModel('models/gemini-2.0-flash', system_instruction=system_prompt)
                response = model.generate_content(user_prompt)
                
                st.markdown("### Your Exam Practice Questions")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Error generating questions: {e}")
    
    st.caption("⚠️ Use these for self-practice; always cross-check with your university syllabus and standard textbooks.")

# --- RESEARCH HELPER (BASIC) ---
elif page == "Research Helper (Basic)":
    st.title("🔬 Research Helper (Basic)")
    
    mode = st.selectbox(
        "What do you want help with?",
        [
            "Refining a research idea",
            "Generating RCT/observational study outline",
            "Keywords for literature search",
            "Drafting a structured abstract (template only)"
        ]
    )
    
    text = st.text_area(
        "Paste your idea/title/abstract",
        placeholder="e.g., Effect of clear aligners vs fixed appliances on oral health-related quality of life in adults",
        height=150
    )
    
    if st.button("Get Research Help", type="primary"):
        if not text.strip():
            st.warning("Please paste some text or a rough idea.")
        else:
            with st.spinner("Thinking as a research mentor..."):
                try:
                    if mode == "Refining a research idea":
                        system_prompt = """You are an orthodontic research mentor.
                        Help refine the research idea by:
                        1. Identifying the key variables
                        2. Suggesting potential research questions
                        3. Highlighting gaps this could address
                        4. Recommending appropriate study design
                        Keep suggestions practical for MDS/PhD level research."""
                    
                    elif mode == "Generating RCT/observational study outline":
                        system_prompt = """You are an orthodontic research mentor.
                        Create a structured study outline with:
                        1. Title
                        2. Aim and objectives
                        3. Study design and setting
                        4. Sample size considerations
                        5. Inclusion/exclusion criteria
                        6. Primary and secondary outcomes
                        7. Statistical analysis plan
                        Make it suitable for orthodontic research."""
                    
                    elif mode == "Keywords for literature search":
                        system_prompt = """You are an orthodontic research librarian.
                        Provide:
                        1. 10-15 relevant MeSH terms and keywords
                        2. Suggested Boolean search string
                        3. Recommended databases (PubMed, Cochrane, Scopus, etc.)
                        4. Alternative search terms"""
                    
                    else:  # Structured abstract
                        system_prompt = """You are an orthodontic research mentor.
                        Create a structured abstract template with:
                        - Background (2-3 sentences)
                        - Aim
                        - Materials and Methods
                        - Results (placeholder format)
                        - Conclusion
                        Make it suitable for orthodontic journal submission."""
                    
                    model = genai.GenerativeModel('models/gemini-2.0-flash', system_instruction=system_prompt)
                    response = model.generate_content(text)
                    
                    st.markdown("### Research Guidance")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Error generating research help: {e}")
    
    st.caption("⚠️ Outputs are for academic guidance only and must be adapted to ethical and institutional norms.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Version:** 2.0 | [GitHub](https://github.com/kubavatajay/ortho-scholar-ai) | "
    "Educational use only"
)
