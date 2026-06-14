import pytest  # noqa
from dash import no_update
from plotly.graph_objs import Figure
from interactive_city_dashboard.data.populations import populations
from interactive_city_dashboard.components.theme import DARK_THEME
from interactive_city_dashboard.callbacks.callbacks import (
    update_city_dropdown,
    switch_layout,
    update_dashboard,
    theme_page,
    toggle_wiki,
    sync_dropdown_with_map,
)


def test_update_city_dropdown_all():

    result = update_city_dropdown(None)
    expected = [{"label": c, "value": c} for c in populations.keys()]

    assert result == expected


def test_update_city_dropdown_filtered():

    result = update_city_dropdown("Europe")
    expected = [
        {"label": city, "value": city}
        for city, data in populations.items()
        if data["continent"] == "Europe"
    ]

    assert result == expected


def test_switch_layout():

    result = switch_layout("side")
    assert result == "dashboard layout-side"


def test_update_dashboard_valid(mocker):
    mock_map = mocker.patch(
        "interactive_city_dashboard.callbacks.callbacks.build_map",
        return_value="MAP",
    )

    mock_chart = mocker.patch(
        "interactive_city_dashboard.components.charts.build_chart",
        return_value=Figure(),
    )

    result = update_dashboard("Paris", "light")

    assert result[0] == "MAP"

    assert isinstance(result[1], Figure)

    mock_map.assert_called_once_with("Paris", mocker.ANY)

    mock_chart.assert_not_called()


def test_update_dashboard_no_city():

    result = update_dashboard(None, "light")
    assert result == (no_update, no_update)


def test_theme_page_dark():

    result = theme_page("dark")

    assert result["background"] == DARK_THEME["wrapper_bg"]
    assert result["color"] == DARK_THEME["text"]


def test_toggle_wiki_open():

    style, label = toggle_wiki(1)
    assert style == {"display": "block"}
    assert "▾" in label


def test_toggle_wiki_closed():

    style, label = toggle_wiki(2)
    assert style == {"display": "none"}
    assert "▸" in label


def test_sync_dropdown_with_map_valid():

    clickData = {"points": [{"text": "Berlin"}]}
    result = sync_dropdown_with_map(clickData)
    assert result == "Berlin"


def test_sync_dropdown_with_map_hovertext():

    clickData = {"points": [{"hovertext": "Rome"}]}
    result = sync_dropdown_with_map(clickData)
    assert result == "Rome"


def test_sync_dropdwon_with_map_no_points():

    result = sync_dropdown_with_map(None)
    assert result is no_update
