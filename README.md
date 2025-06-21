# Multi-Agent Supervisor System

A LangGraph-powered multi-agent system that routes user queries to specialized agents for processing information from the Official Gazette (Resmi Gazete) and current news sources.

## 🚀 Features 

- **Multi-Agent Architecture**: Uses a supervisor agent to route queries to specialized agents
- **Official Gazette Agent**: Processes queries related to official government publications (limited to data between April 7-11)
- **Current Information Agent**: Handles queries about current news and events
- **Fallback Agent**: Provides responses when other agents cannot handle the query
- **Streamlit UI**: User-friendly interface for interacting with the system

## 🏗️ System Architecture

The system is built using LangGraph and consists of:

1. **Supervisor Agent**: Routes incoming queries to the appropriate specialized agent
2. **Specialized Agents**:
   - Official Gazette Agent: Handles queries about government publications (Note: data is limited to April 7-11 period only)
   - Current Information Agent: Processes queries about current news
   - Fallback Agent: Provides responses when other agents cannot handle the query
3. **Web UI**: Streamlit-based interface for user interaction

## 🛠️ Tech Stack

- **LangGraph**: For building the agent workflow and routing
- **LangChain**: For LLM interactions and tool usage
- **FastAPI**: Backend API service
- **Streamlit**: User interface
- **Docker**: Containerization for easy deployment
- **Multiple LLM Models**: OpenAI, Qwen, and LLaMA for different agent functions

## 📋 Prerequisites

- Docker and Docker Compose
- API keys for LLM services (OpenAI, etc.)

## 🚀 Getting Started

### Environment Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/multi-agent-supervisor.git
cd multi-agent-supervisor
```

2. Create a `.env` file with the necessary API keys
```
OPENAI_API_KEY=your_openai_api_key
# Add other API keys as needed
```

### Running with Docker

```bash
docker-compose up --build
```

The UI will be available at http://localhost:8501

### Running Locally

1. Set up a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies
```bash
pip install -r api/requirements.txt
pip install -r ui/requirements.txt
```

3. Run the application
```bash
python main.py
```

## 🧩 Project Structure

```
multi-agent-supervisor/
├── api/                    # Backend API service
│   ├── agents/             # Agent implementations
│   ├── config/             # Configuration files
│   ├── graph/              # LangGraph workflow definitions
│   ├── models/             # LLM model initializations
│   ├── services/           # External service integrations
│   ├── tools/              # Agent tools
│   ├── app.py              # FastAPI application
│   └── requirements.txt    # API dependencies
├── ui/                     # Streamlit UI
│   ├── streamlit_ui.py     # Streamlit application
│   └── requirements.txt    # UI dependencies
├── main.py                 # Main entry point for local execution
└── docker-compose.yml      # Docker Compose configuration
```

## 📝 Usage

1. Access the Streamlit UI at http://localhost:8501
2. Enter your query in the chat input
3. The system will route your query to the appropriate agent and display the response
4. Enable Debug Mode in the sidebar to see detailed processing steps
5. **Note**: Official Gazette data is limited to the period between April 7-11 only

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
