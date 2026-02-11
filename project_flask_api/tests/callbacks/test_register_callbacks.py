import pytest
from unittest.mock import Mock
from dash.dependencies import Input, Output
from project_flask_api.callbacks.callbacks import register_callbacks


def test_register_callbacks():
    """
    Ensure that register_callbacks() correctly registers all Dash callbacks
    with the expected Inputs and Outputs.
    """

    # Create a fake Dash app with a mock callback method.
    # The callback method must return a decorator that returns the function unchanged.
    mock_app = Mock()
    mock_app.callback = Mock(side_effect=lambda *args, **kwargs: lambda f: f)

    # Register all callbacks
    register_callbacks(mock_app)

    # You currently register 6 callbacks in callbacks.py
    assert mock_app.callback.call_count == 6

    # Extract all callback calls for inspection
    calls = mock_app.callback.call_args_list

    # 1. update_city_dropdown
    out, inp = calls[0].args
    assert isinstance(out, Output)
    assert out.component_id == "city-selector"
    assert out.component_property == "options"

    assert isinstance(inp, Input)
    assert inp.component_id == "continent-selector"
    assert inp.component_property == "value"


    # 2. switch_layout
    out, inp = calls[1].args
    assert out.component_id == "layout-container"
    assert out.component_property == "className"

    assert inp.component_id == "layout-selector"
    assert inp.component_property == "value"

    # 3. sync_dropdown_with_map
    out, inp = calls[2].args
    assert out.component_id == "city-selector"
    assert out.component_property == "value"

    assert inp.component_id == "map"
    assert inp.component_property == "clickData"

   
    # 4. update_dashboard
    outputs, inputs = calls[3].args

    assert len(outputs) == 3
    assert outputs[0].component_id == "map"
    assert outputs[0].component_property == "figure"

    assert outputs[1].component_id == "population-chart"
    assert outputs[1].component_property == "figure"

    assert outputs[2].component_id == "city-details"
    assert outputs[2].component_property == "children"

    assert len(inputs) == 2
    assert inputs[0].component_id == "city-selector"
    assert inputs[0].component_property == "value"

    assert inputs[1].component_id == "theme-toggle"
    assert inputs[1].component_property == "value"

    # 5. theme_page
    out, inp = calls[4].args
    assert out.component_id == "app-wrapper"
    assert out.component_property == "style"

    assert inp.component_id == "theme-toggle"
    assert inp.component_property == "value"

    # 6. toggle_wiki
    outputs, inp = calls[5].args

    assert outputs[0].component_id == "wiki-container"
    assert outputs[0].component_property == "style"

    assert outputs[1].component_id == "wiki-toggle"
    assert outputs[1].component_property == "children"

    assert inp.component_id == "wiki-toggle"
    assert inp.component_property == "n_clicks"
