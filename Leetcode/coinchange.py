def coinChange(coins, amount):
    coin_map = {}
    if amount == 0:
        return 0
    lval = min(coins)

    def dfs(amt):
        cl = []
        for c in coins:
            la = amt - c
            if la == 0:
                cl.append(0)
            elif la >= lval:
                if la in coin_map:
                    if coin_map[la] != -1:
                        cl.append(coin_map[la])
                else:
                    coin_map[la] = dfs(la)
                    if coin_map[la] != -1:
                        cl.append(coin_map[la])
        if not cl:
            return -1
        return min(cl) + 1
    return dfs(amount)
    
coins = [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422]
print(coinChange(coins, 9864))
