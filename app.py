import os
import json

from espnff import League 
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

app = Flask(vashi-fantasybot)

@app.route('https://git.heroku.com/vashi-fantasybot.git', methods=['POST'])
def webhook():
	data = request.get_json()

	if data['name'] != 'fantasyTester' and data['text'] = 'scoreboard':
		bot_id = os.environ.get("FF-GM-ID")
   		league_id = os.environ.get("ESPN-ID")
    	year = 2017
		msg = get_scoreboard(league_id, year)
		send_message(msg)


def get_scoreboard(league_id, year):
    '''Gets current week's scoreboard'''
    league = League(league_id, year)
    matchups = league.scoreboard()
    score = ['%s %s - %s %s' % (i.home_team.team_abbrev, i.home_score,
             i.away_score, i.away_team.team_abbrev) for i in matchups   
             if i.away_team]
    text = ['Score Update'] + score
    return '\n'.join(text)

def send_message(msg):
	url = 'https://api.groupme.com/v3/bots/post'
	data = {
			'bot_id' : os.environ.get('FF-GM-ID')
			'text' : msg
	}