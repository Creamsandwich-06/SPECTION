import requests


def send(to, text):
    api_key = "2CpKIQww7XedNpZQpBIWy5ciKUx"
    api_secret = "KSfyMXNQxgLpbsEaATJVBSdhL6dEWVCX9wH2eqQv"

    company = 'Spection Co.'
    payload = "api_key="+api_key+"&api_secret=" + \
        api_secret+"&to="+to+"&text="+text+'&from='+company
    headers = {
        'accept': "application/json",
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request(
        "POST", "https://api.movider.co/v1/sms", data=payload, headers=headers)

    print(response.text)
