# Test_api.py
from dash.development.base_component import Component
from interactive_city_dashboard.api import app
from interactive_city_dashboard.callbacks.callbacks import register_callbacks


def test_app_initializes():

    assert app is not None
    assert callable(app.layout)
    # Optional deeper check:
    layout_instance = app.layout()
    assert isinstance(layout_instance, Component)


def test_layout_structure():
    assert app.layout is not None


def test_callback_register(mocker):
    mock_app = mocker.Mock()
    # If not exception is raised the test passes.
    register_callbacks(mock_app)
