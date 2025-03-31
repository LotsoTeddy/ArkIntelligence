import os

from arkintelligence.agent import ArkAgent
from arkintelligence.tool import ArkTool
from arkintelligence.knowledgebase import ArkKnowledgeBase

# Set your API key here
# os.environ['ARK_API_KEY'] = ''

my_knowledge_base = ArkKnowledgeBase(
    data=os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../assets/knowledgebase_data")
    )
)


@ArkTool
def get_subway_status(station: str) -> dict:
    """Get the status of a specific subway station.

    Args:
        station (str): The name of the subway station.

    Returns:
        dict: the station status
    """
    # Function implementation
    return {"status": "very crowded"}


# ====== 1. Demo for function calling ======
agent = ArkAgent(
    name="Weather reporter",
    model="deepseek-v3-250324",
    prompt="You are a helpful assistant.",
    tools=["get_subway_status"],
)
res = agent.run("How is the Dazhongsi subway station status?")
print(f"Response from agent: {res}")


# ====== 2. Demo for knowledge base ======
agent = ArkAgent(
    name="Knowledge base agent",
    model="deepseek-v3-250324",
    prompt="You are a helpful assistant.",
    knowldgebase=my_knowledge_base,
)
res = agent.run("Please help me to summary the SmartVM, and list its cons and pros.")
print(f"Response from agent: {res}")
