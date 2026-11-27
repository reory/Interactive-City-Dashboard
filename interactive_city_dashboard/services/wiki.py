import requests

# Custom user agent so wikipedia dosen't block the request.
HEADERS = {
    "user-agent": "CityDashboard/1.0 (https://example.com)"
}

WIKI_API = "https://en.wikipedia.org/w/api.php"

ERROR_MESSAGE = "Could not load Wikipedia summary."

def safe_get(url, params):
    """Wrapper around requests.get with headers + error handling."""

    try:
        return requests.get(url, params=params, headers=HEADERS, timeout=5)
    except requests.exceptions.RequestException as e:
        print("WIKI REQUEST ERROR:", e)
        return None

def get_wiki_summary(city_name):
    """Fetch the first paragraph of a Wikipedia article with search fallback."""
    
    try:
        # Step 1 Direct title lookup.
        params = {
            "format":"json",
            "action":"query",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "redirects": 1,
            "titles": city_name
        }

        response = safe_get(WIKI_API, params)
        if not response:
            return ERROR_MESSAGE

        # Extract the summary text
        data = response.json()
        pages = data.get("query", {}).get("pages", {})
        
        for page_data in pages.values():
            extract = page_data.get("extract")
            if extract:
                return extract
            
        # Step 2 Perform a search if step 1 fails.
        search_params = {
            "format": "json",
            "action": "query",
            "list": "search",
            "srsearch": city_name
        }

        search_response = safe_get(WIKI_API, search_params)
        if not search_response:
            return ERROR_MESSAGE
        try:
            search_data = search_response.json()
        except ValueError:
            return ERROR_MESSAGE
        
        search_results = search_data.get("query", {}).get("search", [])
    
        if not search_results:
            return ERROR_MESSAGE
        
        # Take the first search results title
        best_title = search_results[0]["title"]

        # Step 3 Fetch extract for the best match.
        params["titles"] = best_title
        response = safe_get(WIKI_API, params)
        if not response:
            return ERROR_MESSAGE
        
        try:
            data = response.json()
        except ValueError:
            return ERROR_MESSAGE
        
        pages = data.get("query", {}).get("pages", {})

        for page_data in pages.values():
            extract = page_data.get("extract")
            if extract:
                return extract   
        
        return ERROR_MESSAGE
    
    except requests.exceptions.RequestException:
        return ERROR_MESSAGE
