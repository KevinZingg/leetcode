import json
from mymodule import person_kevin
from mymodule import person1

x = '{ "name":"Anna", "age":17, "city":"Stäfa"}'

parsed_local = json.loads(x)

print(parsed_local)
print(parsed_local["name"])

parsed_import = json.loads(person_kevin)

print(parsed_import)
print(parsed_import["city"])

parsed_import_dict = json.dumps(person1)
print(parsed_import_dict)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
