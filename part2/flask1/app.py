from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mathstuff = 7 + 8
    output = f'Flask App 1 - Math output {mathstuff}'
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
