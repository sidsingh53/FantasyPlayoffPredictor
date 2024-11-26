
# Fantasy Football League Tracker (Under some work rn)

A web-based application for tracking and displaying the performance of teams in a fantasy football league. This app will display various statistics like **points for**, **points against**, **head-to-head results**, and other performance data to help users analyze and compare different teams over the course of a season.

## Features

- Displays the team rankings based on **points for** and **points against**.
- Calculates and updates **head-to-head** results between teams.
- Provides real-time data and updated statistics based on the matchups.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (for dynamic content).
- **Backend**: Python (Flask or any other web framework, depending on your implementation).
- **Template Engine**: Jinja2 (if you're using Flask).
- **Database**: Optionally, you can use a database (like SQLite, MySQL, or PostgreSQL) for storing team stats.

## Setup and Installation

Follow the instructions below to set up this project on your local machine.

### Prerequisites

Before starting, make sure you have the following installed:
- Python 3.x (For running the backend)
- Flask (or other Python web framework)
- Text editor or IDE (like VSCode, PyCharm, etc.)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fantasy-football-tracker.git
cd fantasy-football-tracker
```

### 2. Set up the environment

Create a virtual environment and install the required dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
pip install -r requirements.txt
```

### 3. Update Configuration (if needed)

If you're using a database or need to update the app's configuration, modify the `config.py` (or equivalent file) to match your environment.

### 4. Run the Application

```bash
python app.py
```

This will start the server locally. By default, it should be accessible at `http://localhost:5000`.

### 5. Access the Application

Once the server is running, open your browser and navigate to `http://localhost:5000` to see the Fantasy Football League Tracker in action.

## How to Use

- View team statistics including **points for** and **points against**.
- Compare teams' head-to-head results for the season.
- Check team rankings based on performance.
team.

## Contributing

We welcome contributions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Example Team Data (JSON)

Here is an example of how the data might look in your app:

```json
[
  {
    "name": "Lakeside Lions",
    "wins": 10,
    "losses": 2,
    "points_for": 1489.8,
    "points_against": 1115.9,
    "head_to_head": {
      "Seattle Sickos": {"wins": 1, "losses": 0},
      "GoHoos": {"wins": 1, "losses": 0}
    }
  },
  {
    "name": "Seattle Sickos",
    "wins": 7,
    "losses": 5,
    "points_for": 1268.7,
    "points_against": 1181.0,
    "head_to_head": {
      "Lakeside Lions": {"wins": 0, "losses": 1},
      "GoHoos": {"wins": 1, "losses": 0}
    }
  }
]
```

### Troubleshooting

- **Server Not Starting:** Ensure the correct version of Python is installed and dependencies are properly set up in your `requirements.txt`.
- **Data Not Showing:** Double-check if your team data is properly being fetched and rendered. Check the `console` and `network` tabs in the browser developer tools to ensure everything is loading correctly.
- **CSS/JS Not Loading:** Ensure static files (CSS/JS) are in the correct directories and being served properly by the backend.
