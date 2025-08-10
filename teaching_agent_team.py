import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
import os
from agno.tools.serpapi import SerpApiTools

# --- Fonction utilitaire ---
def get_text(resp):
    """Extrait proprement le texte d'une réponse RunResponse."""
    for attr in ("content", "text", "output", "message"):
        if hasattr(resp, attr):
            val = getattr(resp, attr)
            if val:
                return str(val)
    return str(resp)

# --- Config Streamlit ---
st.set_page_config(page_title="👨‍🏫 AI Teaching Agent Team", layout="wide")

# --- Session State ---
if 'google_api_key' not in st.session_state:
    st.session_state['google_api_key'] = ''
if 'serpapi_api_key' not in st.session_state:
    st.session_state['serpapi_api_key'] = ''
if 'topic' not in st.session_state:
    st.session_state['topic'] = ''

# --- Sidebar ---
with st.sidebar:
    st.title("API Keys Configuration")
    st.session_state['google_api_key'] = st.text_input("Enter your Google API Key", type="password").strip()
    st.session_state['serpapi_api_key'] = st.text_input("Enter your SerpAPI Key", type="password").strip()
    st.info("Note: Results will be displayed directly in the app.")

# --- Vérification des clés ---
if not st.session_state['google_api_key'] or not st.session_state['serpapi_api_key']:
    st.error("Please enter Google and SerpAPI keys in the sidebar.")
    st.stop()

# --- Config API ---
os.environ["GOOGLE_API_KEY"] = st.session_state['google_api_key']

# --- Création des Agents ---
professor_agent = Agent(
    name="Professor",
    role="Research and Knowledge Specialist",
    model=Gemini(id="gemini-2.0-flash", api_key=st.session_state['google_api_key']),
    instructions=[
        "Create a comprehensive knowledge base for the given topic.",
        "Explain the topic from first principles.",
        "Format it in a clear and concise way."
    ],
    show_tool_calls=False,
    markdown=True,
)

academic_advisor_agent = Agent(
    name="Academic Advisor",
    role="Learning Path Designer",
    model=Gemini(id="gemini-2.0-flash", api_key=st.session_state['google_api_key']),
    instructions=[
        "Break down the topic into logical subtopics.",
        "Present the roadmap in a structured format."
    ],
    show_tool_calls=False,
    markdown=True
)

research_librarian_agent = Agent(
    name="Research Librarian",
    role="Learning Resource Specialist",
    model=Gemini(id="gemini-2.0-flash", api_key=st.session_state['google_api_key']),
    tools=[SerpApiTools(api_key=st.session_state['serpapi_api_key'])],
    instructions=[
        "List high-quality learning resources for the topic.",
        "Use the SerpApi search tool to find relevant links."
    ],
    show_tool_calls=True,
    markdown=True,
)

teaching_assistant_agent = Agent(
    name="Teaching Assistant",
    role="Exercise Creator",
    model=Gemini(id="gemini-2.0-flash", api_key=st.session_state['google_api_key']),
    tools=[SerpApiTools(api_key=st.session_state['serpapi_api_key'])],
    instructions=[
        "Create practice exercises for the topic.",
        "Include example problems and solutions."
    ],
    show_tool_calls=True,
    markdown=True,
)

# --- Interface principale ---
st.title("👨‍🏫 AI Teaching Agent Team")
topic = st.text_input("Enter the topic you want to learn about:")

if st.button("Run Agents"):
    if not topic.strip():
        st.error("Please enter a topic.")
    else:
        # Spinner général
        with st.spinner("Agents are working together..."):
            prof_response = professor_agent.run(topic)
            advisor_response = academic_advisor_agent.run(topic)
            librarian_response = research_librarian_agent.run(topic)
            ta_response = teaching_assistant_agent.run(topic)

        # --- Mise en page multi-colonnes ---
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📚 Professor's Knowledge Base")
            st.markdown(get_text(prof_response))
        with col2:
            st.subheader("🗺 Academic Advisor's Roadmap")
            st.markdown(get_text(advisor_response))

        col3, col4 = st.columns(2)
        with col3:
            st.subheader("🔍 Research Librarian's Resources")
            st.markdown(get_text(librarian_response))
        with col4:
            st.subheader("✏️ Teaching Assistant's Exercises")
            st.markdown(get_text(ta_response))

# --- Option Debug ---
if st.checkbox("Afficher debug RunResponse (professor)"):
    prof_response = professor_agent.run(topic)
    st.write("Type:", type(prof_response))
    st.write("dir():", dir(prof_response))
    try:
        st.json(prof_response.__dict__)
    except Exception:
        st.write(repr(prof_response))

