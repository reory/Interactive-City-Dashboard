import pytest
from project_flask_api.components.map_builder import build_map
from project_flask_api.data.populations import df, populations
from plotly.graph_objs import Figure

@pytest.fixture
def theme():
    return {
        "background": "#000000",
        "panel": "#111111",
        "text": "#ffffff"
    }

def test_build_map_no_city(theme):
    # Build a baseline figure directly from plotly.
    import plotly.express as px
    baseline = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        hover_name="City",
        size="Population",
        zoom=3,
        height=400
    )

    baseline.update_layout(
        mapbox_style="open-street-map",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        paper_bgcolor=theme["background"],
        plot_bgcolor=theme["panel"],
        font_color=theme["text"]
    )

    baseline_sizes = list(baseline.data[0].marker.size) #type:ignore

    # Call function.
    fig = build_map(None, theme)

    # Should return a plotly figure.
    assert isinstance(fig, Figure)

    # Base trace should be named correctly.
    assert fig.data[0].name == "cities" #type:ignore

    # Should keep plotlys default centre.
    # So we assert that zoom is still the default (3)
    assert fig.layout.mapbox.zoom == 3

    # Compare sizes to baseline.
    sizes = list(fig.data[0].marker.size) # type:ignore
    assert sizes == baseline_sizes

def test_build_map_with_city(theme):
    selected = list(populations.keys())[0] # pick any valid city.
    fig = build_map(selected, theme)

    # Should recenter on selected city.
    expected_lat = populations[selected]["lat"]
    expected_lon = populations[selected]["lon"]

    assert fig.layout.mapbox.center.lat == expected_lat
    assert fig.layout.mapbox.center.lon == expected_lon
    assert fig.layout.mapbox.zoom == 5

    # Marker sizes: selected city = 14, others 10.
    sizes = fig.data[0].marker.size #type: ignore
    cities = df["City"].tolist()

    for city, size in zip(cities, sizes):
        if city == selected:
            assert size == 14
        else:
            assert size == 10

    # Marker colors: selected = red, others = blue.
    colors = fig.data[0].marker.color  #type:ignore
    for city, color in zip(cities, colors):
        if city == selected:
            assert color == "red"
        else:
            assert color == "blue"