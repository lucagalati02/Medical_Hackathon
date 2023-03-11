from flask import render_template, request, session, redirect, url_for
from DiagnosticAI import app
from DiagnosticAI import situation


@app.route('/', methods=["POST", "GET"])
def home():
    title = ""
    message = ""
    if request.method == "POST":
        if 'refresh' in request.form:
            return redirect(url_for('symptoms'))
        elif 'validate' in request.form:
            return render_template("home.html", title="", message="")
    else:
        title = ""
        message = ""
        return render_template("home.html", title=title, message=message)


@app.route('/symptoms', methods=["POST", "GET"])
def symptoms():
    title = "Patient Symptoms"
    message, correct_diagnosis = situation.situation()
    session['message'] = message
    session['correct_diagnosis'] = correct_diagnosis
    if request.method == "POST":
        if 'refresh' in request.form:
            return redirect(url_for('symptoms'))
        elif 'validate' in request.form:
            session['diagnosis_attempt'] = request.form['diagnosis_attempt']
            return redirect(url_for('results'))
    return render_template("home.html", title=title, message=message)


@app.route('/results', methods=["POST", "GET"])
def results():
    correct_diagnosis = session['correct_diagnosis']
    diagnosis_attempt = session['diagnosis_attempt']
    status = situation.diagnosing(correct_diagnosis, diagnosis_attempt)
    if status == "True":
        title = "Correct!"
        message = ""
        return render_template("home.html", title=title, message=message)
    else:
        title = "Incorrect!"
        message = "Correct diagnosis: " + correct_diagnosis
        return render_template("home.html", title=title, message=message)
