# teams.py

teams = [
    {
        "name": "Lakeside Lions", 
        "wins": 10, 
        "losses": 2, 
        "points_for": 1594.96, 
        "points_against": 1243.8, 
        "head_to_head": {
            "Seattle Sickos": 1, 
            "GoHoos": 2, 
            "Raven Lunatics": 1,
            "Deal Makers": 1
        }
    },
    {
        "name": "Seattle Sickos", 
        "wins": 7, 
        "losses": 5, 
        "points_for": 1383.9, 
        "points_against": 1328.8, 
        "head_to_head": {
            "Lakeside Lions": 0, 
            "GoHoos": 1,
            "Raven Lunatics": 1,
            "Deal Makers": 1
        }
    },
    {
        "name": "GoHoos", 
        "wins": 8, 
        "losses": 4, 
        "points_for": 1537.52, 
        "points_against": 1412.12, 
        "head_to_head": {
            "Lakeside Lions": 1, 
            "Seattle Sickos": 0,
            "Raven Lunatics": 1,
            "Deal Makers": 0
        }
    },
    {
        "name": "Raven Lunatics", 
        "wins": 7, 
        "losses": 5, 
        "points_for": 1450.52, 
        "points_against": 1308.98, 
        "head_to_head": {
            "Lakeside Lions": 0, 
            "Seattle Sickos": 0, 
            "GoHoos": 1,
            "Deal Makers": 1
        }
    },
    {
        "name": "Deal Makers", 
        "wins": 6, 
        "losses": 6, 
        "points_for": 1363.46, 
        "points_against": 1191.94, 
        "head_to_head": {
            "Lakeside Lions": 0, 
            "Seattle Sickos": 0, 
            "GoHoos": 1,
            "Raven Lunatics": 0
        }
    },
    {
        "name": "Henry", 
        "wins": 6, 
        "losses": 6, 
        "points_for": 1252.72, 
        "points_against": 1442.72, 
        "head_to_head": {
            "Lakeside Lions": 1, 
            "Seattle Sickos": 1, 
            "GoHoos": 0, 
            "Raven Lunatics": 1
        }
    },
    {
        "name": "Trojan Army", 
        "wins": 7, 
        "losses": 5, 
        "points_for": 1246.62, 
        "points_against": 1315.44, 
        "head_to_head": {
            "Lakeside Lions": 0, 
            "Seattle Sickos": 1,
            "GoHoos": 1,
            "Deal Makers": 1
        }
    },
    {
        "name": "Who here isn't eskimo bros", 
        "wins": 6, 
        "losses": 6, 
        "points_for": 1406.6, 
        "points_against": 1331.58, 
        "head_to_head": {
            "Lakeside Lions": 0, 
            "Seattle Sickos": 1,
            "GoHoos": 0, 
            "Raven Lunatics": 1
        }
    },
    {
        "name": "Who's Your Daddy", 
        "wins": 6, 
        "losses": 6, 
        "points_for": 1326.5, 
        "points_against": 1308.6, 
        "head_to_head": {
            "Lakeside Lions": 0, 
            "Seattle Sickos": 1, 
            "GoHoos": 1, 
            "Deal Makers": 1
        }
    },
    {
        "name": "Diabeto Domination", 
        "wins": 5, 
        "losses": 7, 
        "points_for": 1302.38, 
        "points_against": 1402.12, 
        "head_to_head": {
            "Lakeside Lions": 0, 
            "Seattle Sickos": 1, 
            "GoHoos": 0, 
            "Raven Lunatics": 0
        }
    },
    {
        "name": "Jack the Gripper", 
        "wins": 6, 
        "losses": 6, 
        "points_for": 1373.84, 
        "points_against": 1278.66, 
        "head_to_head": {
            "Lakeside Lions": 1, 
            "Seattle Sickos": 0, 
            "GoHoos": 0, 
            "Deal Makers": 1
        }
    },
    {
        "name": "PEPE CARTEL", 
        "wins": 3, 
        "losses": 9, 
        "points_for": 1281.86, 
        "points_against": 1463.9, 
        "head_to_head": {
            "Lakeside Lions": 0, 
            "Seattle Sickos": 1, 
            "GoHoos": 0, 
            "Raven Lunatics": 1
        }
    },
    {
        "name": "Dawg Pound", 
        "wins": 4, 
        "losses": 8, 
        "points_for": 1134.44, 
        "points_against": 1332.72, 
        "head_to_head": {
            "Lakeside Lions": 0, 
            "Seattle Sickos": 0, 
            "GoHoos": 1, 
            "Deal Makers": 0
        }
    },
    {
        "name": "Tomlin's Troops", 
        "wins": 3, 
        "losses": 9, 
        "points_for": 1255.84, 
        "points_against": 1425.56, 
        "head_to_head": {
            "Lakeside Lions": 1, 
            "Seattle Sickos": 0, 
            "GoHoos": 1, 
            "Raven Lunatics": 1
        }
    }
]

# Hardcoded matchups for the next two weeks
matchups_week_13 = [
    ("Dawg Pound", "Seattle Sickos"),
    ("Trojan Army", "Raven Lunatics"),
    ("Deal Makers", "Diabeto Domination"),
    ("Henry", "Who here isn't eskimo bros"),
    ("Who's Your Daddy", "Lakeside Lions"),
    ("Jack the Gripper", "GoHoos"),
    ("PEPE CARTEL", "Tomlin's Troops")
]

matchups_week_14 = [
    ("Henry", "GoHoos"),
    ("Seattle Sickos", "Dawg Pound"),
    ("Raven Lunatics", "Who here isn't eskimo bros"),
    ("PEPE CARTEL", "Who's Your Daddy"),
    ("Lakeside Lions", "Diabeto Domination"),
    ("Jack the Gripper", "Deal Makers"),
    ("Tomlin's Troops", "Trojan Army")
]