import json
import uuid

from flask import Flask, jsonify, request

app = Flask(__name__)

patients = [
            {'Id': str(uuid.uuid4()), 'Name': 'Ash', 'Age': 25, 'Symptoms': ['Fever', 'Cold']},
            {'Id': str(uuid.uuid4()), 'Name': 'Misty', 'Age': 24, 'Symptoms': ['Knee pain']}
        ]


@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(patients)


@app.route("/patients/<id>", methods=["DELETE"])
def delete_patients(id):
    index = -1
    for i in range(0, len(patients)):
        if patients[i]['Id'] == id:
            index = i
            break
    if index != -1:
        patients.pop(index)
        return '', 200
    else:
        return '', 404


@app.route("/patients", methods=["POST"])
def create_patient():
    patient = json.loads(request.data)
    patient['Id'] = str(uuid.uuid4())
    patients.append(patient)
    return jsonify(patient)


@app.route("/patients/<id>", methods=["PUT"])
def update_patient(id):
    patient = json.loads(request.data)
    index = -1
    for i in range(0, len(patients)):
        if patients[i]['Id'] == id:
            index = i
            break
    if index != -1:
        patient['Id'] = id
        patients[index] = patient
        return jsonify(patient)
    else:
        return '', 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8082, debug=True)
