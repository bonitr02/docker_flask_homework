from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    serum_albumin = 4.4
    serum_calcium = 9

    corrected_calcium = serum_calcium + 0.8 * (4 - serum_albumin)

    output = f'Hello from Flask App 2 \n Corrected Calcium calculator: {corrected_calcium}'
    return output


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5001
        )
