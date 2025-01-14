# TELEGRAM Chat Summarizer

A tool to analyze and summarize Telegram chat exports using AI.

## Prerequisites

1. Install UV package manager:
   - Follow instructions at https://github.com/astral-sh/uv
   - Recommended for better dependency management

2. Set up OpenAI API Key:
   - Create an API key at https://platform.openai.com/api-keys
   - Store your API key securely:
     ```bash
     # On Unix-like systems (Linux/MacOS)
     export OPENAI_API_KEY='your-api-key-here'
     ```
   - For permanent storage, add the export command to your `~/.bashrc`, `~/.zshrc`, or equivalent

## Usage

1. Export your Telegram chat:
   - Open Telegram Desktop
   - Select the group chat
   - Click ⋮ (three dots) > Export chat history
   - Choose JSON format
   - Save the `results.json` file

2. Project Setup:
   - Place your `results.json` in the `Data` folder
   - Run `uv sync` to install dependencies

3. Process the chat data:
   ```bash
   uv run process
   ```
   This will format the Telegram data for AI analysis, and save the filtered messages to Data/filtered_messages.json and the conversation text to Data/conversation_text.txt

4. Analyze and summarize:
   ```bash
   uv run summarize
   ```
   This will start an interactive session where you can ask questions about the chat and save the Q&A to Chats/qa_YYYYMMDD_HHMMSS.md

## Example Questions
- What are the main topics discussed?
- Who are the most active participants?
- Summarize the discussion from [specific date] 