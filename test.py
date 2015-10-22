def changeslow(coins,amount):
        coins_used = [[None]]*len(coins)
        if amount in coins:
            coins_used[coins.index(amount)] = 1
            return coins_used
        else:
            min_coins = float("inf")
            for j in range(1,amount):
                num_coins1 = num_coins2 = [[None]]*len(coins)
                num_coins1 = changeslow(coins,j)
                num_coins2 = changeslow(coins,amount-j)
                print "printing numcoins1"+ str(num_coins1)
                print "printing numcoins1"+str(num_coins2)
                #print("j=" + str(j) + "n1 = "+str(num_coins1)+" n2="+str(num_coins2))
                coin_count1 = sum(num_coins1)
                coin_count2 = sum(num_coins2)
                coin_count = coin_count1+coin_count2
                if coin_count < min_coins:
                    min_coins = coin_count
                    coins_used = [a + b for a, b in zip(num_coins1, num_coins2)]
            return min_coins
        print coins_used
        print min_coins

V=[1,2,3]
A=5
print V
print A
changeslow(V,A)