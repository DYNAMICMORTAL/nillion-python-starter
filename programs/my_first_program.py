from nada_dsl import *

def nada_main():
    parties = [Party(name=f"Party{i+1}") for i in range(5)]
 
    bids = [SecretInteger(Input(name=f"bid_{party.name}", party=party)) for party in parties]
    max_limits = [SecretInteger(Input(name=f"max_limit_{party.name}", party=party)) for party in parties]

    valid_bids = [IfElse(bid <= max_limit, bid, max_limit) for bid, max_limit in zip(bids, max_limits)]

    highest_bid = SecretInteger(0)
    winner = SecretString("No winner")

    for i, bid in enumerate(valid_bids):
        is_higher = bid > highest_bid
        highest_bid = IfElse(is_higher, bid, highest_bid)
        winner = IfElse(is_higher, parties[i].name, winner)
    return [Output(highest_bid, "highest_bid", parties[0]), Output(winner, "winner", parties[0])]

