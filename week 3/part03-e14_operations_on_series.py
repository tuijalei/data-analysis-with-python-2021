import pandas as pd
import numpy as np

#  gets two lists of numbers as parameters, lists should have length 3
#  first creates two Series, s1 and s2
#  
def create_series(L1, L2):
    s1 = pd.Series(L1, index = list('abc'))
    s2 = pd.Series(L2, index = list('abc'))
    return (s1, s2)

#  gets two Series as parameters
#  adds to the first Series s1 a new value with index d (same as the value in Series s2 with index b)
#  deletes the element from s2 that has index b
def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    return (s1, s2)
    
def main():
    L_1 = list('123')
    L_2 = list('345')
    s1, s2 = create_series(L_1, L_2)
    mod1, mod2 = modify_series(s1, s2)
    print(s1, s2)
    print(mod1 + mod2)
    
if __name__ == "__main__":
    main()
