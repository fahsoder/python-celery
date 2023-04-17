from tasks import add
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    result = add.delay(4, 4)
    return f'Resultado: {result.id}'


if __name__ == '__main__':
    app.run(debug=True)