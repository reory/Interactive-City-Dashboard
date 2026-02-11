import pytest
from unittest.mock import patch
from dash import Dash
from project_flask_api.api import app as dash_app


def test_app_initializes():
    """Ensure the Dash app loads and exposes a layout."""
    assert isinstance(dash_app, Dash)
    assert dash_app.layout is not None


def test_callbacks_registered():
    """Ensure the callback map contains all expected callbacks."""
    callback_map = dash_app.callback_map

    # These IDs must exist in the callback registry
    expected_outputs = {
        "city-selector.options",
        "layout-container.className",
        "city-selector.value",
        "map.figure",
        "population-chart.figure",
        "city-details.children",
        "app-wrapper.style",
        "wiki-container.style",
        "wiki-toggle.children",
    }

    assert expected_outputs.issubset(set(callback_map.keys()))


def test_update_dashboard_integration(mocker):
    """
    Simulate the update_dashboard callback firing through Dash's callback map.
    This ensures the callback wiring + return structure works end-to-end.
    """

    # Mock heavy components
    mocker.patch(
        "project_flask_api.components.map_builder.build_map",
        return_value="MAP"
    )
    mocker.patch(
        "project_flask_api.components.charts.build_chart",
        return_value="CHART"
    )
    mocker.patch(
        "project_flask_api.components.details_panel.build_details",
        return_value="DETAILS"
    )

    # Locate the callback in Dash's registry
    callback = dash_app.callback_map["map.figure"]["callback"]

    # Simulate callback invocation
    result = callback("Paris", "light")

    assert result == ("MAP", "CHART", "DETAILS")
