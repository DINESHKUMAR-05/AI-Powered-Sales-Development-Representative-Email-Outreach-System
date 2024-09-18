from crewai_tools import tool
from duckduckgo_search import DDGS

cache = {}

@tool("DuckDuckGo Search Tool with Caching")
def search_duckduckgo_cached(query: str) -> str:
    """
    Searches DuckDuckGo for the given query and returns the body of the first result.
    The result is cached if the same query is repeated.
    """
    
    if query in cache:
        return cache[query]  
    
    results = DDGS().text(query)
    
    if results:
        # Cache the result
        cache[query] = results[0]['body']
        return results[0]['body']
    else:
        return "No results found."