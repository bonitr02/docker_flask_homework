from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/bonitr02/flask_5_tailwind/main/plans.csv')
@app.route('/')
def index(data=df):
    data = data.sample(30)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
        )