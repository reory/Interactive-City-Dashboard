import pandas as pd

# Example population dataset

populations = {
    
    # Europe
    "London": {"lat": 51.5074, "lon": -0.1278, "pop": 9304000, "continent": "Europe"},
    "Paris": {"lat": 48.8566, "lon": 2.3522, "pop": 2148000, "continent": "Europe"},
    "Berlin": {"lat": 52.5200, "lon": 13.4050, "pop": 3769000, "continent": "Europe"},
    "Madrid": {"lat": 40.4168, "lon": -3.7038, "pop": 3223000, "continent": "Europe"},
    "Rome": {"lat": 41.9028, "lon": 12.4964, "pop": 2873000, "continent": "Europe"},
    "Moscow": {"lat": 55.7558, "lon": 37.6173, "pop": 12506000, "continent": "Europe"},
    "Vienna": {"lat": 48.2082, "lon": 16.3738, "pop": 1950000, "continent": "Europe"},
    "Warsaw": {"lat": 52.2297, "lon": 21.0122, "pop": 1793579, "continent": "Europe"},
    "Budapest": {"lat": 47.4979, "lon": 19.0402, "pop": 1756000, "continent": "Europe"},
    "Prague": {"lat": 50.0755, "lon": 14.4378, "pop": 1309000, "continent": "Europe"},
    "Stockholm": {"lat": 59.3293, "lon": 18.0686, "pop": 975000, "continent": "Europe"},

    # North America
    "Washington D.C.": {"lat": 38.9072, "lon": -77.0369, "pop": 705000, "continent": "North America"},
    "Ottawa": {"lat": 45.4215, "lon": -75.6972, "pop": 1000000, "continent": "North America"},
    "Mexico City": {"lat": 19.4326, "lon": -99.1332, "pop": 21581000, "continent": "North America"},
    "Havana": {"lat": 23.1136, "lon": -82.3666, "pop": 2130000, "continent": "North America"},
    "Guatemala City": {"lat": 14.6349, "lon": -90.5069, "pop": 3000000, "continent": "North America"},
    "Panama City": {"lat": 8.9824, "lon": -79.5199, "pop": 880691, "continent": "North America"},
    "San José": {"lat": 9.9281, "lon": -84.0907, "pop": 342000, "continent": "North America"},
    "Kingston": {"lat": 17.9712, "lon": -76.7936, "pop": 670000, "continent": "North America"},
    "Port-au-Prince": {"lat": 18.5944, "lon": -72.3074, "pop": 987000, "continent": "North America"},

    # South America
    "Brasília": {"lat": -15.8267, "lon": -47.9218, "pop": 4291000, "continent": "South America"},
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816, "pop": 15153000, "continent": "South America"},
    "Santiago": {"lat": -33.4489, "lon": -70.6693, "pop": 6310000, "continent": "South America"},
    "Lima": {"lat": -12.0464, "lon": -77.0428, "pop": 9751000, "continent": "South America"},
    "Bogotá": {"lat": 4.7110, "lon": -74.0721, "pop": 10700000, "continent": "South America"},
    "Quito": {"lat": -0.1807, "lon": -78.4678, "pop": 2011388, "continent": "South America"},
    "Caracas": {"lat": 10.4806, "lon": -66.9036, "pop": 1943901, "continent": "South America"},
    "Montevideo": {"lat": -34.9011, "lon": -56.1645, "pop": 1719453, "continent": "South America"},

    # Africa
    "Cairo": {"lat": 30.0444, "lon": 31.2357, "pop": 20484965, "continent": "Africa"},
    "Lagos": {"lat": 6.5244, "lon": 3.3792, "pop": 15388000, "continent": "Africa"},
    "Nairobi": {"lat": -1.2921, "lon": 36.8219, "pop": 4397000, "continent": "Africa"},
    "Addis Ababa": {"lat": 9.0300, "lon": 38.7400, "pop": 5005000, "continent": "Africa"},
    "Accra": {"lat": 5.6037, "lon": -0.1870, "pop": 2291352, "continent": "Africa"},
    "Dakar": {"lat": 14.7167, "lon": -17.4677, "pop": 1146052, "continent": "Africa"},
    "Rabat": {"lat": 34.0209, "lon": -6.8416, "pop": 577827, "continent": "Africa"},
    "Algiers": {"lat": 36.7538, "lon": 3.0588, "pop": 3415811, "continent": "Africa"},
    "Kampala": {"lat": 0.3476, "lon": 32.5825, "pop": 1659600, "continent": "Africa"},
    "Khartoum": {"lat": 15.5007, "lon": 32.5599, "pop": 5274321, "continent": "Africa"},

    # Asia
    "Tokyo": {"lat": 35.6895, "lon": 139.6917, "pop": 37400000, "continent": "Asia"},
    "Beijing": {"lat": 39.9042, "lon": 116.4074, "pop": 20035455, "continent": "Asia"},
    "Delhi": {"lat": 28.7041, "lon": 77.1025, "pop": 28514000, "continent": "Asia"},
    "Seoul": {"lat": 37.5665, "lon": 126.9780, "pop": 9776000, "continent": "Asia"},
    "Bangkok": {"lat": 13.7563, "lon": 100.5018, "pop": 10539000, "continent": "Asia"},
    "Jakarta": {"lat": -6.2088, "lon": 106.8456, "pop": 10770487, "continent": "Asia"},
    "Manila": {"lat": 14.5995, "lon": 120.9842, "pop": 13923452, "continent": "Asia"},
    "Kuala Lumpur": {"lat": 3.1390, "lon": 101.6869, "pop": 8285000, "continent": "Asia"},
    "Riyadh": {"lat": 24.7136, "lon": 46.6753, "pop": 7670000, "continent": "Asia"},
    "Tehran": {"lat": 35.6892, "lon": 51.3890, "pop": 8846782, "continent": "Asia"},
    "Baghdad": {"lat": 33.3152, "lon": 44.3661, "pop": 7180889, "continent": "Asia"},
    "Hanoi": {"lat": 21.0278, "lon": 105.8342, "pop": 8000000, "continent": "Asia"},
    "Taipei": {"lat": 25.0330, "lon": 121.5654, "pop": 2600000, "continent": "Asia"},
}

# Ensure every city has an explicit English label.
for city_name, data in populations.items():
    data.setdefault("name_en", city_name)


# Convert to DataFrame for Plotly
df = pd.DataFrame([
    {
        "City": city, 
        "lat": data["lat"], 
        "lon": data["lon"], 
        "Population": data["pop"],
        "Continent": data["continent"]
    }
    for city, data in populations.items()
])