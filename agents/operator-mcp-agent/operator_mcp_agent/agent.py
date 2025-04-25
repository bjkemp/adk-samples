# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Operator MCP Agent implementation."""

import asyncio
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

async def get_tools_async():
    """Connects to MCP server and gets available tools."""
    print("Connecting to MCP server...")
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=StdioServerParameters(
            command='npx',
            args=["-y", "@modelcontextprotocol/server-stdio"]
        )
    )
    print(f"Connected to MCP server with {len(tools)} tools available")
    return tools, exit_stack

async def create_agent():
    """Creates the Operator MCP agent with connected tools."""
    global root_agent
    tools, exit_stack = await get_tools_async()
    
    root_agent = LlmAgent(
        model='gemini-2.0-flash',
        name='operator_mcp_agent',
        instruction='Operator agent with MCP tool capabilities',
        tools=tools
    )
    return root_agent, exit_stack

# Expose root_agent as module attribute
root_agent, _ = asyncio.run(create_agent())