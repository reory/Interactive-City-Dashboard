import pytest
from dash import html
from project_flask_api.components.details_panel import build_details
from project_flask_api.data.populations import populations

def test_build_details_no_city():
    result = build_details(None)

    # Should return a Div
    assert isinstance(result, html.Div)

    # Should contain the placeholder text.
    assert result.children == "Information on a chosen city will appear here."


def test_build_details_with_city(mocker):
    
    # Pick any valid city.
    selected = list(populations.keys())[0]
    data = populations[selected]

    # Mock the wiki summary.
    mock_summary = "This is a mock summary."
    mocker.patch(
        "project_flask_api.components.details_panel.get_wiki_summary",
        return_value=mock_summary
    )

    result = build_details(selected)

    # Should return a Div with children list.
    assert isinstance(result, html.Div)
    assert isinstance(result.children, list)

    children = result.children

    # Check structure.
    assert isinstance(children[0], html.H3)
    assert children[0].children == selected

    assert isinstance(children[1], html.P)
    assert children[1].children == f"Continent: {data['continent']}"

    assert isinstance(children[2], html.P)
    assert children[2].children == f"Population: {data['pop']:,}"

    assert isinstance(children[3], html.P)
    assert children[3].children == f"Latitude: {data['lat']}"

    assert isinstance(children[4], html.P)
    assert children[4].children == f"Longitude: {data['lon']}"

    assert isinstance(children[5], html.H4)
    assert children[5].children == "About this city"

    assert isinstance(children[6], html.P)
    assert children[6].children == mock_summary