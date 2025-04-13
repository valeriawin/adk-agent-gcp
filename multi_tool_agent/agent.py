from google.adk.agents import Agent
from google.adk.tools import google_search, agent_tool
from langchain_community.tools.shell.tool import ShellTool


search_agent = Agent(
    model='gemini-2.0-flash-exp',
    name='search_agent',
    instruction='You are a specialist in Google Search.',
    tools=[google_search]
)

def limited_shell(command: str) -> dict:
    """Execute shell commands on the local machine.
    Use this tool carefully and only when asked to perform local system operations."""
    shell_tool = ShellTool()

    # safety check for potentially harmful commands
    dangerous_commands = ['rm', 'mkfs', 'dd', ':(){', 'sudo', '>', 'shutdown']
    if any(cmd in command for cmd in dangerous_commands):
        error_msg = 'For safety reasons, I cannot execute potentially harmful commands.'
        return {'status': 'error', 'data': error_msg}

    return {'status': 'success', 'data': shell_tool.run(command)}

shell_agent = Agent(
    model='gemini-2.5-pro-exp-03-25',
    name='shell_agent',
    instruction='You are a specialist in executing Shell commands.',
    tools=[limited_shell]
)

root_agent = Agent(
    name='my_agent',
    model='gemini-2.5-pro-exp-03-25',
    # model='gemini-2.0-flash',
    description=(
        'Agent to answer questions using search engine and run commands in shell.'
    ),
    instruction=(
        'I can search any information and prepare an answer. I can also run commands in shell terminal.'
    ),
    tools=[agent_tool.AgentTool(agent=search_agent), agent_tool.AgentTool(agent=shell_agent)],
)
