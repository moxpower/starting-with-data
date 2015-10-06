from flask import Flask, Response
import json
import urllib2

app = Flask(__name__)

@app.route('/')
def test():
    return 'Everything is running!'

@app.route('/projects/highpoverty/states')
def high_poverty_states():
#    donors_choose_url = "http://api.donorschoose.org/common/json_feed.html?highLevelPoverty=true&APIKey=DONORSCHOOSE"
#    response = urllib2.urlopen(donors_choose_url)
#    json_response = json.load(response)
#### insert json from GaBi
    json_response=df.to_json
    states = set()
#### check original json_response structure    
    for proposal in json_response["proposals"]:
        states.add(proposal["state"])

#### maybe I can dump the json directly.
    return json.dumps(list(states))


if __name__ == '__main__':
    app.run()
