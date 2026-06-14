# Entry point of the API/dash app.
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dash import Dash
from interactive_city_dashboard.layout.layout import serve_layout
from interactive_city_dashboard.callbacks.callbacks import register_callbacks

app = Dash(__name__, suppress_callback_exceptions=True)

# Scaling view for all devices.
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <meta name="viewport" content="width=device-width, initial-scale=1">
        {%title%}
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""
app.layout = serve_layout
register_callbacks(app)
server = app.server


if __name__ == "__main__":
    app.run(debug=True, port=8050)
