from __future__ import annotations

from typing import Any, Callable, List, Union

from arkintelligence.agent.ArkAgent import ArkAgent


class ArkWorkflow:
    """
    ArkWorkFlow is a class that represents a workflow in the Ark Intelligence system.
    It manages the execution of tasks and their dependencies.
    """

    def __init__(
        self,
        name: str = "Unknown",
        description: str = "No description",
        node_list: List[Union[ArkAgent, ArkWorkflow, Callable[..., Any]]] = [],
    ):
        """
        Initializes the ArkWorkFlow instance.
        """
        self.name = name
        self.description = description

        # Note that the nodes are sequential
        self.node_list = node_list

        self.print()

    def run(self, prompt: str):
        """
        Runs the workflow.
        """
        tmp_input = prompt

        pass

    def add_node(self, node):
        """
        Adds a node to the workflow.
        """
        pass

    def print(self):
        """
        Prints the workflow.
        """
        pass


ArkWorkflow(node_list=["123"])
