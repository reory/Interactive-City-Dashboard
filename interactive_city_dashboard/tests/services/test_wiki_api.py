import pytest  # noqa
from unittest.mock import patch, MagicMock
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
        side_effect=Exception("boom"),
    ):
        result = wiki.safe_get("http://example.com", {"a": 1})
        assert result is None


def test_get_wiki_summary_title_with_spaces():
    """Ensure titles with spaces are passed correctly to the API."""
    with patch("interactive_city_dashboard.services.wiki.safe_get") as mock_safe:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "query": {"pages": {"123": {"extract": "Sample extract text"}}}
        }
        mock_safe.return_value = mock_response

        summary = wiki.get_wiki_summary("New York City")

        # Should return the extract
        assert summary == "Sample extract text"

        # First call should be a direct title lookup
        first_call_params = mock_safe.call_args_list[0].args[1]
        assert first_call_params["titles"] == "New York City"
