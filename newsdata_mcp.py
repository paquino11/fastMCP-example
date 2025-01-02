from fastmcp import FastMCP
import requests
from fastmcp.prompts.base import UserMessage, AssistantMessage

mcp = FastMCP("NewsData MCP Server")

API_URL = "https://newsdata.io/api/1/news"
API_KEY = "pub_630641b803481b6c595cc9f1378ab23e7bd01"

@mcp.tool()
def fetch_news(keyword: str, language: str = "en", country: str = None) -> list[dict]:
    """
    Fetch the latest news articles based on a keyword, language, and country.
    
    Parameters:
        keyword (str): The search term for news.
        language (str): Language code (default: 'en').
    Returns:
        list[dict]: A list of news articles.
    """
    query_params = {
        "apikey": API_KEY,
        "q": keyword,
        "language": language,
        "country": country
    }

    response = requests.get(API_URL, params=query_params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        raise ValueError(f"Error fetching news: {response.json().get('message', 'Unknown error')}")
    
@mcp.prompt()
def fetch_news_prompt(keyword: str, language: str = "en", country: str = None) -> list:
    """
    Fetch news articles based on keyword, language, and country, and return a list of articles with links.
    
    Parameters:
        keyword (str): The search term for news.
        language (str): Language code (default: 'en').
        country (str): Country code (optional).
    
    Returns:
        list: A structured list of messages with article titles and links.
    """
    # Fetch news using the existing tool
    articles = fetch_news(keyword=keyword, language=language, country=country)
    
    # Create a structured response
    if not articles:
        return [AssistantMessage(f"No news articles found for keyword '{keyword}' in language '{language}'.")]

    messages = [UserMessage(f"News articles for keyword '{keyword}':")]
    for article in articles[:10]:  # Limit to the first 10 articles
        title = article.get("title", "No title available")
        link = article.get("link", "No link available")
        messages.append(UserMessage(f"Title: {title}\nLink: {link}"))
    
    return messages

@mcp.resource("newsapi://languages")
def get_supported_languages() -> list[str]:
    """
    Get a list of supported language codes.
    """
    return ["en", "es", "fr", "de", "it", "pt", "ar"]

@mcp.resource("newsapi://countries")
def get_supported_countries() -> list[str]:
    """
    Get a list of supported country codes.
    """
    return ["us", "gb", "ca", "au", "in", "br", "de", "fr"]

@mcp.resource("newsapi://categories")
def get_news_categories() -> list[str]:
    """
    Get a list of supported news categories.
    """
    return ["business", "entertainment", "health", "science", "sports", "technology"]