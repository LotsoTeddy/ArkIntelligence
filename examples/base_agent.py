from arkintelligence.agent import ArkAgent
from arkintelligence.tool import ArkTool

# Set your API key here
# os.environ['ARK_API_KEY'] = ''


@ArkTool
def get_weather(city: str, date: str = "2025-03-19") -> dict:
    """Get city weather infomation

    Args:
        city (str): The name of the city.
        date (str, optional): The data in the format of YYYY-MM-DD. The default date is the current day.

    Returns:
        dict: the weather infomation
    """
    # Function implementation
    return {"temprature": "25"}


agent = ArkAgent(
    name="Weather reporter",
    model="deepseek-v3-250324",
    prompt="You are a helpful assistant.",
    tools=["get_weather"],
)
res = agent.run("How is the weather in Beijing city?")

print(
    res
)  # My name is Bytedance. And I'm here to assist you with a wide range of questions and information!
