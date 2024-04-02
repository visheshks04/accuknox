from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    data = {
        "Student 1": [77,66,85,99,76],
        "Student 2": [77,55,85,99,76],
        "Student 3": [67,76,34,64,77],
        "Student 4": [78,76,88,44,66],
        "Student 5": [54,57,66,74,77],
        "Student 6": [88,58,62,86,95],
        "Student 7": [55,86,37,37,44],
    }

    return jsonify(data)



if __name__ == '__main__':
    app.run(debug = True)
