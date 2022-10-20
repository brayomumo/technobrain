'''

write a function that accepts a number and returns the number at that position in the Fibonacci sequence
fibonacci sequence [ 0,1,1,2,3,5,8,13,21,34]

sol(5) === 3

'''
def solution(num:int ):
    ''''
        formular for finding nth number in fibonacci sequence:
                Fn = Fn-1 + Fn-2
    '''

    count  = 0
    n1, n2 = 0,1
    while count < num+2:
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        if count == num-2: # num-2 since the first 2 are already defined
            return nth

        count += 1


assert solution(3) == 2
assert solution(5) == 5
assert solution(10) == 55
