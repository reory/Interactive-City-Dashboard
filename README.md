<p align="center">
  <strong>🌍 Interactive City Dashboard</strong><br>
  <em>Explore world cities with an interactive map, charts, and live data</em>
</p>

![Last Commit](https://img.shields.io/github/last-commit/reory/interactive_city_dashboard?cacheSeconds=60)
![Repo Size](https://img.shields.io/github/repo-size/reory/interactive_city_dashboard?cacheSeconds=60)
![License](https://img.shields.io/badge/License-MIT-green)

![Dash](https://img.shields.io/badge/Dash-1E88E5?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
[![Folium](https://img.shields.io/badge/Folium-orange.svg)](https://python-visualization.github.io/folium/)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)](https://www.sqlalchemy.org/)

## 🗺️ Interactive City Map + Population Dashboard

- A fully interactive Dash application that visualises world cities with:
- A dynamic Mapbox map
- A responsive population bar chart
- A collapsible Wikipedia-powered city information panel
- A clean light/dark theme system
- Multiple layout modes (side-by-side, stacked, wide, minimalist, pro)
- A modular, test-driven architecture designed for clarity and maintainability

This project demonstrates professional-grade Dash engineering, clean separation of concerns, and a fully tested callback + layout system.

---

## 📑 Table of Contents

- [Why This Project Exists](#-why-this-project-exists)
- [Problem](#-problem)
- [Solution](#-solution)
- [Features](#-features)
- [Demo](#-demo)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Running the App](#running-the-app)
- [Architecture Principles](#-architecture-principles)
- [Deployment](#-deployment)
- [Testing](#-testing)
- [Roadmap Features](#️-roadmap-features)

---

## 🧠 Why This Project Exists

This project was created to explore interactive data visualisation using Dash, Plotly, and Mapbox. The goal is to provide an engaging way to explore world cities through maps, population statistics, and live information sources while demonstrating modular application design and test-driven development.

---

## 🔍 Problem 
Geographical datasets are often presented in static tables that make it difficult to explore relationships between locations, population data, and contextual information.

## ✅ Solution 
This project combines mapping, visualisation, and live information retrieval into a unified interactive dashboard, making city exploration more intuitive and engaging.

---

## 🚀Features

### Interactive Map
- Click any city to update the dashboard
- Map auto-centres and highlights the selected city
- Interactive map built with Plotly and OpenStreetMap

### Population Chart
- Shows population for the selected city
- Automatically scales the y-axis
- Theme-aware styling

### Wikipedia Summary Panel
- Collapsible “City Information” panel
- Fetches live city summaries through a dedicated service layer.
- Clean separation between UI and data fetching

### Light/Dark Themes
- Full theme propagation across map, chart, and layout
- Smooth transitions

### Multiple Layout Modes
- Side-by-side
- Stacked
- Sidebar
- Wide map focus
- Chart focus
- Minimalist
- Three-column “Pro” layout

### Testing
- Layout tests
- Callback unit tests
- Integration tests using Dash’s callback map

### Export Options

- Export map visualisations as PNG
- Export charts as PNG using Plotly tools
- High-resolution image downloads
- Export PDF report

---

## Demo

### 🎥 Video Preview

Click below to watch the 1 minute demo:

[▶️ View Demo Video](https://github.com/reory/Interactive-City-Dashboard/releases/download/v0.1.0/Demo.mp4)

---

## 📸 Screenshots

<details>
   <summary>click here</summary>

### Dashboard (Light Mode)

- Interactive city selection on a world map.
- Population analysis through dynamic charts.
- Responsive dashboard layout.
![Dashboard Light](screenshots/dashboard.png)

### Dashboard (Dark Mode)

- Interactive city selection on a world map.
- Population analysis through dynamic charts.
- Responsive dashboard layout with Dark Mode
![Dashboard Dark](screenshots/dashboard-darkmode.png)

### City Views

- Different view tabs
![City 1](screenshots/cities%201.png)
![City 2](screenshots/cities%202.png)
![City 3](screenshots/cities%203.png)
![City 4](screenshots/cities%204.png)
![City 5](screenshots/cities%205.png)

### PDF Report Export

- Generate downloadable dashboard reports for the selected city.
- Includes city demographics and geographic coordinates.
- Embeds the current population chart and map view.
- Incorporates Wikipedia summary information.
- Produces presentation-ready PDF documents for sharing and archiving.

![PDF report](screenshots/export_pdf.png)

</details>

---

## ⚒️ Project Structure

<details>
  <summary>click here</summary>

```plaintext
interactive_city_dashboard/
│
├── api.py                     # Dash app entrypoint
│
├── data/
│   └── populations.py         # City dataset
│
├── services/
│   ├── report_generator.py    # PDF report generation utilities
│   └── wiki.py                # Wikipedia summary fetcher
│
├── components/
│   ├── map_builder.py         # Map figure builder
│   ├── charts.py              # Population chart builder
│   ├── details_panel.py       # Wiki/details panel builder
│   └── theme.py               # Light/Dark theme definitions
│
├── layout/
│   └── layout.py              # serve_layout() → full UI tree
│
├── callbacks/
│   └── callbacks.py           # Pure callback logic + register_callbacks()
│
└── tests/                     # Pytest suite
    ├── test_layout.py
    ├── test_callbacks.py
    └── test_integration_app.py
```

</details>

---

## 💻 Installation

```bash
git clone https://github.com/reory/Interactive-City-Dashboard.git
cd Interactive-City-Dashboard
```

### Install Dependencies

```bash
uv sync
```

### Running the App

```bash
uv run python api.py
```

Then open:
http://127.0.0.1:8050

---

## 🏢 Architecture Principles

<details>
  <summary>click here</summary>

This project follows:

Pure functions:
- All callback logic is pure and testable.

Separation of concerns:
- Layout = static UI

- Callbacks = behaviour

- Components = reusable UI builders

- Services = external data

- Data = static datasets

Predictable state:
- No hidden globals, no side effects.

Test-driven structure:
- Every major part of the app is validated.

</details>

---

## 💻 Deployment

<details>
  <summary>click here</summary>

This app can be deployed to:

- Heroku
- Render
- Azure App Service
- Docker
- Gunicorn + Nginx
- Expose the server object in api.py:

```bash
server = app.server
```

</details>

---

## 🧪 Testing

The test suite includes:

- Layout validation tests
- Callback unit tests
- Integration tests
- Dashboard behaviour verification

```bash
uv run pytest
```

---

## 🛣️ Roadmap Features

- [x] Export charts as PNG
- [x] Export dashboard reports as PDF
- [ ] Additional demographic datasets
- [ ] GDP and economic indicators
- [ ] Weather integration
- [ ] Migrate Plotly mapbox → maplibre API
- [ ] Geographic clustering
- [ ] Real-time city statistics APIs

---

**Built by Roy Peters** [Click here for contact details 😁](https://www.linkedin.com/in/roy-p-74980b382/)