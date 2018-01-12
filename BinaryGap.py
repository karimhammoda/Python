'''
Created on Jul 8, 2017

@author: karim hammouda
'''
def solution(N):
    
    #convert N to its binary representation
    binary_rep = bin(N)[2:]
    
    #initialize operating parameters
    max_binary_gap = 0
    start_counting = False
    counter = 0
    
    #loop for each bit on binary representation
    for dig in binary_rep:
        
        #End state: right hand one => calculate results
        if(dig == '1' and start_counting):
            max_binary_gap = max(counter, max_binary_gap)
            counter = 0;
        
        #Start state: left hand one => initialize counting
        elif(dig == '1' and not start_counting):
            start_counting = True
            
        #Intermediate state: inner zeros => counting
        elif(dig == '0' and start_counting):
                counter +=1
    
    return max_binary_gap


def main():
    print(bin(991892)[2:])
    print(solution(991892))


if __name__ == '__main__':
    main()
