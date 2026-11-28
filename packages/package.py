import requests

#pip install requests
#pip install ipykernel
# Jupyter > Interactive Window > Text Editor: Execute Selection


response = requests.get("https://api.github.com")
print(response)