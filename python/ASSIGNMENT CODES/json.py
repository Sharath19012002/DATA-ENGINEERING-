# Import JSON module
import json

# Define JSON string
jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'

# Convert JSON String to Python
student_details = json.loads(jsonString)

# Print Dictionary
print(student_details)
# Print values using keys
print(student_details['name'])
print(student_details['course'])

# Python program to demonstrate
# Conversion of JSON data to
# dictionary

import json

# Sample data to write to the JSON file
data_to_write = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "isStudent": False
}

# Specify the file name
json_file_name = 'data.json'

# Write data to the JSON file
with open(json_file_name, 'w') as json_file:
    json.dump(data_to_write, json_file, indent=2)  # indent is optional for pretty formatting

print(f"Data has been written to {json_file_name}")

import json

# JSON-formatted string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON string to Python dictionary
python_dict = json.loads(json_string)

# Display the resulting Python dictionary
print(python_dict)

import json

# Specify the JSON file name with double backslashes or a raw string
json_file_name = r"C:\Users\Sumedha\PycharmProjects\pythonProject\example.json"

# Read JSON data from file and convert it to Python object
with open(json_file_name, 'r') as json_file:
    python_object = json.load(json_file)

# Display the resulting Python object (dictionary in this case)
print(python_object)

import json

# Nested JSON-formatted string
nested_json_string = '''
{
  "name": "John",
  "age": 30,
  "address": {
    "city": "New York",
    "zipcode": "10001"
  },
  "courses": ["Math", "Physics", "Computer Science"]
}
'''

# Convert nested JSON string to Python dictionary
nested_dict = json.loads(nested_json_string)

# Display the resulting Python dictionary
print(nested_dict)