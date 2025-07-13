from google.adk.agents import Agent
from .tools import create_corpus
DEFAUL_MODEL="gemini-2.0-flash"
        
root_agent = Agent(
    name="RAG_agent",
    model=DEFAUL_MODEL,
    description="You are a helpful and polite agent supporting retrieval augmented generation (RAG) related tasks."
                "When asked to create a corpus, use 'create_corpus' tool."
                "Do NOT process other requests.",
    tools=[create_corpus],
)
