# Python 2 Final - API + Database Backend Data Processing

**Author:** Amanullah Anis  
**Created:** July 25, 2025  

---

## Overview

This program retrieves statistics for the top five soccer teams in the English Premier League based on a user-selected season. It then:

1. Creates a SQLite database to store the data
2. Generates 4 bar charts visualizing team performance
3. Launches a Flask API to serve the data

---

## Technologies Used

- Python 3.x
- Requests – Fetch data from TheSportsDB API
- SQLite3 – Local database storage
- Pandas – Data manipulation
- NumPy – Array processing
- Matplotlib – Data visualization
- Flask – REST API

---

## Features

### Data Retrieval (`class Info`)
- `get_input()` – Prompts user for a season year (2010-2011 through 2024-2025)
- `get_stats(year)` – Fetches EPL table data from TheSportsDB API
- `panda(statistacs)` – Converts raw stats into a Pandas DataFrame

### Database Storage (`create_connection`)
- Creates SQLite database file `soccer_stats.db`
- Stores DataFrame as table named `stats`

### Data Visualization
- Generates 4 bar charts in a single figure:
  - Points per team
  - Wins per team
  - Losses per team
  - Goal Difference per team

### Flask API
- `GET /` – Returns HTML homepage with API description
- `GET /api/v1/soccer` – Returns JSON array of all top 5 teams data

---

## How to Run

### Prerequisites

```bash
pip install requests numpy pandas flask matplotlib

Step 1: Clone the repository
bash

git clone https://github.com/amanullahanis12-cmyk/python-2-final-api-db-backend-data-processing-.git
cd python-2-final-api-db-backend-data-processing-

Step 2: Run the program
bash

python final.py

Step 3: Enter a season

When prompted, enter a season in the format YYYY-YYYY

Valid seasons from the code:

    2010-2011 through 2016-2017

    2017-2018 through 2024-2025

Example:
text

What seasons do you want to see the top five teams in the table 2023-2024

Step 4: View outputs

The program will:

    Fetch data from TheSportsDB API

    Display the raw JSON response

    Create soccer_stats.db database

    Show 4 bar charts (matplotlib window opens)

    Start a Flask server at http://127.0.0.1:5000

Step 5: Use the API

Once the server is running:
Endpoint	Method	Description
http://127.0.0.1:5000/	GET	HTML homepage
http://127.0.0.1:5000/api/v1/soccer	GET	JSON data of top 5 teams
API Response Example
json

[
  {
    "Teams": "Manchester City",
    "Points": 91,
    "Wins": 28,
    "Loss": 3,
    "GoalDiff": 62
  }
]

File Structure
text

python-2-final-api-db-backend-data-processing/
├── final.py           # Main application
├── soccer_stats.db    # SQLite database (created at runtime)
└── README.md          # This file

Known Limitations

    API key (123) is hardcoded in the code

    Only the top 5 teams are processed

    Season input validation only accepts specific year ranges

    Flask server runs with debug=True

Academic Honesty Statement
text

I attest that this is my original work.
I have not used unauthorized source code, either modified or unmodified.
— Amanullah Anis

Future Improvements

    Add more seasons

    Allow user to choose number of teams

    Add error handling for API failures

    Save charts as image files
