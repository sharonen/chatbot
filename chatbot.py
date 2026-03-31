import arxiv
import json
import os
from typing import List
from dotenv import load_dotenv
import anthropic

from helpers import mapping_tool_function, tools, execute_tool
class Chatbot:
    def __init__(self):
        load_dotenv()
        self.anthropic_client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = os.getenv("ANTHROPIC_MODEL", "claude-3.5")

    def process_query(self, query: str) -> str:
        # Here you would implement the logic to determine which tool to use based on the message
        # For simplicity, let's assume the message is in the format: "tool_name: {json_args}"
        try:
            messages = [{'role': 'user', 'content': query}]
    
            response = self.anthropic_client.messages.create(max_tokens = 2024,
                                  #model = 'claude-3-7-sonnet-20250219', #deprecated model
                                  model = 'claude-sonnet-4-6', 
                                  tools = tools,
                                  messages = messages)
            process_query = True
            while process_query:
                assistant_content = []

                for content in response.content:
                    if content.type == 'text':
                        
                        print(content.text)
                        assistant_content.append(content)
                        
                        if len(response.content) == 1:
                            process_query = False
                    
                    elif content.type == 'tool_use':
                        
                        assistant_content.append(content)
                        messages.append({'role': 'assistant', 'content': assistant_content})
                        
                        tool_id = content.id
                        tool_args = content.input
                        tool_name = content.name
                        print(f"Calling tool {tool_name} with args {tool_args}")
                        
                        result = execute_tool(tool_name, tool_args)
                        messages.append({"role": "user", 
                                        "content": [
                                            {
                                                "type": "tool_result",
                                                "tool_use_id": tool_id,
                                                "content": result
                                            }
                                        ]
                                        })
                        response = self.anthropic_client.messages.create(max_tokens = 2024,
                                        #model = 'claude-3-7-sonnet-20250219', #deprecated model
                                        model = 'claude-sonnet-4-6', 
                                        tools = tools,
                                        messages = messages) 
                        
                        if len(response.content) == 1 and response.content[0].type == "text":
                            print(response.content[0].text)
                            process_query = False
        except Exception as e:
            return f"Error processing message: {str(e)}"
        
    def chat_loop(self):
        print("Type your queries or 'quit' to exit.")
        while True:
            try:
                query = input("\nQuery: ").strip()
                if query.lower() == 'quit':
                    break
        
                self.process_query(query)
                print("\n")
            except Exception as e:
                print(f"\nError: {str(e)}")