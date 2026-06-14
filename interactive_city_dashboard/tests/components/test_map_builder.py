import pytest
from interactive_city_dashboard.components.map_builder import build_map
from interactive_city_dashboard.data.populations import populations
from plotly.graph_objs import Figure


@pytest.fixture
def theme():
    return {"background": "#000000", "panel": "#111111", "text": "#ffffff"}


def test_build_map_no_city(theme):
    fig = build_map(None, theme)

    # Should return a plotly figure.
    assert isinstance(fig, Figure)

    # Base trace should be named correctly.
    assert fig.data[0].name == "Cities"

    # Should keep default zoom (3)
    assert fig.layout.mapbox.zoom == 3

    # Marker size should be the fixed size you set (8)
    assert fig.data[0].marker.size == 8

    # Marker color should be blue
    assert fig.data[0].marker.color == "blue"


def test_build_map_with_city(theme):
    selected = list(populations.keys())[0]
    fig = build_map(selected, theme)

    # Should recenter on selected city.
    expected_lat = populations[selected]["lat"]
    expected_lon = populations[selected]["lon"]

    assert fig.layout.mapbox.center.lat == expected_lat
    assert fig.layout.mapbox.center.lon == expected_lon
    assert fig.layout.mapbox.zoom == 5

    # First trace: base cities (blue, size 8)
    base_trace = fig.data[0]
    assert base_trace.marker.size == 8
    assert base_trace.marker.color == "blue"

    # Second trace: selected city highlight
    highlight = fig.data[1]
    assert highlight.marker.size == 16
    assert highlight.marker.color == "red"
    assert list(highlight.lat) == [expected_lat]
    assert list(highlight.lon) == [expected_lon]
