# Operator MCP Agent

A sample ADK project demonstrating an Operator agent with MCP tool capabilities.

## Overview

This project shows how to:
- Create an ADK Operator agent
- Integrate with MCP (Model Context Protocol)
- Expose custom tools via MCP

## Structure

- `operator_mcp_agent/`: Main package
  - `__init__.py`: Package definition
  - `agent.py`: Main agent implementation
  - `prompt.py`: Agent instructions
  - `tools/`: MCP tools
    - `__init__.py`: Tools package
    - `tools.py`: Example tools

## Getting Started

1. Install dependencies:
```bash
pip install google-adk
npm install -g @modelcontextprotocol/server-stdio
```

2. Run the agent:
```bash
python3 -m operator_mcp_agent.agent
```

## Example Usage

The agent comes with a sample `echo` tool that can be accessed via MCP.

## Configuration

Copy `.env.example` to `.env` and modify as needed.

## License

Apache 2.0