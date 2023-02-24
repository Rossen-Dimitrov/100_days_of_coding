from blind_auction_logo import logo


def winner(bidders):
    high_name = ""
    high_bid = 0
    for key in bidders:
        if bidders[key] > high_bid:
            high_name = key
            high_bid = bidders[key]
    print(f"The winner is {high_name} with a bid of ${high_bid}")


print(logo)

bidders_dict = {}

while True:
    name = input("What is your name\n")
    bidd = int(input("Enter you bid\n"))

    bidders_dict[name] = bidd

    other_bidder = input("Are there any other bidders? Type 'y or 'n'.\n")
    if other_bidder == "n":
        winner(bidders_dict)
        break