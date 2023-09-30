import sys

def minCoins(coins, y):
    m = len(coins)
    #initialize table with every single money value from 0 to y
    table = [sys.maxsize for i in range(y+1)]
    #base case (if given value y = 0)
    table[0] = 0

    # for i in range(1, y+1):
    #     table[i] = sys.maxsize
    for i in range(1, y+1): #increment through each value up to y, find the min #coins for each 
        for j in range(m): #go through all the coin denominations
            if coins[j] <= i:
                sub_res = table[i-coins[j]] #optimal solution of subproblem 
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1 #update if current #coins is larger than sub_res + 1
    return table[y]

if __name__ == '__main__':
    coins = [1,10,21,34,70,100,350,1225,1500]
    y = 140
    print('Minimum coins required is',minCoins(coins,y))