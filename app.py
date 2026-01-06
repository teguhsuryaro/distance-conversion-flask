from flask import Flask, render_template, request

app = Flask(__name__)

# Konversi ke meter sebagai basis
conversion_to_meter = {
    # SI units
    "km": 1000,
    "hm": 100,
    "dam": 10,
    "m": 1,
    "dm": 0.1,
    "cm": 0.01,
    "mm": 0.001,

    # Imperial units
    "inch": 0.0254,
    "feet": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    value = None
    from_unit = None
    to_unit = None


    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        value_in_meter = value * conversion_to_meter[from_unit]
        result = value_in_meter / conversion_to_meter[to_unit]

    return render_template(
        "index.html",
        result = round(result, 4),
        value=value,
        from_unit=from_unit,
        to_unit=to_unit
    )

if __name__ == "__main__":
    app.run(debug=True)
