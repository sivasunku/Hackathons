

class Food(object):
    def __init__(self, n, profit, price):
        self.name = n
        self.profit = profit
        self.price = price
    def getProfit(self):
        return self.profit
    def getPrice(self):
        return self.price
    def __str__(self):
        return self.name + ': <' + str(self.profit)\
                 + ', ' + str(self.price) + '>'

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu
#
#def maxVal(toConsider, avail):
#    """Assumes toConsider a list of items, avail a weight
#       Returns a tuple of the total value of a solution to the
#         0/1 knapsack problem and the items of that solution"""
#    if toConsider == [] or avail == 0:
#        result = (0, ())
#    elif toConsider[0].getCost() > avail:
#        #Explore right branch only
#        result = maxVal(toConsider[1:], avail)
#    else:
#        nextItem = toConsider[0]
#        #Explore left branch
#        withVal, withToTake = maxVal(toConsider[1:],
#                                     avail - nextItem.getCost())
#        withVal += nextItem.getValue()
#        #Explore right branch
#        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
#        #Choose better branch
#        if withVal > withoutVal:
#            result = (withVal, withToTake + (nextItem,))
#        else:
#            result = (withoutVal, withoutToTake)
#    return result
#
#def testMaxVal(foods, maxUnits, printItems = True):
#    print('Use search tree to allocate', maxUnits,
#          'calories')
#    val, taken = maxVal(foods, maxUnits)
#    print('Total value of items taken =', val)
#    if printItems:
#        for item in taken:
#            print('   ', item)




def fastMaxVal(toConsider, avail, memo = {}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    #print("Function:",memo,avail)
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getPrice() > avail:
        #Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 fastMaxVal(toConsider[1:],
                            avail - nextItem.getPrice(), memo)
        withVal += nextItem.getProfit()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

def testMaxVal(foods, maxUnits, algorithm=fastMaxVal, printItems = True):
    #print('Menu contains', len(foods), 'items')
    #print('Use search tree to allocate', maxUnits,
    #      'calories')
    val, taken = algorithm(foods, maxUnits)
    return val
  
names = ['A','B','C'] * 30
profits = [5,10,15] * 30
prices = [10,20,25] * 30
foods = buildMenu(names, profits, prices)

print('')
testMaxVal(foods, 245)

def knapSack(W , wt , val , n): 
    print("Came here",W,wt,val,n)
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 
          
#for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
#    items = buildLargeMenu(numItems, 90, 250)
#    testMaxVal(items, 750, fastMaxVal, True)
