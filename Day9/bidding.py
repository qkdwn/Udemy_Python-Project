# TODO-1 : Ask the user for input
name = input("이름을 입력하세요: ")
price = int(input("입찰할 가격을 입력하세요: $"))

bids = {}
# TODO-2: Save data into dictionary {name: price}
bids[name] = price
# TODO-3: Whether if new bids need to be added
should_continue = input("추가로 입찰할 사람이 있나요? 있다면 'yes', 없다면 'no'를 입력해주세요: \n")

continue_bidding = True
while continue_bidding:
    name
# TODO-4: Compare bids in dictionary