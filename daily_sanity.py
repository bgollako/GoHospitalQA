from requests import get, post, delete, patch
from json import dumps


def test_get_patients():
    url = 'http://localhost:8082/v1/Patients'
    response = get(url=url)
    if response.status_code == 200:
        print('GET Patients completed')
        patients = response.json()
        print('Found {0} patients'.format(len(patients)))
    else:
        print('GET Patients failed with status code {0}'.format(str(response.status_code)))


# This method creates patients
def test_post_patients():
    url = 'http://localhost:8082/v1/Patients'
    patients = dumps([{'name':'Kishore', 'age':33, 'disease':'back pain'},{'name':'Kiran', 'age':31, 'disease':'shoulder pain'}])
    response = post(url=url, data=patients)
    if response.status_code == 200:
        print('Created 2 patients')
    else:
        print('Patients creation failed with status code {0}'.format(str(response.status_code)))


# This method deletes patients that were created by the above post patients method
def test_delete_patients():
    del_url = 'http://localhost:8082/v1/Patients?id={0}'
    get_url = 'http://localhost:8082/v1/Patients'
    response = get(url=get_url)
    ids = []
    if response.status_code == 200:
        patients = response.json()
        if len(patients) == 0:
            print('No patients found')
            return
        for patient in patients:
            if patient.get('name') == 'Kiran' or patient.get('name') == 'Kishore':
                ids.append(patient['id'])
        for i in ids:
            response = delete(del_url.format(i))
            if response.status_code == 200:
                print('Deleted patient with id {0}'.format(i))
            else:
                print('Patient deletion failed with status code {0}'.format(str(response.status_code)))


# This method increments the created patients age by 2
def test_update_patient():
    update_url = 'http://localhost:8082/v1/Patients?id={0}'
    get_url = 'http://localhost:8082/v1/Patients'
    response = get(url=get_url)
    update_patients = []
    if response.status_code == 200:
        patients = response.json()
        if len(patients) == 0:
            print('No patients found')
            return
        for patient in patients:
            if patient.get('name') == 'Kiran' or patient.get('name') == 'Kishore':
                update_patients.append(patient)
        for p in update_patients:
            p['age'] += 2
            i = p.pop('id')
            response = patch(update_url.format(i), dumps(p))
            if response.status_code == 200:
                print('Updated patient with id {0}'.format(i))
            else:
                print('Patient updation failed with status code {0}'.format(str(response.status_code)))


def main():
    test_get_patients()
    test_post_patients()
    test_update_patient()
    test_delete_patients()


if __name__ == '__main__':
    main()