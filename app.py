from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        nama = request.form.get('nama')
        nim  = request.form.get('nim')
        return render_template("output.html",
        namamhs = nama,
        nimmhs  = nim)


if __name__ == "__main__":
    app.run()