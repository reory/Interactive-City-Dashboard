# Test_api.py
from dash.development.base_component import Component

from interactive_city_dashboard.api import app


def test_app_initialises():
    """Verify the application initialises successfully."""

    assert app is not None
    assert callable(app.layout)
    # Optional deeper check:
    layout_instance = app.layout()
    assert isinstance(layout_instance, Component)
