# Json to python Conversion
import json

# some JSON:
x = '{ "name":"Tom", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])
print(y)
print("---------------------------------------------------")
# **************************************************

# a Python object (dict):
x = {
    "name": "Ram",
    "age": 30,
    "city": "Mumbai"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print("JSON Data: - ", y)

# ---------------------------------------------------
print("-------Convert Python objects into JSON strings, and print the values:----------------------")
print(json.dumps({"name": "Pomo", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("-------Convert a Python object containing all the legal data types into Json:----------------------")

x = {
  "name": "Gomes",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "Tata 230", "mpg": 27.5},
    {"model": "Ford ", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True))
print("---------------------------------------------------")
print(json.dumps(x, indent=4, separators=(". ", " = ")))