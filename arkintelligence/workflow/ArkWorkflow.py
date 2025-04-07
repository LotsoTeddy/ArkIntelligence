from __future__ import annotations

from typing import Any, Callable, List, Union

from arkintelligence.agent.ArkAgent import ArkAgent


class ArkWorkflow:
    """ArkWorkFlow is a class that represents a workflow in the Ark Intelligence system.

    It manages the execution of tasks and their dependencies. The current workflow supports the following agent execution patterns:

    - sequential
    - parallel
    - conditional
    """

    def __init__(
        self,
        name: str = "Unknown",
        description: str = "No description",
        nodes: List[Union[ArkAgent, ArkWorkflow, Callable[..., Any]]] = [],
    ):
        """
        Initializes the ArkWorkFlow instance.
        """
        self.name = name
        self.description = description

        self.nodes = nodes

    def run(self, prompt: str):
        """
        Runs the workflow.
        """
        tmp_input = prompt

    def add_node(self, node):
        """
        Adds a node to the workflow.
        """

    def print(self):
        """
        Prints the workflow.
        """


ArkWorkflow(node_list=["123"])
