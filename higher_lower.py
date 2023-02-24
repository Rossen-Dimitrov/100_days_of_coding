from game_data import data
from art import logo, vs
from random import choice


def get_random_account():
    """Get random account from data"""
    return choice(data)


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
  and returns True if they got it right.
  Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


print(logo)
account_b = get_random_account()
score = 0

you_win = True
while you_win:

    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
        account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    account_a_count = account_a['follower_count']
    account_d_count = account_b['follower_count']

    is_true = check_answer(guess, account_a_count, account_d_count)

    clear()
    if is_true:
        score += 1
        print(f"You're right! Current {score}: 1.")
    else:
        print(f"Sorry, that's wrong. Final {score}:.")
        you_win = False
