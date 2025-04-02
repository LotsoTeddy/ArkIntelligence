from arkintelligence.agent import ArkAgent
from arkintelligence.utils.logger import logger


class ArkContext:
    """This class manages the context of the ArkAgent.

    Responsibilities:
    - Store the context messages of the ArkAgent.
    - Manage the prompts in messages
    - Manage multi-media data if possible
    """

    def __init__(self, agent: ArkAgent = None):
        self.agent = agent
        self.messages = []

    def create_context(self, sys_prompt: str = ""):
        if sys_prompt == "":
            sys_prompt = "Please try your best to response user's input."
        self.messages.append({"role": "system", "content": sys_prompt})

    def get_context(self):
        return self.messages

    def add_to_context(self, role: str, content: str, **kwargs):
        if role not in ["user", "assistant", "tool"]:
            logger.warning(
                "Role must be 'user', 'assistant' or 'tool'. Converting to 'user'."
            )
            role = "user"
        self.messages.append({"role": role, "content": content})


def handle_context(func):
    def wrapper(*args, **kwargs):
        if args[0].agent.enable_context:
            context = args[0].agent.context_mgr
            if context is None:
                context = ArkContext()
                context.create_context()
            args[0].agent.context_mgr = context
        return func(*args, **kwargs)

    return wrapper
