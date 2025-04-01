from arkintelligence.model import ArkModel

# ======== 1. Model usage ========
model = ArkModel(model="doubao-1.5-pro-32k-250115", enbale_context=True)
response = model.chat(prompt="Who are you?")
print(response)
