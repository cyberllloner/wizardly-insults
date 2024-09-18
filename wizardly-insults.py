from requests import get

def generate_random_insult():
    response = get("https://insult.mattbas.org/api/insult")
    if response.status_code != 200:
        return "Unfortunately, now my creativity is lost, and I can't insult :)"
    else:
        random_insult = response.text
        return random_insult