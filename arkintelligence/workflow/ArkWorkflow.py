from __future__ import annotations

from typing import Any, Callable, List, Union

from arkintelligence.workflow.ArkWorkflowNode import ArkWorkflowNode


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
        nodes: List[Union[ArkWorkflowNode, ArkWorkflow, Callable[..., Any]]] = [],
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
        for node in self.nodes:
            if isinstance(node, ArkWorkflowNode):
                node.run(prompt)
            elif isinstance(node, ArkWorkflow):
                node.run(prompt)
            elif callable(node):
                node(prompt)
            else:
                raise ValueError("Invalid node type in workflow")

    def add_node(self, node: ArkWorkflowNode):
        """
        Adds a node to the workflow.
        """

    def print(self):
        """
        Prints the workflow.
        """


ArkWorkflow(node_list=["123"])
