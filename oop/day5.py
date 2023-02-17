import requests  
response = requests.get('https://www.google.com/search?client=opera-gx&q=https%3A%2F%2Fgoogle.com&sourceid=opera&ie=UTF-8&oe=UTF-8') 
  
print(response) 
print(f'Time: {response.elapsed}')