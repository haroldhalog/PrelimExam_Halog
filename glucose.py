from flask import Flask, jsonify, request
app = Flask(__name__)
glucose_info=[
    {
        "glucose_id" : "0111222333",
        "glucose_date" : ["07,14,2000"],
        "glucose" : ["1"]
        
    },
    {
        "glucose_id" : "0111222444",
        "glucose_date" : ["07,14,2005"],
        "glucose" : ["2"]
    }
    
]

@app.route('/glucose_info', methods=['GET'])
def GLucoseInformation():
    return jsonify(glucose_info)

if __name__ == '__main__':
    app.run()