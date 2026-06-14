import pytest  # noqa
from dash import html, dcc
from interactive_city_dashboard.layout.layout import serve_layout


def test_layout_root_structure():
    layout = serve_layout()

    # Top-level wrapper
    assert isinstance(layout, html.Div)
    assert layout.id == "app-wrapper"

    # It should contain exactly 6 children
    assert len(layout.children) == 6

    # Check key components exist in correct order
    assert isinstance(layout.children[0], html.H1)
    assert isinstance(layout.children[1], dcc.Dropdown)  # continent selector
    assert isinstance(layout.children[2], dcc.Dropdown)  # city selector
    assert isinstance(layout.children[3], dcc.RadioItems)  # theme toggle
    assert isinstance(layout.children[4], html.Div)  # layout selector wrapper
    assert isinstance(layout.children[5], html.Div)  # layout-container


def test_layout_selector():
    layout = serve_layout()

    selector_wrapper = layout.children[4]
    assert isinstance(selector_wrapper, html.Div)

    # First child inside wrapper is the layout selector dropdown
    selector = selector_wrapper.children[0]
    assert isinstance(selector, dcc.Dropdown)
    assert selector.id == "layout-selector"


def test_dynamic_containers_exist():
    layout = serve_layout()

    layout_container = layout.children[5]
    assert isinstance(layout_container, html.Div)
    assert layout_container.id == "layout-container"

    # layout-container should have 3 children: map, chart, wiki panel
    assert len(layout_container.children) == 3

    map_graph = layout_container.children[0]
    chart_graph = layout_container.children[1]
    wiki_panel = layout_container.children[2]

    assert isinstance(map_graph, dcc.Graph)
    assert map_graph.id == "map"

    assert isinstance(chart_graph, dcc.Graph)
    assert chart_graph.id == "population-chart"

    # Wiki panel structure
    assert isinstance(wiki_panel, html.Div)
    assert wiki_panel.className == "panel wiki"

    wiki_toggle = wiki_panel.children[0]
    wiki_container = wiki_panel.children[1]

    assert wiki_toggle.id == "wiki-toggle"
    assert wiki_container.id == "wiki-container"

    # wiki-container should contain wiki-details
    assert isinstance(wiki_container.children, html.Div)
    assert wiki_container.children.id == "wiki-details"
