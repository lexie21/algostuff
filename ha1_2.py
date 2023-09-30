def min_stamp(stp,money):
    sol = {} #solution output
    for k in range(len(stp)-1,-1,-1): #iterate over all possible denominations
        if money >= stp[k]: #check for feasibility
            sol[stp[k]] = money//stp[k] #add to solution (denomination,#coin) to sol
            money %= stp[k] #compute remaining money
    return(sol)

if __name__ == "__main__":
    sta = input('Input stamps without bracket: ')
    bal = int(input('Input money: '))
    stamps = [int(i) for i in sta.split(',')]
    print([str(v)+' coin(s) of '+str(k)+'$' for k,v in min_stamp(stamps,bal).items()])
  

  