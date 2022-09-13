from replit import clear
from art import logo
print(logo)
bids = {}
end_game = False

def highest_bid(bidding_amount):
  high_bid = 0
  winner = ""
  for bidder in bidding_amount:
    bid_money = bidding_amount[bidder]
    if bid_money > high_bid:
      high_bid = bid_money
      winner = bidder
  print(f"Winner is {winner} with the bid of ${high_bid}")
    
while not end_game:
  name = input("What is your Name? \n")
  price = int(input("Write your Price: $"))
  bids[name] = price
  next = input("is there anyone left? if yes the type = 'Yes' otherwise type = 'No'").lower()
  if next == "no":
    end_game = True
    highest_bid(bids)
  elif next == "yes":
    clear()
