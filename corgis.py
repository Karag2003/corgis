from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route('/funFact')  
def render_fun_fact():
    state_chosen = request.args['state']
    return render_template('location.html', options=get_state_options(), funFact=fun_fact_by_state(state_chosen))
    
def get_state_options():
    listOfStates = [] #makes an empty list
    with open('real_estate.json') as real_estate_data:
        counties = json.load(real_estate_data)
    for county in counties:
        if not(county["State"] in listOfStates):
            listOfStates.append(county["State"])
        
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options
    
def fun_fact_by_state(state):
    with open('real_estate_data') as estate_data:
        counties = json.load(estate_data)
    first_county = "ZZZZZZZ"
    for county in counties:
        if county["County"] < first_county and county["State"] == state:
            first_county = county["County"]
    return "In alphabetical order " + first_county + " comes up first!"






    
if __name__=="__main__":
    app.run(debug=False)
