person = {"name": "Akansh", "age": 20, "city": "Faridabad"}
print("Person dictionary:", person)
print("\nName:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
person["email"] = "akansh@gmail.com"
print("\nDictionary after adding email:", person)
person["age"] = 26
print("\nDictionary after updating age:", person)
if "city" in person:
    print("\n'city' key exists in the dictionary")
keys = person.keys()
values = person.values()
print("\nAll keys:", list(keys))
print("All values:", list(values))