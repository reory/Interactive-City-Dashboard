import pytest  # noqa
from dash import Dash
from interactive_city_dashboard.layout.layout import serve_layout
from interactive_city_dashboard.callbacks.callbacks import register_callbacks


def test_callbacks_registered():
    """
    Ensure that all callbacks are registered on a real Dash app instance.
    """

    app = Dash(__name__)
    app.layout = serve_layout()
    register_callbacks(app)

    # Dash stores callbacks in app.callback_map
    callback_map = app.callback_map

    # Expected callback outputs (component_id.property)
    expected_outputs = {
        "city-selector.options",
        "layout-container.className",
        "city-selector.value",
        "map.figure",
        "population-chart.figure",
        "app-wrapper.style",
        "wiki-container.style",
        "wiki-toggle.children",
        "wiki-details.children",
    }

    actual_keys = set(callback_map.keys())
    missing = {k for k in expected_outputs if not any(k in a for a in actual_keys)}
    assert not missing, f"Missing callback outputs: {missing}"


def test_update_dashboard_integration():
    app = Dash(__name__)
    app.layout = serve_layout()
    register_callbacks(app)

    # Find the combined multi-output callback key Dash generated
    key = next(
        k
        for k in app.callback_map
        if "map.figure" in k and "population-chart.figure" in k
    )

    cb = app.callback_map[key]

    # Inputs should be city-selector.value and theme-toggle.value
    inputs = cb["inputs"]
    assert len(inputs) == 2

    ids = {i["id"] for i in inputs}
    props = {i["property"] for i in inputs}

    assert ids == {"city-selector", "theme-toggle"}
    assert props == {"value"}
