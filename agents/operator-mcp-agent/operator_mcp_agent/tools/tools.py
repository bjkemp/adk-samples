# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Example MCP tools for Operator agent."""

from google.adk.tools.function_tool import FunctionTool

async def echo_message(message: str) -> str:
    """Echoes back the input message with MCP prefix.
    
    Args:
        message: The message to echo back
        
    Returns:
        The echoed message with MCP prefix
    """
    return f"[MCP] {message}"

# Create ADK FunctionTool that can be exposed via MCP
echo_tool = FunctionTool(
    echo_message,
    name="echo",
    description="Echoes back the input message with an MCP prefix"
)