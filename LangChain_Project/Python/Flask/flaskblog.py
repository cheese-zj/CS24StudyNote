from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route("/qa", methods=['GET', 'POST'])
def qa():
    if request.method == 'POST':
        question = request.form['question']
        answer = process_question(question) 

        # pass the value to template
        return render_template('answer.html', question=question, answer=answer)

    return render_template('qa.html')

def process_question(question):
    return "收到收到"

if __name__ == '__main__':
    app.run(debug=True)
