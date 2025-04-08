from typing import Any, Callable

from arkintelligence.agent.ArkAgent import ArkAgent


class ArkWorkflowNode:
    def __init__(
        self,
        name: str = "Unknown",
        description: str = "No description",
        agent: ArkAgent = None,
        callback: Callable[..., Any] = None,
    ):
        """
        Initializes the ArkWorkflowNode instance.
        """
        self.name = name
        self.description = description
        self.agent = agent
        self.callback = callback

    def run(self, prompt: str):
        """
        Runs the node.
        """
        output = ""
        return self.callback(output)
