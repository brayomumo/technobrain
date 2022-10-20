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
    n_1 = num - 1
    n_2 = num - 2
    f_n = n_1 + n_2

    return f_n

print(solution(5))