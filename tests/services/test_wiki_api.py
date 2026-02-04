# tests/test_wiki_api.py
import pytest
from unittest.mock import Mock, patch
from project_flask_api.services.wiki import get_wiki_summary, safe_get


class TestSafeGet:
    """Test the safe_get wrapper function."""
    
    @patch('project_flask_api.services.wiki.requests.get')
    def test_safe_get_success(self, mock_get):
        """Test successful request."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        result = safe_get("https://test.com", {"param": "value"})
        
        assert result == mock_response
        mock_get.assert_called_once()
    
    @patch('project_flask_api.services.wiki.requests.get')
    def test_safe_get_timeout(self, mock_get):
        """Test timeout returns None."""
        mock_get.side_effect = TimeoutError("Connection timeout")
        
        result = safe_get("https://test.com", {})
        
        assert result is None
    
    @patch('project_flask_api.services.wiki.requests.get')
    def test_safe_get_connection_error(self, mock_get):
        """Test connection error returns None."""
        mock_get.side_effect = ConnectionError("Network error")
        
        result = safe_get("https://test.com", {})
        
        assert result is None


class TestGetWikiSummary:
    """Test Wikipedia summary fetching."""
    
    @patch('project_flask_api.services.wiki.safe_get')
    def test_get_wiki_summary_direct_hit(self, mock_safe_get):
        """Test successful direct title lookup."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "query": {
                "pages": {
                    "12345": {
                        "extract": "London is the capital of England."
                    }
                }
            }
        }
        mock_safe_get.return_value = mock_response
        
        result = get_wiki_summary("London")
        
        assert result == "London is the capital of England."
        assert mock_safe_get.called
    
    @patch('project_flask_api.services.wiki.safe_get')
    def test_get_wiki_summary_search_fallback(self, mock_safe_get):
        """Test search fallback when direct lookup fails."""
        # First call (direct lookup) returns no extract
        no_extract_response = Mock()
        no_extract_response.json.return_value = {
            "query": {"pages": {"123": {}}}
        }
        
        # Second call (search) returns results
        search_response = Mock()
        search_response.json.return_value = {
            "query": {
                "search": [
                    {"title": "Paris"}
                ]
            }
        }
        
        # Third call (extract from search result) returns summary
        extract_response = Mock()
        extract_response.json.return_value = {
            "query": {
                "pages": {
                    "456": {
                        "extract": "Paris is the capital of France."
                    }
                }
            }
        }
        
        mock_safe_get.side_effect = [
            no_extract_response,
            search_response,
            extract_response
        ]
        
        result = get_wiki_summary("Paris")
        
        assert result == "Paris is the capital of France."
        assert mock_safe_get.call_count == 3
    
    @patch('project_flask_api.services.wiki.safe_get')
    def test_get_wiki_summary_no_results(self, mock_safe_get):
        """Test when no Wikipedia article exists."""
        # First call (direct lookup) - no extract
        no_extract_response = Mock()
        no_extract_response.json.return_value = {
            "query": {"pages": {"123": {}}}
        }
        
        # Second call (search) - no results
        no_search_response = Mock()
        no_search_response.json.return_value = {
            "query": {"search": []}
        }
        
        mock_safe_get.side_effect = [
            no_extract_response,
            no_search_response
        ]
        
        result = get_wiki_summary("NonexistentCity123")
        
        assert "no wikipedia summary" in result.lower()
    
    @patch('project_flask_api.services.wiki.safe_get')
    def test_get_wiki_summary_api_error(self, mock_safe_get):
        """Test when API request fails."""
        mock_safe_get.return_value = None
        
        result = get_wiki_summary("London")
        
        assert "could not load" in result.lower()
    
    @patch('project_flask_api.services.wiki.safe_get')
    def test_get_wiki_summary_malformed_response(self, mock_safe_get):
        """Test handling of unexpected API response structure."""
        mock_response = Mock()
        mock_response.json.return_value = {"unexpected": "structure"}
        mock_safe_get.return_value = mock_response
        
        result = get_wiki_summary("TestCity")
        
        assert isinstance(result, str)
        assert len(result) > 0

    @patch('project_flask_api.services.wiki.safe.get')
    def test_get_wiki_summary_title_with_spaces(self, mock_safe_get):
        """Test handling of search results with multi-word titles."""
        first = Mock()
        first.json.return_value = {"query": {"pages": {"1":{}}}}

        search = Mock()
        search.json.return_value = {
            "query": {"search": [{"title": "New York City"}]}
        }

        extract = Mock()
        extract.json.return_value = {
            "query": {"pages": {"2": {"extract": "NYC summary"}}}
        }

        mock_safe_get.side_effect = [first, search, extract]

        result = get_wiki_summary("NYC")

        assert result == "NYC summary"

    @patch('project_flask_api.services.wiki.safe_get')
    def test_get_wiki_summary_json_error(self, mock_safe_get):
        """Test JSON decoding failure."""
        mock_response = Mock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_safe_get.return_value = mock_response

        result = get_wiki_summary("London")