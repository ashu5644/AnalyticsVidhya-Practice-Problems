from flask import Flask, request, render_template, redirect, url_for
from process_input import func

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    sent = "#people aren't protesting #trump because a #republican won-they do so because trump has fuhered  &amp;â¦"
    ans = int(float(func(sent)))
    if ans==1:
        return "+ve"
    else:
        return "-ve"

@app.route("/submit", methods=["POST","GET"])
def submit():
    if request.method=="POST":
        sent = request.form['sentence']
        #sent = "#people aren't protesting #trump because a #republican won-they do so because trump has fuhered  &amp;â¦"
        ans = int(float(func(sent)))
        
        final_ans = ""
        if ans==1:
            final_ans = "+ve"
        else:
            final_ans =  "-ve"
        return render_template('index.html', sent=sent, ans=final_ans)
    



if __name__=='__main__':
    app.run(debug=True)