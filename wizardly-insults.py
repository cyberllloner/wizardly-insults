import requests
from textwrap import fill

def generate_random_insult():
    response = requests.get("https://insult.mattbas.org/api/insult")
    if response.status_code != 200:
        return "Unfortunately, now my creativity is lost, and I can't insult :)"
    else:
        return response.text

def style_text(value):
    return "\nOne Message From The Great Wizard:\n\n" + f'\033[1m"{fill(value, width=50)}"\033[0m'

def main():
    insult = style_text(generate_random_insult())
    wizard_ascii_art = '''
    (\.   \      ,/)
    \(   |\     )/
    //\  | \   /\\
    (/ /\_#oo#_/\ \)
    \/\  ####  /\/
        `##'
    '''
    print(insult + "\n" + wizard_ascii_art)

if __name__ == "__main__":
    main()