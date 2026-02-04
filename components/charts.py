import plotly.express as px
from data.populations import df, populations

def build_chart(selected_city, theme):

    # No city is selected, show the full dataset.
    if selected_city is None:
        fig = px.bar(
            df,
            x="City",
            y="Population",
            title="Population Of Cities",
        )
        fig.update_layout(
            paper_bgcolor=theme["background"],
            plot_bgcolor=theme["panel"],
            font_color=theme["text"]
        )
        return fig
    
    # City selected, show single bar.
    value = populations[selected_city]["pop"]

    chart_fig = px.bar(
            x = [selected_city],
            y = [value],
            title = f"Population of {selected_city}",
            labels = {"x": "City", "y": "population"},
    )

    chart_fig.update_layout(
        yaxis=dict(range=[0, int(value *1.2)]),
        paper_bgcolor=theme["background"],
        plot_bgcolor=theme["panel"],
        font_color=theme["text"]
    )
    
    return chart_fig