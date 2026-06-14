import pytest  # noqa
from unittest.mock import Mock
from interactive_city_dashboard.callbacks.callbacks import register_callbacks


def test_register_callbacks():
    """
    Ensure that register_callbacks() correctly registers all Dash callbacks
    with the expected Inputs and Outputs.
    """

    mock_app = Mock()
    mock_app.callback = Mock(side_effect=lambda *args, **kwargs: lambda f: f)

    register_callbacks(mock_app)

    # Your app registers 7 callbacks
    assert mock_app.callback.call_count == 7

    calls = mock_app.callback.call_args_list

    # 1. update_city_dropdown
    out, inp = calls[0].args
    assert out.component_id == "city-selector"
    assert out.component_property == "options"
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
    out1, out2, inp1, inp2 = calls[3].args

    assert out1.component_id == "map"
    assert out1.component_property == "figure"

    assert out2.component_id == "population-chart"
    assert out2.component_property == "figure"

    assert inp1.component_id == "city-selector"
    assert inp1.component_property == "value"

    assert inp2.component_id == "theme-toggle"
    assert inp2.component_property == "value"

    # 5. theme_page
    out, inp = calls[4].args
    assert out.component_id == "app-wrapper"
    assert out.component_property == "style"
    assert inp.component_id == "theme-toggle"
    assert inp.component_property == "value"

    # 6. toggle_wiki
    out1, out2, inp = calls[5].args
    assert out1.component_id == "wiki-container"
    assert out1.component_property == "style"
    assert out2.component_id == "wiki-toggle"
    assert out2.component_property == "children"
    assert inp.component_id == "wiki-toggle"
    assert inp.component_property == "n_clicks"

    # 7. update_wiki
    out, inp = calls[6].args
    assert out.component_id == "wiki-details"
    assert out.component_property == "children"
    assert inp.component_id == "city-selector"
    assert inp.component_property == "value"
