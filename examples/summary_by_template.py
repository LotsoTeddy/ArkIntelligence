from arkintelligence.agent import ArkAgent
from arkintelligence.knowledgebase import ArkKnowledgeBase
from arkintelligence.tool import ArkTool


@ArkTool
def visit_url(url: str) -> dict:
    """Visit a url, get the inside document, and return the document content.

    Args:
        url (str): The URL to visit.
""" """
    Returns:
        dict: The document content.
    """
    # import requests

    # response = requests.get(url, headers=headers)
    # if response.status_code != 200:
    #     raise ValueError(f"Failed to fetch URL: {url}")
    # content = response.text

    if url == "https://example.com":
        content = """
        Paper title: PaVM: A Parallel Virtual Machine for Smart Contract Execution and Validation
        
        Abstract: The performance bottleneck of blockchain has shifted from consensus to serial smart contract execution in transaction validation. Previous works predominantly focus on inter-contract parallel execution, but they fail to address the inherent limitations of each smart contract execution performance. In this paper, we propose PaVM, the first smart contract virtual machine that supports both inter-contract and intra-contract parallel execution to accelerate the validation process. PaVM consists of (1) key instructions for precisely recording entire runtime information at the instruction level, (2) a runtime system with a re-designed machine state and thread management to facilitate parallel execution, and (3) a read/write-operation-based receipt generation method to ensure both the correctness of operations and the consistency of blockchain data. We evaluate PaVM on the Ethereum testnet, demonstrating that it can outperform the mainstream blockchain client Geth. Our evaluation results reveal that PaVM speeds up overall validation performance by 33.4×, and enhances validation throughput by up to 46 times.
        """

    return content


kb = ArkKnowledgeBase(
    name="Summary templates",
    description="A knowledge base that stores summary template.",
    data="/root/ArkIntelligence/assets/knowledgebase_data/summary_templates/",
)

summary_agent = ArkAgent(
    name="Summary agent",
    model="doubao-1.5-pro-32k-250115",
    prompt="You are a helpful assistant that can help user to make summary.",
    tools=["visit_url"],
    knowldgebase=kb,
)

res = summary_agent.run(
    "Please summarize the scientific paper from the following URL: https://example.com."
)
print(res)
