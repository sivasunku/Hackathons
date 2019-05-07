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


iProfit =  list(map(int, input().rstrip().split()))
iPrice  =  list(map(int, input().rstrip().split()))
iCap = int(input())

remCapacity = iCap - sum(iPrice)
mtimes = remCapacity // min(iPrice)

names = ['A','B','C'] * mtimes
profits = iProfit * mtimes
prices = iPrice * mtimes
foods = buildMenu(names, profits, prices)

val = testMaxVal(foods, remCapacity)
Total = val + sum(iProfit)
print(Total)
