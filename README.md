# GoHospitalQA

### Setup steps
1. Clone this repo
2. Run "docker-compose up" inside the cloned repo
3. The apis will be available on http://localhost:80
4. Press Ctrl+C to stop the containers.
5. After testing, run "docker-compose down --rmi local -v" to shutdown all the containers.

### Available APIs

* Get All Patients
    - URL : http://localhost:80/v1/Patients
    - Method : GET
* Delete Patient
    - URL : localhost:8082/v1/Patients?id=patient_id
    - Method : DELETE
    - Example : localhost:8082/v1/Patients?id=5c6da1cbc98edcc2a14ed703
* Post Patients
    - URL : http://localhost:80/v1/Patients
    - Method : POST
    - Body : [
             {
             	"name":"Sherlock",
             	"age":24,
             	"disease":"Diabetes"
             },
             {
             	"name":"Moriarty",
             	"age":22,
             	"disease":"Madness"
             }
             ]
* Update Patient
    - URL : localhost:8082/v1/Patients?id=patient_id
    - Method : PATCH
    - Body : {
             	"name":"Sherlock",
             	"age":24,
             	"disease":"Diabetes"
             }
            