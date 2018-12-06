from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def strona_glowna():
    if request.method == 'POST':
        imie = request.form['imie']
        nazwisko = request.form['nazwisko']
        return render_template('projekt_1.html', imie=imie, nazwisko=nazwisko)
    return render_template('projekt_1.html')


if __name__ == "__main__":
    app.run(debug=True)
