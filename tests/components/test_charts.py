import pytest
from project_flask_api.components.charts import build_chart
from project_flask_api.data.populations import df, populations
from plotly.graph_objs import Figure

@pytest.fixture
def theme():
    return {
        "background": "#000000",
        "panel": "#111111",
        "text": "#ffffff"
    }

def test_build_chart_no_city(theme):
    fig = build_chart(None, theme)

    # Should return a plotly figure.
    assert isinstance(fig, Figure)

    # Should contain one bar per city.
    assert len(fig.data[0].x) == len(df["City"])
    assert list(fig.data[0].x) == list(df["City"])

    # Should use the full population dataset.
    assert list(fig.data[0].y) == list(df["Population"])

    # Title should match.
    assert fig.layout.title.text == "Population Of Cities"

    # Theme applied
    assert fig.layout.paper_bgcolor == theme["background"]
    assert fig.layout.plot_bgcolor == theme["panel"]
    assert fig.layout.font.color == theme["text"]

def test_build_chart_with_city(theme):
    selected = list(populations.keys())[0]
    value = populations[selected]["pop"]

    fig = build_chart(selected, theme)

    # Should return a plotly figure.
    assert isinstance(fig, Figure)

    # Should contain exactly one bar.
    assert list(fig.data[0].x) == [selected]
    assert list(fig.data[0].y) == [value]

    # Title should match
    assert fig.layout.title.text == f"Population of {selected}"

    # Y axis range should be 0 -> value * 1.2
    expected_max = int(value * 1.2)
    assert fig.layout.yaxis.range == (0, expected_max)

    # Theme applied.
    assert fig.layout.paper_bgcolor == theme["background"]
    assert fig.layout.plot_bgcolor == theme["panel"]
    assert fig.layout.font.color == theme["text"]