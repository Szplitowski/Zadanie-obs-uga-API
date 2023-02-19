from flask import Flask, render_template, request

app = Flask(__name__)


currencies = {
    "USD": "4.5283",
    "AUD": "3.1093",
    "CAD": "3.365",
    "EUR": "4.8286",
    "HUF": "0.012572",
    "CHF": "4.888",
    "GBP": "5.4257",
    "JPY": "0.033707",
    "CZK": "0.2038",
    "DKK": "0.6483",
    "NOK": "0.44",
    "SEK": "0.432",
    "XDR": "6.0353",
}


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        waluta = request.form["waluta"]
        val = float(request.form["val"])
        kurs = float(currencies[waluta])
        result = round(val * kurs, 2)
    return render_template("glowna.html", currencies=currencies, result=result)


if __name__ == "__main__":
    app.run(debug=True)
