import os

from arkintelligence.agent import ArkAgent
from arkintelligence.knowledgebase import ArkKnowledgeBase

my_knowledge_base = ArkKnowledgeBase(
    data=os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../assets/knowledgebase_data")
    )
)

agent = ArkAgent(
    name="Knowledge base agent",
    model="deepseek-v3-250324",
    prompt="You are a helpful assistant.",
    knowldgebase=my_knowledge_base,
)
res = agent.run("What is the capital of Bazhou?")
print(f"Response from agent:\n{res}")
