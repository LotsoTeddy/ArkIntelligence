from arkintelligence.model import ArkModel

# ======== 1. Chat without context ========
# model = ArkModel(model="doubao-1.5-pro-32k-250115")

# response = model.chat(prompt="Who are you?")
# print(response)

# ======== 2. Chat with context ========
# model = ArkModel(
#     model="doubao-1.5-pro-32k-250115",
#     enbale_context=True,  # Make LLM remember the context
# )

# response = model.chat(prompt="Your name is ArkIntelligence.")
# print(response)

# response = model.chat(prompt="What is your name?")
# print(response)

# ======== 3. Chat with attachment (i.e., an image) ========
# IMAGE_PATH = "/root/ArkIntelligence/tutorial/assets/images/cat.png"
# model = ArkModel(
#     model="doubao-1.5-vision-pro-32k-250115",  # Use vision model here
# )

# response = model.chat(
#     prompt="Please describe this image with details.",
#     attachment=IMAGE_PATH,
# )
# print(response)

# ======== 4. Video generation ========
model = ArkModel(
    model="doubao-seaweed-241128",  # Use video generation model here
)

response = model.chat(
    prompt="Please describe this image with details.",
)
print(response)
