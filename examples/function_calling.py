from arkintelligence.agent import ArkAgent
from arkintelligence.tool import ArkTool


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
    name="Station status reporter",
    model="deepseek-v3-250324",
    prompt="You are a helpful assistant.",
    tools=["get_subway_status"],
)
res = agent.run("How is the Dazhongsi subway station status?")
print(f"Response from agent: {res}")
