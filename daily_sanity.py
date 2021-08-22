from requests import get, post, put, delete
from json import dumps

patient_url = 'http://localhost:8082/patients'

test_case_table = {
    'Get Patients': False,
    'Add Patient': False,
    'Update Patient': False,
    'Delete Patient': False
}


# get_patients fetches the patients from the given url and checks against the given expected_patient_count
# updates the test_case_table if is_test_case is true
# Returns the list of patients if the request was successful
def get_patients(expected_patient_count: int, is_test_case: bool):
    resp = get(patient_url)
    if resp.status_code != 200:
        print('failed to fetch patients with status code {0}'.format(resp.status_code))
        return
    if len(resp.json()) != expected_patient_count:
        print('expected {0} patients found {1} patients'.format(expected_patient_count, len(resp.json())))
        return
    if is_test_case:
        test_case_table['Get Patients'] = True
    return resp.json()


def add_patient():
    new_patient = {"Name": "Tom", "Age": 70, "Symptoms": ["Knee Pains", "Back Pains"]}
    resp = post(patient_url, data=dumps(new_patient))
    if resp.status_code != 200:
        print('failed to create patient with status code {0}'.format(resp.status_code))
        return
    if get_patients(3, False) is not None:
        test_case_table['Add Patient'] = True


def update_patient():
    updated_patient = {"Name": "Tom", "Age": 70, "Symptoms": ["Knee Pains", "Back Pains", "Ankle Pain"]}
    patients = get_patients(3, False)
    for patient in patients:
        if patient['Name'] == 'Tom':
            resp = put('/'.join([patient_url, patient['Id']]), data=dumps(updated_patient))
            if resp.status_code != 200:
                print('failed to update patient with status code {0}'.format(resp.status_code))
                return
            test_case_table['Update Patient'] = True
            break


def delete_patient():
    patients = get_patients(3, False)
    for patient in patients:
        if patient['Name'] == 'Tom':
            resp = delete('/'.join([patient_url, patient['Id']]))
            if resp.status_code != 200:
                print('failed to delete patient with status code {0}'.format(resp.status_code))
                return
            if get_patients(2, False) is not None:
                test_case_table['Delete Patient'] = True
            break


if __name__ == '__main__':
    get_patients(2, True)
    add_patient()
    update_patient()
    delete_patient()
