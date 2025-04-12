from dotenv import load_dotenv
from google.adk.agents import Agent
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain_community.tools.shell.tool import ShellTool


load_dotenv()

def limited_search(query: str) -> dict:
    """Search the web for information.

    Args:
        query (str): The query for the search engine to search.

    Returns:
        dict: status and result or error msg.
    """
    # search = GoogleSearchAPIWrapper(google_cse_id=os.getenv("GOOGLE_CSE_ID"), google_api_key=os.getenv("GOOGLE_API_KEY"))
    search = DuckDuckGoSearchRun()
    return {"status": "success", "report": search.run(query)}


def limited_shell(command: str) -> str:
    """Execute shell commands on the local machine.
    Use this tool carefully and only when asked to perform local system operations."""
    shell_tool = ShellTool()

    # safety check for potentially harmful commands
    dangerous_commands = ["rm", "mkfs", "dd", ":(){", "sudo", ">", "shutdown"]
    if any(cmd in command for cmd in dangerous_commands):
        return "For safety reasons, I cannot execute potentially harmful commands like deletion, formatting, or system commands."

    return shell_tool.run(command)

root_agent = Agent(
    name="rag_agent",
    model="gemini-2.5-pro-exp-03-25",
    # model="gemini-2.0-flash",
    description=(
        "Agent to answer questions using search engine and run commands in shell."
    ),
    instruction=(
        "I can search any information and prepare an answer. I can also run commands in shell terminal."
    ),
    tools=[limited_search, limited_shell],
)
