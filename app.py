from flask import Flask, render_template, request
import mod

app = Flask(__name__)
app.secret_key = "GuvfVfNGbcHygenZnfgreOynfgreFrpergXrl"

@app.route("/")
def hello_world():

    return render_template('app.html')

@app.route("/response", methods=["POST"])
def response():

    choice = request.form['options']
    text = str(request.form['input'])
    rtn_text = ""

    if choice == 'min':
        rtn_text += mod.minusculo(text)
    elif choice == 'mai':
        rtn_text += mod.maiusculo(text)
    elif choice == 'ran':
        rtn_text += mod.aleatorio(text)
    elif choice == 'ess':
        rtn_text += mod.esses(text)
    elif choice == 'cam':
        rtn_text += mod.camelo(text)
    elif choice == 'esp':
        rtn_text += mod.espaco(text)
    elif choice == 'mir':
        rtn_text += mod.espelho(text)
    elif choice == 'rot':
        rtn_text += mod.rot13(text)
    # print(f"Choice: {choice}. Text: {text}. Return: {rtn_text}")
    
    return rtn_text