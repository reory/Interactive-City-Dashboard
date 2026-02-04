import pytest
from dash import html, dcc
from project_flask_api.layout.layout import serve_layout
from project_flask_api.data.populations import populations


def test_layout_root_structure():
    layout = serve_layout()

    # Root must be a Div.
    assert isinstance(layout, html.Div)
    assert layout.id == "app-wrapper" #type:ignore

    # Children must be a list.
    assert isinstance(layout.children, list)

    # New layout has 7 top-level children:
    # 0: header
    # 1: continent selector
    # 2: city selector
    # 3: layout selector wrapper
    # 4: theme toggle
    # 5: wiki section
    # 6: dashboard container
    assert len(layout.children) == 7


def test_layout_contains_header():
    layout = serve_layout()
    header = layout.children[0] #type:ignore

    assert isinstance(header, html.H1)
    assert header.children == "Interactive City Map + Population Chart"


def test_continent_selector():
    layout = serve_layout()
    continent_dd = layout.children[1] #type:ignore

    assert isinstance(continent_dd, dcc.Dropdown)
    assert continent_dd.id == "continent-selector" #type:ignore

    expected_labels = ["Europe", "North America", "South America", "Africa", "Asia"]
    actual_labels = [opt["label"] for opt in continent_dd.options] #type:ignore

    assert actual_labels == expected_labels


def test_city_selector():
    layout = serve_layout()
    city_dd = layout.children[2] #type:ignore

    assert isinstance(city_dd, dcc.Dropdown)
    assert city_dd.id == "city-selector" #type:ignore

    expected_cities = list(populations.keys())
    actual_cities = [opt["value"] for opt in city_dd.options] #type:ignore

    assert actual_cities == expected_cities


def test_layout_selector():
    layout = serve_layout()
    wrapper = layout.children[3] #type:ignore

    assert isinstance(wrapper, html.Div)
    assert isinstance(wrapper.children, list)

    layout_dd = wrapper.children[0]
    info_icon = wrapper.children[1]

    assert isinstance(layout_dd, dcc.Dropdown)
    assert layout_dd.id == "layout-selector" #type:ignore
    assert layout_dd.value == "side" #type:ignore

    expected_layouts = ["side", "stacked", "sidebar", "wide", "chart", "minimal", "pro"]
    actual_layouts = [opt["value"] for opt in layout_dd.options] #type:ignore

    assert actual_layouts == expected_layouts

    assert isinstance(info_icon, html.Span)
    assert info_icon.children == "🛈"


def test_dynamic_containers_exist():
    layout = serve_layout()

    # Theme toggle
    theme_toggle = layout.children[4] #type:ignore
    assert isinstance(theme_toggle, dcc.RadioItems)
    assert theme_toggle.id == "theme-toggle" #type:ignore

    # Wiki section
    wiki_section = layout.children[5] #type:ignore
    assert isinstance(wiki_section, html.Div)
    assert wiki_section.id == "wiki-section" #type:ignore

    wiki_toggle = wiki_section.children[0] #type:ignore
    wiki_container = wiki_section.children[1] #type:ignore

    assert wiki_toggle.id == "wiki-toggle"
    assert wiki_container.id == "wiki-container"

    wiki_details = wiki_container.children
    assert isinstance(wiki_details, html.Div)
    assert wiki_details.id == "wiki-details" #type:ignore

    # Dashboard container
    dashboard = layout.children[6] #type:ignore
    assert isinstance(dashboard, html.Div)
    assert dashboard.id == "dashboard-container" #type:ignore

    map_div = dashboard.children[0] #type:ignore
    chart_div = dashboard.children[1] #type:ignore

    assert map_div.id == "map"
    assert chart_div.id == "population-chart"
