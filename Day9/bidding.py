# TODO-1 : Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
#from day5.High_score import highest_score
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

bids = {}  # while 반복문 안에 있으면 반복할 때마다 이전 데이터를 모두 잃게 되기 때문에 밖으로 빼둔다.
continue_bidding = True

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while continue_bidding:
    name = input("이름을 입력해주세요: ")
    price = int(input("당신의 입찰가는?: "))
    bids[name] = price
    should_continue = input("추가로 입찰할 사람이 더 있나요? 있다면 'yes', 없다면 'no'를 입력해주세요..\n")
    if should_continue == "no":
      continue_bidding = False
      find_highest_bidder(bids)
    elif should_continue == "yes":
      print("\n" * 20)