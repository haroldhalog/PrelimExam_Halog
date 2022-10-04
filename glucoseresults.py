from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def glucoseINformation():

    return {'Results'}

if __name__ == '__main__':
    app.run()
    