from dash import Output, Input, no_update
from data.populations import populations
from components.charts import build_chart
from components.details_panel import build_details
from components.map_builder import build_map
from components.theme import LIGHT_THEME, DARK_THEME

def update_city_dropdown(continent):
    """Return city dropdown options based on selected continent."""
    if continent is None:
        return [{"label": c, "value": c} for c in populations.keys()]

    return [
        {"label": city, "value": city}
        for city, data in populations.items()
        if data["continent"] == continent
    ]


def switch_layout(layout_choice):
    return f"dashboard layout-{layout_choice}"

def update_dashboard(dropdown_value, theme_choice):
    """Main dashboard update: map, chart"""

    if not dropdown_value:
        return no_update, no_update
    
    theme = LIGHT_THEME if theme_choice == "light" else DARK_THEME
    selected_city = dropdown_value

    map_fig = build_map(selected_city, theme)
    chart = build_chart(selected_city, theme)

    return map_fig, chart


def theme_page(theme_choice):
    """Return page-level style based on theme."""
    theme = LIGHT_THEME if theme_choice == "light" else DARK_THEME
    return {
        "background": theme["wrapper_bg"],
        "color": theme["text"],
        "minHeight": "100vh",
        "margin": "0",
        "padding": "0",
        "transition": "background 0.3s ease, color 0.3s ease"
    }

def toggle_wiki(n):
    """Toggle the wiki box on/off."""
    if n and n % 2 == 1:
        return {"display": "block"}, "▾ City Information"
    return {"display": "none"}, "▸ City Information"

def sync_dropdown_with_map(clickData):
    
    if clickData and clickData.get("points"):
        point = clickData["points"][0]
        return point.get("text") or point.get("hovertext")
    
    return no_update

def update_wiki(selected_city):
    return build_details(selected_city)

# ---------- DASH WIRING ONLY ----------

def register_callbacks(app):
    app.callback(
        Output("city-selector", "options"),
        Input("continent-selector", "value")
    )(update_city_dropdown)

    app.callback(
        Output("layout-container", "className"),
        Input("layout-selector", "value"),
    )(switch_layout)

    app.callback(
        Output("city-selector", "value"),
        Input("map", "clickData"),
        prevent_initial_call=True
    )(sync_dropdown_with_map)

    app.callback(
            Output("map", "figure"),
            Output("population-chart", "figure"),
            Input("city-selector", "value"),
            Input("theme-toggle", "value")
    )(update_dashboard)

    app.callback(
        Output("app-wrapper", "style"),
        Input("theme-toggle", "value")
    )(theme_page)

    app.callback(
        Output("wiki-container", "style"),
        Output("wiki-toggle", "children"),
        Input("wiki-toggle", "n_clicks"),
    )(toggle_wiki)

    app.callback(
        Output("wiki-details", "children"),
        Input("city-selector", "value")
    )(update_wiki)
