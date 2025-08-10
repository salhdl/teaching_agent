# teaching_agent
💡 Multi-Agent AI Teaching Assistant built with Streamlit and Agno Agents (Gemini + SerpAPI) to research, design learning paths, find resources, and generate exercises for any topic.
# 👨‍🏫 AI Teaching Agent Team

An interactive **multi-agent teaching assistant** built with [Streamlit](https://streamlit.io/) and [Agno Agents](https://pypi.org/project/agno/) using **Google Gemini** and **SerpAPI**.  
This app lets you:
- Research a topic from first principles.
- Design a structured learning roadmap.
- Find high-quality learning resources online.
- Generate practice exercises with solutions.

---

## 🚀 Features
- **Professor Agent** → Builds a detailed knowledge base on the topic.
- **Academic Advisor Agent** → Creates a logical learning roadmap.
- **Research Librarian Agent** → Finds external resources via SerpAPI.
- **Teaching Assistant Agent** → Generates exercises and example problems.

---
## 📦 Installation

```bash
git clone https://github.com/YourUser/teaching_agent.git
cd teaching_agent

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt


🔑 API Keys
You need API keys for:

Google Gemini API (Google Cloud Console)

SerpAPI (https://serpapi.com/)

Enter these keys in the app sidebar.

▶️ Usage
Run the app with:

bash
Copier le code
streamlit run teaching_agent.py
Open the browser, input your keys and a topic, then run the agents.

🛠 Tech Stack
Python

Streamlit

Agno Agents

Google Gemini API

SerpAPI
