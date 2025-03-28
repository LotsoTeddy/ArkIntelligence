import os

from typing import List
from typing import Optional
from arkintelligence.base.network import send_request
from arkintelligence.config.config import CHAT_COMPLETIONS_TEXT_URL

SUPPORTED_AGENT_TYPE = [
    'CHAT_TEXT',
    'CHAT_VIDEO',
    ]

class ArkAgent():
    
    def __init__(
        self,
        name: str = 'Undefined',
        type: str = 'CHAT_TEXT',
        prompt: str = 'You are an agent that can response user.',
        tools: List[str] = [],
        knowldgebase: str = None,
    ):
        self.name = name
        self.type = type
        self.prompt = prompt
        self.tools = tools
        self.knowldgebase = knowldgebase
        
    def run(self, prompt: str):
        if self.type == 'CHAT_TEXT':
            return self.chat_text(prompt)
        elif self.type == 'CHAT_VIDEO':
            return self.chat_video(prompt)
        else:
            raise ValueError(f"Unsupported agent type: {self.type}")
    
    def chat_text(self, prompt: str):
        response = send_request(
            url=CHAT_COMPLETIONS_TEXT_URL,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + os.getenv('ARK_API_KEY'),
            },
            data={
                'model': 'doubao-1.5-pro-32k-250115',
                'messages': [
                    {
                        'role': 'system',
                        'content': self.prompt
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
            }
        )
        response = response.get('choices')[0].get('message').get('content')
        if response is None:
            raise ValueError('Response is None')
        return response
    
    def chat_video(self, prompt: str):
        # Implement the logic for video chat agent
        response = f"Video response to: {prompt}"
        return response
        
    
    
    
    
