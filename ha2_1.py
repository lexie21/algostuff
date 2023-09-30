def lis(arr):
    max_lst = []
    n = len(arr)
    #initialize 2-row table, h[0] holds length of lis thus far 
    #and h[1] holds each item's predecessor
    h = [[1]*n, [-1]*n]

    #update table
    for i in range(1,n): 
        for j in range(0,i):
            if arr[i] > arr[j] and h[0][i] < h[0][j] + 1:
                h[0][i] = h[0][j] + 1 #update length
                h[1][i] = j #assign predecessor

    max_length = max(h[0]) 
    
    #trace LIS in descending order
    for i in range(n-1,-1,-1):
        if h[0][i] == max_length and h[1][i] > -1: #h[1][i] > -1 to avoid appending the "predecesor" of the smallest item
            if len(max_lst) == 0: #append the last/biggest item of lis
                max_lst.append(arr[i])
            max_lst.append(arr[h[1][i]]) #the next array item to be appended is indexed by the current's h[1]
            max_length = h[0][h[1][i]] #update max_length to be the length of the current item's predecessor 


    return max_lst[::-1] #reverse order to become LIS, time complexity is always O(n) regardless of state of input

if __name__ == '__main__':
    arr = [10,22,9,33,21,50,41,60]
    result = lis(arr)
    print('LIS is',result)
    print('Length of LIS is',len(result))
