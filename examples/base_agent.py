from arkintelligence.agent import ArkAgent
from arkintelligence.tool import ArkTool

# Set your API key here
# os.environ['ARK_API_KEY'] = ''


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


agent = ArkAgent(
    name="Weather reporter",
    model="deepseek-v3-250324",
    prompt="You are a helpful assistant.",
    tools=["get_subway_status"],
)
res = agent.run("How is the Dazhongsi subway station status?")

print(f"Response from agent: {res}")
