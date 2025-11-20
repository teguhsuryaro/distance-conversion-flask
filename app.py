from flask import Flask, render_template, request

app = Flask(__name__)

# Konversi ke meter sebagai basis
conversion_to_meter = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        # Step 1: ubah ke meter dulu
        value_in_meter = value * conversion_to_meter[from_unit]

        # Step 2: Ubah dari meter ke satuan tujuan
        result = value_in_meter / conversion_to_meter[to_unit]

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
