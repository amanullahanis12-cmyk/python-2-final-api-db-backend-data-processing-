"""
* Name         : final.py
* Author       : Amanullah Anis
* Created      : 7/25/2025
* Module       : final
* Topic        : final
* Description  : Retrieves information about top five soccer teams in the English Premier League based on the season which is used as a parameter and then makes a DB,
                    four graphs, and send information to an api after creating one.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""  
import requests 
import json
import sqlite3
from sqlite3 import Error
import numpy as np
import pandas as pd
import flask
from flask import request, jsonify
import matplotlib.pyplot as plt
class Info:
    def get_input(self):
        loopy = True
        while loopy:
            year = input("What seasons do you want to see the top five teams in the table ")
            if year == '2010-2011' or year == '2011-2012' or year == '2012-2013' or year == '2013-2014' or year == '2014-2015' or year == '2015-2016' or year == '2016-2017':
                loopy = False
                return year
            elif year == '2017-2018' or year == '2018-2019' or year == '2019-2020' or year == '2020-2021' or year == '2021-2022' or year == '2022-2023' or year == '2023-2024' or year == '2024-2025':
                loopy = False
                return year
                
    def get_stats(self, year):
    #2010-2011 earliest btw
        response = requests.get(f"https://www.thesportsdb.com/api/v1/json/123/lookuptable.php?l=4328&s={year}")
        pythoned_json = json.loads(response.text)
        print(pythoned_json)
        teams = np.arange(5,0)
        points = np.arange(5,0)
        wins = np.arange(5,0)
        losses = np.arange(5,0)
        gdifference = np.arange(5,0)
        for item in pythoned_json['table']:
            teams = np.append(teams, [[item['strTeam']]])
        for item in pythoned_json['table']:
            points = np.append(points, [[item['intPoints']]])
        for item in pythoned_json['table']:
            wins = np.append(wins, [[item['intWin']]])
        for item in pythoned_json['table']:
            losses = np.append(losses, [[item['intLoss']]])
        for item in pythoned_json['table']:
            gdifference = np.append(gdifference, [[item['intGoalDifference']]])
        statistacs = np.array([[teams], [points], [wins], [losses], [gdifference]])
        statistacs = np.transpose(statistacs)    
        statistacs = np.reshape(statistacs, (5,5))
        return statistacs
    def panda(self, statistacs):
        stats = pd.DataFrame(statistacs, columns=['Teams','Points','Wins','Loss','GoalDiff'])
        stats['Points'] = stats['Points'].astype('Int64')
        stats['Wins'] = stats['Wins'].astype('Int64')
        stats['Loss'] = stats['Loss'].astype('Int64')
        stats['GoalDiff'] = stats['GoalDiff'].astype('Int64')
        return stats
def main(service: Info):
    service = Info()
    year = service.get_input()
    statistacs = service.get_stats(year)
    stats = service.panda(statistacs)
    return stats
def create_connection(db_file):
    """ create a database connection to the SQLite database
    specified by db_file
:param db_file: database file
:return: Connection object or None
"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

        return conn
    
if __name__ == "__main__":
    app = flask.Flask(__name__)    
    service = main(service=Info())
    
    
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    database = 'soccer_stats.db'
    conn = create_connection(database)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    service.to_sql(name='stats',con=conn, if_exists='replace')    
    all_books = cur.execute('SELECT * FROM stats;').fetchall()
    @app.route('/', methods=['GET'])
    def home():
        return '''<h1>EPL Top 5 Teams</h1>
    <p>An API that returns a list of top 5 teams in EPL based on season.</p>'''

    @app.route('/api/v1/soccer', methods=['GET'])
    def api_all():
        
        

        return jsonify(all_books)
    plt.rcParams['figure.autolayout']=True
    fig, axs = plt.subplots(1,4)
    axs[0].bar(service['Teams'], service['Points'])
    axs[0].set_xticklabels(service['Teams'],rotation=90,ha='right')
    axs[0].title.set_text('Points')
    axs[1].bar(service['Teams'], service['Wins'])
    axs[1].set_xticklabels(service['Teams'],rotation=90,ha='right')
    axs[1].title.set_text('Wins')
    axs[2].bar(service['Teams'], service['Loss'])
    axs[2].set_xticklabels(service['Teams'],rotation=90,ha='right')
    axs[2].title.set_text('Loss')
    axs[3].bar(service['Teams'], service['GoalDiff'])
    axs[3].set_xticklabels(service['Teams'],rotation=90,ha='right')
    axs[3].title.set_text('Goal Difference')
    plt.show()
    app.run(debug=True, use_reloader = False)
    print(service)
    