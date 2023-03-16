import requests

def process_comment(comment):
    response  = requests.get("https://profane.azurewebsites.net/profane/"+comment)
    processed = response.json()['cleantext']
    return processed