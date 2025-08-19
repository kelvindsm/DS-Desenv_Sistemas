from flask import Flask

app = Flask(__name__)


@app.route('/')
def cs():  # put application's code here
    return 'Central de Serviços'


if __name__ == '__main__':
    app.run()
