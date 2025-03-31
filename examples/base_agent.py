from arkintelligence.agent import ArkAgent

agent = ArkAgent(
    name="Chatting assistant",
    model="deepseek-v3-250324",
    prompt="You are a helpful assistant. Your name is ByteDance.",
)
res = agent.run("Hello, what is your name?")
print(f"Response from agent: {res}")
