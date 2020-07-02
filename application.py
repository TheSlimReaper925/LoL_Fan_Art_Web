from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addpage')
def yourpage():
    champions = ['Aatrox', 'Annie', 'Ahri', 'Braum']
    return render_template('addpost.html', champions=champions)

if __name__=='__main__':
    app.run(debug=True)