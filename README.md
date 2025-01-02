
# NewsData MCP Server

A simple MCP (Model Context Protocol) server built with [FastMCP](https://github.com/jlowin/fastmcp) that fetches news articles using the [NewsData.io API](https://newsdata.io/). This server provides tools, prompts, and resources to retrieve and format the latest news articles.
You can read the full Medium story at:

## Features

- **Fetch News Tool:** Retrieve news articles based on a keyword, language, and country.
- **Structured Output Prompt:** Generate a user-friendly list of news articles with titles and links.
- **Supported Resources:** Provide metadata such as supported languages, countries, and categories.

## Getting Started

### Prerequisites

- Python 3.10 or later
- [uv](https://docs.astral.sh/uv/) (required for deploying MCP servers)
- An API key from [NewsData.io](https://newsdata.io/). Sign up for a free account to generate your API key.

### Installation

1. **Install `uv`:**

   ```bash
   brew install uv
   ```

2. **Set up a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install FastMCP and other dependencies:**

   ```bash
   uv pip install fastmcp requests
   ```

4. **Clone or copy the project code into a file named `newsdata_mcp.py`.**

### Usage

1. **Run the MCP server:**

   ```bash
   uv run fastmcp install --with uvicorn --with requests newsdata_mcp.py
   ```

2. **Test the MCP server in development mode:**

   ```bash
   uv run fastmcp dev --with uvicorn --with requests newsdata_mcp.py
   ```

3. **Attach the MCP server to the Claude Desktop app for testing tools, prompts, and resources.**

## Tools, Prompts, and Resources

### Tools

#### `fetch_news`

Fetch news articles based on a keyword, language, and country.

**Parameters:**
- `keyword` (str): Search term for news articles.
- `language` (str): Language code (default: `en`).
- `country` (str): Country code (optional).

**Example Usage in Claude:**
> "Tell me the news related to Artificial Intelligence in the United States."

---

### Prompts

#### `fetch_news_prompt`

Formats fetched news articles into a structured list of titles and links.

**Example Usage in Claude:**
1. Attach the `fetch_news_prompt` tool from the MCP server.
2. Fill in:
   - **Keyword:** Blockchain
   - **Language:** en
   - **Country:** us
3. Submit and receive a `.json` file with the news articles.

---

### Resources

#### `newsapi://languages`
Returns a list of supported language codes.

#### `newsapi://countries`
Returns a list of supported country codes.

#### `newsapi://categories`
Returns a list of supported news categories.

**Example Usage in Claude:**
Attach any resource to receive a `.json` file with metadata.

---

## Code Overview

### Key Functions

1. **`fetch_news`:** The main tool for retrieving news articles from the NewsData.io API.
2. **`fetch_news_prompt`:** Formats the fetched articles into a readable list with titles and links.
3. **Resources:**
   - `get_supported_languages`: Supported language codes.
   - `get_supported_countries`: Supported country codes.
   - `get_news_categories`: Supported news categories.

---

## References

- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [NewsData.io API Documentation](https://newsdata.io/docs)
- [Claude Desktop Integration](https://claude.ai/download)


Enjoy building with MCP and FastMCP!
