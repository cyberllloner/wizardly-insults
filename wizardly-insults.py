from requests import get

def generate_random_insult():
    response = get("https://insult.mattbas.org/api/insult")
    if response.status_code != 200:
        return "Unfortunately, now my creativity is lost, and I can't insult :)"
    else:
        random_insult = response.text
        return random_insult

def add_text_border(text):
    dash = len(text) * "-"
    transformed_text = dash + "\n" + text + "\n" + dash
    return transformed_text

def main():
    text = add_text_border(generate_random_insult())
    wizard_ascii_art = r'''
    (\.   \      ,/)
    \(   |\     )/
    //\  | \   /\\
    (/ /\_#oo#_/\ \)
    \/\  ####  /\/
        `##'
    '''
    result = text + "\n" + wizard_ascii_art
    print(result)

main()