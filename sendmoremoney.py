import time
start = time.time() # timer to see how fast it works
list = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for s in list: # starting from the first letter
    if(s == 0): 
        continue
    for e in list:
        if(e == s): 
            continue
        for n in list:
            if(n == s)|(n == e): 
                continue
            for d in list:
                if(d == s)|(d == e)|(d == n): 
                    continue
                for m in list:
                    if(m == 0): 
                        continue
                    if(m == s)|(m == e)|(m == n)|(m == d): 
                        continue
                    for o in list:
                        if(o == s)|(o == e)|(o == n)|(o == d)|(o == m):
                            continue
                        for r in list:
                            if(r == s)|(r == e)|(r == n)|(r == d)|(r == m)|(r == o): 
                                continue
                            for y in list:
                                if(y == s)|(y == e)|(y == n)|(y == d)|(y == m)|(y == o)|(y == r): 
                                    continue
                                send = s*1000 + e*100 + n*10 + d
                                more = m*1000 + o*100 + r*10 + e 
                                money = m*10000 + o*1000 + n*100 + e*10 + y
                                if(send + more) != money:
                                     continue
                                print('(SEND: {}) + (MORE: {}) = (MONEY: {})'.format(send, more, money)) # send more money in digits
print('Time (in s):', time.time() - start) # average 8sec in vsc terminal, average 4sec in google colab