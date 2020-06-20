from flask import Flask, request,render_template
app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html')



@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/reserve')
def reserve():
	return render_template('reserve.html')
	


if __name__ == "__main__":
    app.debug = True
    app.run()