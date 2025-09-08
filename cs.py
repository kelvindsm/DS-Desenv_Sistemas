from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def cs():
    return render_template('index.html')


@app.route('/menu_adm')
def menu_adm():
    return render_template('menu_adm.html')


@app.route('/menu_pre')
def menu_pre():
    return render_template('menu_pre.html')


@app.route('/menu_sol')
def menu_sol():
    return render_template('menu_sol.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
