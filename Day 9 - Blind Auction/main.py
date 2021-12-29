from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

option = 'yes'
bidder_info = {}
highest_bid = 0
winner = ' '
list = []
while option == 'yes':
    
    name = input("What is your name?:")
    bid_amount = int(input("What is your bid?: $"))
    #if bid_amount > highest_bid:
    #    highest_bid = bid_amount
    #    winner = name
    bidder_info[bid_amount] = name
    #bidder_info[name] = bid_amount
    option = input("Are there any other bidders?")
    clear()
#dictionary cannot take index directly
#solution that not using for loop, exchange name as value and amount as key (by the way, there is a flaw, if more than one user key in same amount, it will get the latter user as winner, while using original solution/Angela solution, it will get the former user) question, what is the rule of the secret auction? is the first to bid get win or the second? if is the first, then my exchange solution is wrong, else is ok to use this
#also there is flaw, if names key in are the same, should be validate for it

highest_bid= max(bidder_info.keys())
winner = bidder_info[highest_bid]

#values = bidder_info.values()
#print(values)
#winner = keys[values.index(highest_bid)]

print(f"The winner is {winner} with a bid of ${highest_bid}")