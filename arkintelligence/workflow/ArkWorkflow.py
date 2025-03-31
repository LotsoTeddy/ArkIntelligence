from typing import List, Union

from arkintelligence.agent import ArkAgent
from arkintelligence.workflow import ArkWorkflow


class ArkWorkflow:
    """
    ArkWorkFlow is a class that represents a workflow in the Ark Intelligence system.
    It manages the execution of tasks and their dependencies.
    """

    def __init__(
        self,
        name: str = "Unknown",
        description: str = "No description",
        node_list: List[Union[ArkWorkflow, ArkAgent]] = [],
    ):
        """
        Initializes the ArkWorkFlow instance.
        """
        self.name = name
        self.description = description
        self.node_list = node_list

    def run(self):
        """
        Runs the workflow.
        """
        pass

    def add_node(self, node):
        """
        Adds a node to the workflow.
        """
        pass
