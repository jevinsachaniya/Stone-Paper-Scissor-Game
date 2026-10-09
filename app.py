from flask import Flask, render_template, request, url_for, redirect, session
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jevin1681'
CHOISE = ["Rock", "Paper", "Scissors"]

EMOJI = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

@app.route("/", methods=["POST", "GET"])
def game():
    if request.method == "POST":
        computer_choise = random.choice(CHOISE)
        user_choise = request.form.get("user_choise")

        if user_choise == computer_choise:
            result = "draw"
            message = "It's a Draw! 😀"
        elif (user_choise == "Rock"     and computer_choise == "Scissors" or
              user_choise == "Scissors" and computer_choise == "Paper"    or
              user_choise == "Paper"    and computer_choise == "Rock"):
            result = "won"
            message = "You Won! 🎉"
        else:
            result = "lost"
            message = "You Lost! 😞"

        session['result']          = result
        session['message']         = message
        session['user_choise']     = user_choise
        session['computer_choise'] = computer_choise
        return redirect(url_for('resultpage'))

    return render_template("index.html")


@app.route("/resultpage", methods=["GET"])
def resultpage():
    result          = session.get('result', 'draw')
    message         = session.get('message', '')
    user_choise     = session.get('user_choise', '')
    computer_choise = session.get('computer_choise', '')
    return render_template("result.html",
                           result=result,
                           message=message,
                           user_choise=user_choise,
                           computer_choise=computer_choise,
                           emoji=EMOJI)


@app.route("/playagain", methods=["POST"])
def playagain():
    return redirect(url_for("game"))


# if __name__ == "__main__":
#     app.run(debug=True)
