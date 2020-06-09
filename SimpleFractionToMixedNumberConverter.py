'''
https://www.codewars.com/kata/556b85b433fb5e899200003f/train/python

Given a string representing a simple fraction x/y, your function must return a string representing the 
corresponding mixed fraction in the following format:

[sign]a b/c

where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c. 
Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional 
part must be provided absolute).

If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. 
In both of these cases, the resulting string must not contain any spaces.

Division by zero should raise an error (preferably, the standard zero division error of your language).
Value ranges

    -10 000 000 < x < 10 000 000
    -10 000 000 < y < 10 000 000

Examples

    Input: 42/9, expected result: 4 2/3.
    Input: 6/3, expedted result: 2.
    Input: 4/6, expected result: 2/3.
    Input: 0/18891, expected result: 0.
    Input: -10/7, expected result: -1 3/7.
    Inputs 0/0 or 3/0 must raise a zero division error.

Note

Make sure not to modify the input of your function in-place, it is a bad practice.
'''
def mixed_fraction(s):
    from fractions import Fraction
    print(s)
    n,d = s.split('/')
    n = int(n)
    d = int(d)
    if(n!=d):
        if((n>0 and d>0) or (n<0 and d<0)):
            n = abs(n)
            d = abs(d)
            resto_da_divisao = n%d
            parte_inteira = n//d
            quociente = n - (parte_inteira * d)
            fracao_simplificada_diferente = Fraction(quociente,d)
            fracao_simplificada = Fraction(n,d)
            if(resto_da_divisao == 0):
                return str(parte_inteira)
            elif(resto_da_divisao!=0 and n>d):
                return str(parte_inteira) + ' ' + str(fracao_simplificada_diferente)
            elif(parte_inteira == 0 and n<d):
                return str(fracao_simplificada)
        elif(n<0 and d>0 or n>0 and d<0):
            n = -1* n
            d = -1*d
            resto_da_divisao = n%d
            parte_inteira = n//d
            quociente = n - (parte_inteira * d)
            fracao_simplificada_diferente = Fraction(quociente,d)
            fracao_simplificada = Fraction(n,d)
            if(resto_da_divisao == 0):
                return str(-1 * parte_inteira)
            elif(resto_da_divisao!=0 and n>d):
                return str(-1 * parte_inteira) + ' ' + str(fracao_simplificada_diferente)
            elif(parte_inteira == 0 and n<d):
                return str(-1 * fracao_simplificada)
        elif(n==0 or d==0):
            return str(int(n/d)) 
    else:
        if(n==0 and d ==0):
            return str(int(n/d))
        else:
            return '1'
