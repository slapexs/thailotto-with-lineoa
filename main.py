import requests

url_api = "https://lotto.api.rayriffy.com/latest"

res = requests.get(url_api).json()['response']
date = res['date']
prizes = res['prizes']

input_number = ""
while len(input_number) != 6:
    input_number = input("Enter number: ")
    if len(input_number) < 6:
        print(f"Please enter all 6 numbers {6 - len(input_number)} more missing")
    elif len(input_number) > 6:
        print(f"Sorry your number's more then 6 unit")
    else:
        pass


def Checklotto(number:str):
    isWon = False
    for i in range(len(prizes)):
        if number in prizes[i]['number']:
            isWon = i

    if isWon != False:
        return f"You won!! {prizes[isWon]['name']} - Reward:{prizes[isWon]['reward']}"
    else:
        return f"Sorry is not your time, GG Go next"
        
print(Checklotto(input_number))

