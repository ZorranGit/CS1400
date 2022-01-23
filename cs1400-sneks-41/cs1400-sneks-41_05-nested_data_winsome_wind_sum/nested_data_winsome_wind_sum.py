forecast = [
    {"Day": "Friday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 2, "Temperature": 60, "Windy?": False}},
    {"Day": "Saturday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 4, "Temperature": 65, "Windy?": True}},
    {"Day": "Sunday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 1, "Temperature": 72, "Windy?": True}},
]
total=0
for okthen in forecast:
    if okthen["Weather"]["Windy?"] is True:
        total+=okthen["Weather"]["Rainfall"]
print(total)
