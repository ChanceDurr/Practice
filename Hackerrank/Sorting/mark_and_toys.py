"""
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.
Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example,
if prices = [1,2, 3, 4] and Mark has k = 7 to spend, he can buy items [1, 2, 3] for 6, or [3, 4] for 7 units of currency. He would choose the first group of 3 items.
"""

def maximumToys(prices, k):
    prices.sort()
    spent = 0
    bought = 0
    
    for toy in prices:
        if toy < k - spent:
            bought += 1
            spent += toy
        else:
            return bought

    return bought

