# GoHospitalQA

### Setup steps
1. Run "git clone git@github.com:bgollako/GoHospital.git"
2. Run "go run main.go" inside the cloned repo
3. The apis will be available on http://localhost:8082

### Available APIs

* Get All Patients
    - URL : http://localhost:80/v1/Patients
    - Method : GET
* Delete Patient
    - URL : http://localhost:80/v1/Patients?id=patient_id
    - Method : DELETE
    - Example : http://localhost:80/v1/Patients?id=5c6da1cbc98edcc2a14ed703
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
    - URL : http://localhost:80/v1/Patients?id=patient_id
    - Method : PATCH
    - Body : {
             	"name":"Sherlock",
             	"age":24,
             	"disease":"Diabetes"
             }
            
