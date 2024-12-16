# -*- coding: utf-8 -*-
"""
MATB25 Discrete Math, Programming Assignment

@authors: Ruth Risberg, Iman Ebrahimi
"""

# (a)
cols_a = 8
ans_a = ['\t\t'.join(['x1\tx2\tx3'] * cols_a)]
temp_a = []

# run for loops for each variable in the range where they could create a solution
for x1 in range(11):
    for x2 in range(11 - x1):
        temp_a.append(str(x1) + '\t' + str(x2) + '\t' + str(10 - x1 - x2))

        # start a new line when the desired number of columns have been filled
        if len(temp_a) == cols_a:
            ans_a.append('\t\t'.join(temp_a))
            temp_a = []
print('\n'.join(ans_a))

# (b)
cols_b = 6
ans_b = ['\t\t'.join(['x1\tx2\tx3\tx4'] * cols_b)]
temp_b = []

# run for loops for each variable in the range where they could create a solution
for x1 in range(-2, 11):
    for x2 in range(-2, 9 - x1):
        for x3 in range(-2, 7 - x1 - x2):
            temp_b.append(
                str(x1) + '\t' + str(x2) + '\t' + str(x3) + '\t' +
                str(4 - x1 - x2 - x3))

            # start a new line when the desired number of columns have been filled
            if len(temp_b) == cols_b:
                ans_b.append('\t\t'.join(temp_b))
                temp_b = []

# print the solutions to part b
print('\n'.join(ans_b))

#Task 2
""""
#The following function s_t (commented) is based on the definition 
of Stirling Number.
Obviously, this wasn't asked by the assignment. 
We used it to compare the outcomes which resulted from the recursive function 
with those of the original definition.
"""

"""
def s_t(m, n):
    summ = 0
    for k in range(n + 1):
        nChooseK = (factorial(n)) / ((factorial(n - k)) * (factorial(k)))
        elt = ((-1)**k) * nChooseK * ((n - k)**m)
        summ += elt
    return (summ / factorial(n))

"""
#Part a)

#A Function To Calculate the Stirling Number using the Recursive Method.
def stir_rec(m, n):
    #Shifting the index m: S(m,n) = S(m-1,n-1) + nS(m-1,n)
    if n == 1 or m == n:
        return 1

    stir_sum = stir_rec(m - 1, n - 1) + n * stir_rec(m - 1, n)
    return stir_sum


#Part b) 
def stir_quotient(m, n):
    return stir_rec(m, n) / (m + n)


print("The output of stir_quotient(12,5) = ", stir_quotient(12, 5))
print("The output of stir_quotient(13,8) = ", stir_quotient(13, 8))

