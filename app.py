from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/adlib', methods=['POST'])
def adlib():
    if request.method == 'POST':
        noun1 = request.form['noun1']
        noun2 = request.form['noun2']
        verb1 = request.form['verb1']
        verb2 = request.form['verb2']
        adjective1 = request.form['adjective1']
        adjective2 = request.form['adjective2']

        return render_template('adlib_result.html', noun1=noun1, noun2=noun2, verb1=verb1, verb2=verb2, adjective1 = adjective1, adjective2 = adjective2)

if __name__ == '__main__':
    app.run(debug=True)
