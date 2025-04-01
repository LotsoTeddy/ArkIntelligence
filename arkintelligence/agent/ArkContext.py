from arkintelligence.agent import ArkAgent


class ArkContext:
    """This class manages the context of the ArkAgent.

    Responsibilities:
    - Store the context messages of the ArkAgent.
    - Manage the prompts in messages
    - Manage multi-media data if possible
    """

    def __init__(self, agent: ArkAgent):
        self.agent = agent
        self.messages = []
