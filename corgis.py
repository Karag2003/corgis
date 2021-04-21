from flask import Flask, url_for, render_template, request, Markup

import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route('/funFact')  
def render_fun_fact():
    if "state" in request.args:
        state_chosen = request.args['state']
        return render_template('location.html', options=get_state_options(), funFact=fun_fact_by_state(state_chosen))
    else:
        return render_template('location.html', options=get_state_options())

def get_state_options():
    listOfStates = [] #makes an empty list
    with open('real_estate.json') as real_estate_data:
        counties = json.load(real_estate_data)
    for county in counties:
        if not(county["location"]["address"]["state"] in listOfStates):
            listOfStates.append(county["location"]["address"]["state"])
        
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options
    
def fun_fact_by_state(state):
    listOfAddress = []
    with open('real_estate.json') as estate_data:
        counties = json.load(estate_data)
    for county in counties:
        if county["location"]["address"]["state"] == state:
            listOfAddress.append (county["location"]["address"]["line 1"])
    random = Markup("<p>Here are the properties within ") + state + Markup("</p><ul>")
    
    for address in listOfAddress:
        random = random + Markup("<li>" + address + "</li>")
    return random + Markup("</ul>")
        
        
if __name__=="__main__":
    app.run(debug=True)
