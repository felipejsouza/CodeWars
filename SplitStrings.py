'''
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character of the final
pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''

def solution(s):
    old_string = list(s)
    new_string = []
    x = 0
    if len(s)%2 == 0 and len(s)!=1:
      while(x<len(s)):
        aux = old_string[x] + old_string[x+1]
        new_string.append(aux)
        x+=2
      return new_string
    elif len(s) %2 == 1 and len(s)!=1:
      while(x<(len(s)-1)):
        aux = old_string[x] + old_string[x+1]
        new_string.append(aux)
        x+=2
        print(x, len(s))
        if (len(s) - x == 1):
          aux = old_string[x] + '_'
          new_string.append(aux)
      return new_string
    elif len(s) == 1:
      aux = old_string[0] +'_'
      new_string.append(aux)
      return new_string
    else:
      return new_string
