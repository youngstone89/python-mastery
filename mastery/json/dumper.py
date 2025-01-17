import json

# Creating a dictionary
Dictionary ={1:'김', 2:'to',
			3:'영', 4:'for',
			5:'Geeks'}

# Converts input dictionary into
# string and stores it in json_string
json_string = json.dumps(Dictionary, ensure_ascii=False)
print('Equivalent json string of input dictionary:',
	json_string)
print("	 ")

# Checking type of object
# returned by json.dumps
print(type(json_string))

json_back = json.loads(json_string)
print(json_back)

