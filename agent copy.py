from typing import Dict, Callable, Any, List
import json
from dotenv import load_dotenv
import os
import openai

load_dotenv()

class Agent():
    def __init__(self, model: str, prompt: str, tools: list = None, tool_executor: Dict[str, Callable] = None):
        self.tools = tools
        self.tool_executor = tool_executor
        self.client = openai.OpenAI(
            base_url=os.getenv("BASE_URL"),
            api_key=os.getenv("GROQ_API_KEY")
        )
        self.model = model
        self.messages = [
            {"role": "system", "content": prompt}
        ]

    def run(self, user_message: str) -> str:
        self.messages.append({
            "role": "user",
            "content": user_message
        })

        while True:
            response = self.client.chat.completions.create(
                model = self.model,
                tools=self.tools,
                messages=self.messages,
                parallel_tool_calls= True
            )

            tool_calls = response.choices[0].message.tool_calls
            if not tool_calls:
                self.messages.append(
                    {
                        "role": "assistant",
                        "content": response.choices[0].message.content
                    }
                )
                return response.choices[0].message.content
            
            self.messages.append(
                {
                    "role": "assistant",
                    "tool_calls": response.choices[0].message.tool_calls,
                }
            )
            
            for tool_call in tool_calls:
                tool_name = tool_call.function.name
                tool_args = tool_call.function.arguments
                try:
                    result = self.execute_tool(tool_name, tool_args)
                except Exception as e:
                    print(f"Tool error: {e}")
                    result = "Could not execute the tool to get information"


                self.messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })

    def execute_tool(self, tool_name: str, args: str) -> Any:
        parsed_args = json.loads(args)
        
        if tool_name not in self.tool_executor:
            return "The tool does not exist"
        
        tool_func = self.tool_executor[tool_name]
        try:
            result = tool_func(**parsed_args)
        except:
            return "There was an error in calling the tool"

        return result