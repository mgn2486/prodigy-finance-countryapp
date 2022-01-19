import  requests

BASE = "http://127.0.0.1:5000/"

# populate three countries
data = [{"name":"South-Africa","alpha2code":"027","alpha3code":"27","currency":"Rand" },
    {"name":"Zimbabwe","alpha2code":"02637","alpha3code":"63","currency":"ZimDollar" },
    {"name":"Botswana","alpha2code":"0265","alpha3code":"65","currency":"Pula" }]

# request all countries 
for i in range(len(data)):
    response = requests.put(BASE + "country/"+str(i), data[i])
    print(response.json())

input()
# look for a non existing record
response = requests.delete(BASE + "country/7")
print(response)

input()
# soft delete a country by id
response = requests.delete(BASE + "country/0")
print(response)
input()
# get a country by id
response = requests.get(BASE + "country/2")
print(response.json())