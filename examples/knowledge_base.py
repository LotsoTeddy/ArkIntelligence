import os

from arkintelligence.agent import ArkAgent
from arkintelligence.knowledgebase import ArkKnowledgeBase

data = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../assets/knowledgebase_data")
)

my_knowledge_base = ArkKnowledgeBase(data=data)
agent = ArkAgent(
    name="Knowledge base agent",
    model="deepseek-v3-250324",
    prompt="You are a helpful assistant.",
    knowldgebase=my_knowledge_base,
)
res = agent.run("Summary the pros and cons of SmartVM")
print(f"Response from agent:\n{res}")
