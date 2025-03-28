# Ark Intelligence

## Setup

```bash
pip install .
```

## Example

```python
import os

from arkintelligence.agent import ArkAgent

os.environ['ARK_API_KEY'] = YOUR_API_KEY


agent = ArkAgent(
    name='Test Agent',
    prompt='Your name is Bytedance, you are a powerful AI agent.',
)
res = agent.run('What is your name?')

print(res) # My name is Bytedance. And I'm here to assist you with a wide range of questions and information!
```