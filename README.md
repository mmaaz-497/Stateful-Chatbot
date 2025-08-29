# Stateful Chatbot

A conversational AI chatbot built with [Chainlit](https://www.chainlit.io/) and [Google Generative AI](https://ai.google.dev/), supporting stateful conversations and multi-language UI.

## Features

- Stateful chat experience with session persistence
- Google Gemini LLM integration
- OAuth login (GitHub, Google)
- Multi-language UI (translations in `.chainlit/translations/`)
- File upload support
- Customizable assistant name and UI via `.chainlit/config.toml`

## Getting Started

### Prerequisites

- Python 3.13+
- [Poetry](https://python-poetry.org/) or `pip` for dependency management

### Installation

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd chatbot
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   # or, if using Poetry:
   poetry install
   ```

3. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in your API keys and OAuth credentials.
   - Example:
     ```
     GEMINI_API_KEY=your_gemini_api_key
     OAUTH_GITHUB_CLIENT_ID=your_github_client_id
     OAUTH_GITHUB_CLIENT_SECRET=your_github_client_secret
     OAUTH_GOOGLE_CLIENT_ID=your_google_client_id
     OAUTH_GOOGLE_CLIENT_SECRET=your_google_client_secret
     CHAINLIT_AUTH_SECRET=your_chainlit_auth_secret
     ```

4. **Run the app:**
   ```sh
   chainlit run main.py
   ```

   Or, if using Poetry:
   ```sh
   poetry run chainlit run main.py
   ```

5. **Access the chatbot:**
   - Open [http://localhost:8000](http://localhost:8000) in your browser.

## Project Structure

- `main.py` — Main entry point for the Chainlit app
- `.chainlit/` — Chainlit configuration, UI settings, and translations
- `.env` — Environment variables (API keys, secrets)
- `pyproject.toml` — Python project metadata and dependencies

## Customization

- **UI & Assistant:** Edit `.chainlit/config.toml` to change assistant name, theme, and features.
- **Welcome Screen:** Edit `chainlit.md` for the welcome message.
- **Translations:** Update files in `.chainlit/translations/` for multi-language support.

## License

This project is for educational/demo purposes. See [LICENSE](LICENSE)