from arkintelligence.model import ArkModel

model = ArkModel(model="doubao-1.5-pro-32k-250115")

response = model.chat(prompt="Who are you?")
response
