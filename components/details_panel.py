from dash import html
from data.populations import populations
from services.wiki import get_wiki_summary

def build_details(selected_city):

    if not selected_city or selected_city not in populations:
        return html.Div("Information on a chosen city will appear here.")
    
    data = populations[selected_city]
    summary = get_wiki_summary(selected_city)

    return html.Div([
        html.H3(selected_city),
        html.P(f"Continent: {data['continent']}"),
        html.P(f"Population: {data['pop']:,}"),
        html.P(f"Latitude: {data['lat']}"),
        html.P(f"Longitude: {data['lon']}"),
        html.H4("About this city"),
        html.P(summary)
    ])