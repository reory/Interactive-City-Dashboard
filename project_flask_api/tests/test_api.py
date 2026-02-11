# Test_api.py

def test_app_initializes():
    from project_flask_api.api import app

    assert app is not None
    assert callable(app.layout)

    # Optional deeper check:
    layout_instance = app.layout()
    from dash.development.base_component import Component
    assert isinstance(layout_instance, Component)

def test_layout_structure():
    from project_flask_api.api import app
    assert app.layout is not None

def test_callback_register(mocker):
    mock_app = mocker.Mock()
    from project_flask_api.callbacks.callbacks import register_callbacks
    
    # If not exception is raised the test passes.
    register_callbacks(mock_app)
    