from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def start():
    answer = ""
    if (request.method == "POST"):
        grade = int(request.form["txtGrade"])
        if grade >= 70:
            answer = "Aprobado"
        else:
            answer = "Aprendizaje inicial"
    return render_template("index.html", answer = answer)

if __name__ == "__main__":
    app.run(debug=True)