li = [
  {
    "roll": 0,
    "mark": 0,
    "userName": "string",
    "email": "string",
    "personDetails": {
      "fullName": "string",
      "fatherName": "string",
      "motherName": "string",
      "brotherName": "string",
      "sisterName": "string",
      "maritalStatus": {
        "maritalStatus": "string",
        "relation": "string"
      }
    }
  },
  {
    "roll": 1,
    "mark": 0,
    "userName": "string",
    "email": "string",
    "personDetails": {
      "fullName": "string",
      "fatherName": "string",
      "motherName": "string",
      "brotherName": "string",
      "sisterName": "string",
      "maritalStatus": {
        "maritalStatus": "string",
        "relation": "string"
      }
    }
  }
]
for i, value in enumerate(li):
  if(value["roll"]==1):
    index = i
print(li[index])

