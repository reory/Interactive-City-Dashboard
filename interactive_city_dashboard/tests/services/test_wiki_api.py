from unittest.mock import MagicMock, patch

import requests

from interactive_city_dashboard.services import wiki


def test_safe_get_success():
    """safe_get should call requests.get with correct params and headers."""

    with patch("interactive_city_dashboard.services.wiki.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_get.return_value = mock_response

        result = wiki.safe_get("http://example.com", {"a": 1})

        mock_get.assert_called_once_with(
            "http://example.com",
            params={"a": 1},
            headers=wiki.HEADERS,
            timeout=5,
        )
        assert result is mock_response


def test_safe_get_failure():
    """safe_get should return None on exception."""

    with patch(
        "interactive_city_dashboard.services.wiki.requests.get",
        side_effect=requests.exceptions.RequestException("boom"),
    ):
        result = wiki.safe_get("http://example.com", {"a": 1})
        assert result is None


def test_get_wiki_summary_direct_hit():
    """Return extract when the initial title lookup succeeds."""

    with patch("interactive_city_dashboard.services.wiki.safe_get") as mock_safe:
        mock_response = MagicMock()

        mock_response.json.return_value = {
            "query": {
                "pages": {
                    "123": {
                        "extract": "Sample extract text",
                    }
                }
            }
        }

        mock_safe.return_value = mock_response

        summary = wiki.get_wiki_summary("New York City")

        assert summary == "Sample extract text"

        first_call_params = mock_safe.call_args_list[0].args[1]
        assert first_call_params["titles"] == "New York City"


def test_get_wiki_summary_search_request_failure():
    first_response = MagicMock()
    first_response.json.return_value = {
        "query": {"pages": {"123": {}}}
    }

    with patch(
        "interactive_city_dashboard.services.wiki.safe_get",
        side_effect=[first_response, None],
    ):
        result = wiki.get_wiki_summary("London")

    assert result == wiki.ERROR_MESSAGE


def test_get_wiki_summary_search_fallback():
    """Fall back to Wikipedia search when direct lookup has no extract."""

    first_response = MagicMock()
    first_response.json.return_value = {
        "query": {
            "pages": {
                "123": {}
            }
        }
    }

    search_response = MagicMock()
    search_response.json.return_value = {
        "query": {
            "search": [
                {"title": "London"}
            ]
        }
    }

    final_response = MagicMock()
    final_response.json.return_value = {
        "query": {
            "pages": {
                "456": {
                    "extract": "London is the capital of England."
                }
            }
        }
    }

    with patch(
        "interactive_city_dashboard.services.wiki.safe_get",
        side_effect=[
            first_response,
            search_response,
            final_response,
        ],
    ):
        summary = wiki.get_wiki_summary("London")
        
        assert summary == "London is the capital of England."


def test_get_wiki_summary_no_search_results():
    """Return a friendly message when Wikipedia returns no matches."""

    first_response = MagicMock()
    first_response.json.return_value = {
        "query": {
            "pages": {
                "123": {}
            }
        }
    }

    search_response = MagicMock()
    search_response.json.return_value = {
        "query": {
            "search": []
        }
    }

    with patch(
        "interactive_city_dashboard.services.wiki.safe_get",
        side_effect=[
            first_response,
            search_response,
        ],
    ):
        summary = wiki.get_wiki_summary("DefinitelyNotARealCity")

        assert summary == wiki.ERROR_MESSAGE


def test_get_wiki_summary_invalid_search_json():
    """Handle invalid JSON returned from search results."""

    first_response = MagicMock()
    first_response.json.return_value = {
        "query": {"pages": {"123": {}}}
    }

    search_response = MagicMock()
    search_response.json.side_effect = ValueError()

    with patch(
        "interactive_city_dashboard.services.wiki.safe_get",
        side_effect=[first_response, search_response],
    ):
        result = wiki.get_wiki_summary("London")

    assert result == wiki.ERROR_MESSAGE


def test_get_wiki_summary_invalid_final_json():
    """Handle invalid JSON returned from the fallback article lookup."""

    first_response = MagicMock()
    first_response.json.return_value = {
        "query": {"pages": {"123": {}}}
    }

    search_response = MagicMock()
    search_response.json.return_value = {
        "query": {"search": [{"title": "London"}]}
    }

    final_response = MagicMock()
    final_response.json.side_effect = ValueError()

    with patch(
        "interactive_city_dashboard.services.wiki.safe_get",
        side_effect=[
            first_response,
            search_response,
            final_response,
        ],
    ):
        result = wiki.get_wiki_summary("London")

    assert result == wiki.ERROR_MESSAGE


def test_get_wiki_summary_best_match_request_failure():
    """Handle request failure during fallback article retrieval."""

    first_response = MagicMock()
    first_response.json.return_value = {
        "query": {"pages": {"123": {}}}
    }

    search_response = MagicMock()
    search_response.json.return_value = {
        "query": {"search": [{"title": "London"}]}
    }

    with patch(
        "interactive_city_dashboard.services.wiki.safe_get",
        side_effect=[
            first_response,
            search_response,
            None,
        ],
    ):
        result = wiki.get_wiki_summary("London")

    assert result == wiki.ERROR_MESSAGE
