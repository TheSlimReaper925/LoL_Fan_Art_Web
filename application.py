from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/addpage', methods=['GET', 'POST'])
def yourpage():
    champions = ['Aatrox', 'Annie', 'Ahri', 'Ashe', 'Braum']
    if request.method == 'POST':
        champion = request.form['ChampionSelect']
        nickname = request.form['Name']
        image = request.files['Image']
        imageB = image.read()
        return champions[int(champion)] + ' ' + nickname
    return render_template('addpost.html', champions=champions)


if __name__ == '__main__':
    app.run(debug=True)
