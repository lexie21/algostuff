
def sum_of_subsets(i,wsum,rsum): 
    if wsum == M: #base case, print solution and return if sum M is found
                print(sol[1:]) #remove the inserted 0
                return
    if i < len(w)-1: 
        if is_expand(i,wsum,rsum):           
            sol[i+1] = 1 #since expandable means the next element (i+1) can be added, we add 1 to this position in sol
            sum_of_subsets(i+1, wsum+w[i+1],rsum-w[i+1])
        sol[i+1] = 0 #similar reasoning as above, not expandable so add 0 to index i+1 of sol
        sum_of_subsets(i+1,wsum,rsum-w[i+1])

def is_expand(i,wsum,rsum): #if returns False, prune the tree hereforth
    return ((wsum + rsum >= M) and ((wsum == M) or (wsum+w[i+1] <= M)))
# because of how we set these conditions, we cannot place both sum_of_subsets inside is_expand() 
# for if current wsum != M and the next node > M, the function just evaluates nothing and stops 
# even if subsequent items can form the desired sum. Ex: if the first item > M



if __name__ == '__main__':
    w = [3,34,4,12,5,2] 
    w.insert(0,0) #modify input m for the indexing to work
    M = 9
    sol = [0]*len(w) #initialize sol to hold solution
    sum_of_subsets(0,0,sum(w))
   
    