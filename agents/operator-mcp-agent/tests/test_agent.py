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

"""Tests for Operator MCP Agent."""

import pytest
import asyncio
from operator_mcp_agent.agent import create_agent

@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent can be initialized and connects to MCP."""
    agent, exit_stack = await create_agent()
    assert agent is not None
    assert exit_stack is not None
    
    # Clean up
    await exit_stack.aclose()