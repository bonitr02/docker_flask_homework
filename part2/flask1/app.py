from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    WBC = 11000
    Neutrophils = 30
    Bands = 3

    calculatedOutcome = ((Neutrophils + Bands)/ 100) * WBC
    output = f'Flask App 1 - ANC Calculator Results: {calculatedOutcome}'
    return output

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5002
        )
