from dash import html, dcc
from data.populations import populations

DEFAULT_CITY = list(populations.keys())[0]  # First city in the list


def serve_layout():
    """Return the layout of the API and Map data."""
    
    return html.Div(
        id="app-wrapper",
        style={
            "maxWidth": "1200px",
            "margin": "0 auto",
            "padding": "20px",
            "boxSizing": "border-box",
        },
        children=[
            
            html.H1(
                "Interactive City Map + Population Chart",
                style={"marginBottom": "20px"}
            ),

            # Continent selector
            dcc.Dropdown(
                id="continent-selector",
                options=[
                    {"label": "Europe", "value": "Europe"},
                    {"label": "North America", "value": "North America"},
                    {"label": "South America", "value": "South America"},
                    {"label": "Africa", "value": "Africa"},
                    {"label": "Asia", "value": "Asia"},
                ],
                placeholder="Select a continent...",
                persistence=True,
                persistence_type="local",
                style={
                    "width": "100%",
                    "maxWidth": "300px",
                    "marginBottom": "20px",
                    "backgroundColor": "#ffffff",
                    "color": "#222222",
                },
            ),

            # City selector
            dcc.Dropdown(
                id="city-selector",
                value=DEFAULT_CITY,
                options=[{"label": c, "value": c} for c in populations.keys()],
                placeholder="Select a city...",
                persistence=True,
                persistence_type="local",
                style={
                    "width": "100%",
                    "maxWidth": "300px",
                    "marginBottom": "20px",
                    "backgroundColor": "#ffffff",
                    "color": "#222222",
                },
            ),

            # Theme toggle
            dcc.RadioItems(
                id="theme-toggle",
                options=[
                    {"label": "Light", "value": "light"},
                    {"label": "Dark", "value": "dark"},
                ],
                value="light",
                persistence=True,
                persistence_type="local",
                inline=True,
                style={"marginBottom": "20px"},
            ),

            # Layout selector with info icon
            html.Div(
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "gap": "6px",
                    "marginBottom": "20px",
                },
                children=[
                    dcc.Dropdown(
                        id="layout-selector",
                        options=[
                            {"label": "Side by Side", "value": "side"},
                            {"label": "Stacked", "value": "stacked"},
                            {"label": "Sidebar", "value": "sidebar"},
                            {"label": "Wide Map Focus", "value": "wide"},
                            {"label": "Chart Focus", "value": "chart"},
                            {"label": "Minimalist Clean", "value": "minimal"},
                            {"label": "Three Column Pro", "value": "pro"},
                        ],
                        value="side",
                        persistence=True,
                        persistence_type="local",
                        clearable=False,
                        style={
                            "width": "100%",
                            "maxWidth": "300px",
                            "backgroundColor": "#ffffff",
                            "color": "#222222",
                        },
                    ),
                    html.Span(
                        "🛈",
                        title="Select how map and chart are arranged",
                        style={"cursor": "help"},
                    ),
                ],
            ),
            html.Div(
                id="layout-container",
                className="dashboard",
                children=[
                    dcc.Graph(
                        id="map", 
                        className="panel map",
                        config={"responsive": True}
                    ),
                    dcc.Graph(
                        id="population-chart", 
                        className="panel chart",
                        config={"responsive": True}
                    ),
                    html.Div(
                        [
                            html.Div(
                                "▸ City Information",
                                id="wiki-toggle",
                                n_clicks=0,
                                className="wiki-toggle",
                            ),
                            html.Div(
                                id="wiki-container", 
                                className="wiki-body",
                                children=html.Div(id="wiki-details"),
                            ),
                        ],
                        className="panel wiki",
                    ),
                ],
            ),
        ],
    )
