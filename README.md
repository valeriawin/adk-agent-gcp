# Multi-Agent System with Google Agent Development Kit (ADK)

This project demonstrates a multi-agent system built with ADK, featuring a root agent that coordinates specialized agents for Google Search and Shell command execution.

## Setup

1. Clone this repository
2. Create a `.env` file in the project root with the following content:
   ```
   GOOGLE_GENAI_USE_VERTEXAI="False"
   GOOGLE_API_KEY="your token from https://aistudio.google.com/apikey"
   ```
3. Install the required dependencies:
   ```bash
   pip install google-adk langchain-community
   ```

## Running the Application

Start the web interface by running:
```bash
adk web
```

## Architecture

The system consists of three agents:

- **Root Agent**: Coordinates between the search and shell agents (using Gemini 2.5 Pro)
- **Search Agent**: Specializes in Google Search operations (using Gemini 2.0 Flash)
- **Shell Agent**: Executes shell commands with safety checks (using Gemini 2.5 Pro)

## Safety Features

The shell agent includes safety mechanisms to prevent execution of potentially harmful commands.

## Requirements

- Python 3.9+
- Google ADK package
- LangChain Community package
- Google AI Studio API key

## License

MIT