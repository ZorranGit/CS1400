forecast = [
    {"Day": "Friday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 2, "Temperature": 60, "Windy?": False}},
    {"Day": "Saturday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 4, "Temperature": 65, "Windy?": True}},
    {"Day": "Sunday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 1, "Temperature": 72, "Windy?": True}},
]
total=0
for forboi in forecast:
    total+=forboi["Weather"]["Rainfall"]
print(total)
