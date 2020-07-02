from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    champions = ['Aatrox', 'Annie', 'Ahri', 'Braum']
    return render_template('index.html', champions=champions)

@app.route('/Yourpage')
def yourpage():
    return render_template('PersonsPage.html')

if __name__=='__main__':
    app.run(debug=True)