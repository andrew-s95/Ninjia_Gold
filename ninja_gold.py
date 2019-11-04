from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

app.secret_key = "Ninja Gold"

@app.route('/')
def game():
    session['ninja_gold']={
    "farm":random.randint(10,21),
    "cave":random.randint(5,11),
    "house":random.randint(2,5),
    "casino":random.randint(-50,51)
    }
    if "counter" not in session:
        session["counter"] = 0
    if 'total_points' not in session:
        session['total_points'] = 0
        print (f"Total points is set")
    if "activities" not in session: 
        session["activities"] = ""
    return render_template("index.html")

@app.route('/process_money', methods = ["post"])
def process_money():
    print(f"Total points is {session['total_points']}")
    location = request.form["location"]
    points = session['ninja_gold'][location]
    session['total_points'] += points
    
    session['counter'] += 1
    # if session['counter'] == 5:
    #     session['activities'] = "<p>dahodihwado</p>"

    if session['counter'] > 15: 
        print("hi")
        session['activities'] = "<h1>You Suck!!!</h1>"
        return redirect('/')
        
    elif session['total_points'] >= 500 and session['counter'] <= 15:
        session['activities'] = "<h1>You Win</h1>" 
        return redirect('/')

    if points > 0:
        session["activities"] = "<p class='green'>You earned money " + str(points) + " at " + location + "</p>" + session["activities"]
    else:
        session["activities"] = "<p class='red'>You lost money " + str(points) + " at " + location + "</p>" + session["activities"]
    session.pop('ninja_gold')
    return redirect("/")

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

