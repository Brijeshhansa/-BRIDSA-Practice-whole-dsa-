a = 'Asymptotic Notation is a mathematical notation used in computer science and mathematics to describe the behavior of functions as their input values approach certain limits, such as infinity. It is particularly useful for analyzing and comparing the efficiency of algorithms and understanding how their performance scales with input size.'
b = '''Big O Notation (O()):

Represents an upper bound on the growth rate of a function or the worst-case time/space complexity.
It describes how the function's performance behaves in the worst-case scenario as the input size increases.
O(g(n)) means that the function's growth rate is at most proportional to g(n), up to a constant factor.
O(1) means constant time complexity (independent of input size).
O(log n) means logarithmic time complexity.
O(n) means linear time complexity.
O(n^2) means quadratic time complexity.
O(2^n) means exponential time complexity.'''
c = '''Omega Notation (Ω()):

Represents a lower bound on the growth rate of a function or the best-case time/space complexity.
It describes how the function's performance behaves in the best-case scenario as the input size increases.
Ω(g(n)) means that the function's growth rate is at least proportional to g(n), up to a constant factor.
Ω(1) means constant time complexity (best case).
Ω(log n) means logarithmic time complexity (best case).
Ω(n) means linear time complexity (best case).'''
d = '''Theta Notation (Θ()):

Represents both an upper bound and a lower bound on the growth rate of a function or the average-case time/space complexity.
It describes how the function's performance behaves in the average case as the input size increases.
Θ(g(n)) means that the function's growth rate is bounded both from above and from below by g(n), up to constant factors.
Θ(1) means constant time complexity (average case).
Θ(log n) means logarithmic time complexity (average case).
Θ(n) means linear time complexity (average case).'''

i=1
while(i!='12'):
    i=input('Enter a choice:\n0 to exit\n1 Big O Notation\n2 Omega Notation\n3 Theta Notation\n4 go to back menu\n-->\t')
    
    if(i=='1'):
        print(a)
        print(b)
    elif(i=='2'):
        print(a)
        print(c)
    elif(i=='3'):
        print(a)
        print(d)
    elif(i=='4'):
        i = 0
        print("these are the Asymptotic notations \n THANK YOU")
        break
    elif(i== '0'):
        mainloopchoice = '0'
        submainloopchoice = '0'
        i = '0'
        
        print('Thank you for using  Asymptotic Notation menu.\n @ BRIDSA \nCopyright 2023 - brijesh')
        break
    else:
        print('error')

