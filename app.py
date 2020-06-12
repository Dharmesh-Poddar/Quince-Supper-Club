from flask import Flask, request,render_template
app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.debug = True
    app.run()