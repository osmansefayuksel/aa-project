def getWays(amount, coinTypes):
    
    dp = [0] * (amount + 1)
    dp[0] = 1 
 
   
    for coin in coinTypes:
        
        for i in range(coin, amount + 1):
            
            dp[i] += dp[i - coin]
 
    return dp[amount]




print("Ways : ", getWays(3, [8, 3, 1, 2]))


#Output: Ways :  3
    



# This algorithm uses dynamic programming approach to solve the coin change problem. 

# Worst case time complexity: O(amount * n)

# Best case time complexity: O(amount * n) 

# Average case time complexity: O(amount * n)

# The big-O notation describes the upper bound of the time complexity of an algorithm, which means that the algorithm will take no more than O(amount * n) steps in the worst case, best case, and average case.
# The big-Ω notation describes the lower bound of the time complexity of an algorithm, which means that the algorithm will take at least Ω(amount * n) steps in the best case.
# The big-Θ notation describes the exact time complexity of an algorithm, which means that the algorithm will take Θ(amount * n) steps in the average case.

