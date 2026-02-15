from typing import Dict, Callable, Any, List
import json
from dotenv import load_dotenv
from tools import *
import os
import openai
import yaml

load_dotenv()


class AgentConfig:
    def __init__(self, name: str = "", description: str = "", tools=None, model_name: str = "openai/gpt-oss-20b"):
        self.name = name
        self.description = description
        self.model = model_name
        self.__load_tool_schemas(tools)
    
    def __load_tool_schemas(self, tools):
        self.tools = []
        tool_names = tools if tools is not None else []
        for tool_name in tool_names:
            file_path = f"./schemas/{tool_name}_schema.json"
            with open(file_path, "r") as f:
                tools_schema = json.load(f)
            self.tools.append(tools_schema)
            

class Agent():

    DEFAULT_MODEL = "openai/gpt-oss-20b"

    def __init__(self, skill_file_path: str):
        self.file_path = skill_file_path
        self.client = openai.OpenAI(
            base_url=os.getenv("BASE_URL"),
            api_key=os.getenv("GROQ_API_KEY")
        )
        self.__initialize()
    
    def __initialize(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            skill_text = f.read()

        skill_parts = skill_text.split("---")
        yaml_part = skill_parts[1]
        markdown_part = skill_parts[2]

        yaml_config = yaml.safe_load(yaml_part)
        self.config = AgentConfig(**yaml_config)

        system_prompt = markdown_part.strip()
        self.messages = [
            {"role": "system", "content": system_prompt}
        ]


    def run(self, user_message: str) -> str:
        self.messages.append({
            "role": "user",
            "content": user_message
        })

        while True:
            response = self.client.chat.completions.create(
                model = self.config.model,
                tools=self.config.tools,
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
        
        if tool_name not in tool_exec:
            return "The tool does not exist"
        
        tool_func = tool_exec[tool_name]
        try:
            result = tool_func(**parsed_args)
        except:
            return "There was an error in calling the tool"

        return result