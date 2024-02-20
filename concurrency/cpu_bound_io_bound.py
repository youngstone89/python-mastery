import requests

response = requests.get('https://www.example.com')  # io bound

items = response.headers.items()  # cpu bound

headers = [f'{key}: {header}' for key, header in items]  # cpu bound

formatted_headers = '\n'.join(headers)  # cpu bound

with open('headers.txt', 'w') as file:  # io bound
    file.write(formatted_headers)
