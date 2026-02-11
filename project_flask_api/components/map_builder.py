import plotly.express as px
import plotly.graph_objects as go
from data.populations import df, populations

# Build map with markers (using scatter_mapbox)
def build_map(selected_city, theme):
    map_fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        hover_name="City",
        size="Population",
        zoom=3,
        height=400
    )

    # Enable zoom controls and interactivity
    map_fig.update_layout(
        mapbox_style="open-street-map",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        paper_bgcolor=theme["background"],
        plot_bgcolor=theme["panel"],
        font_color=theme["text"]
    )

    # Name the base trace
    map_fig.update_traces(
        marker=dict(size=8, color="blue"),
        name="Cities"
    )

    # If no city selected, return base map
    if not selected_city:
        return map_fig
    
    # Selected city data.
    city = populations[selected_city]

    # Recenter on selected city
    map_fig.update_layout(
        mapbox=dict(
            center={"lat": city["lat"], "lon": city["lon"]},
            zoom=5
        )
    )

    # Highlight selected city
    map_fig.add_scattermapbox(
        lat=[city["lat"]],
        lon=[city["lon"]],
        mode="markers+text",
        marker=dict(size=16, color="red"),
        text=[city["name_en"]],
        textposition="top center",
        textfont=dict(size=25, color=theme["text"]),
        hoverinfo="text",
        name=selected_city
    )
    
    return map_fig
