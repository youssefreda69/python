x = eval(input("please enter how many codes you want to be generated: "))
count = 0
while count < x :
    import time 
    time.sleep(1)
    import random
    value=random.uniform(1,1000000)
    from datetime import datetime
    now = datetime.now()
    seed = value*(int(now.strftime("%S")))
    def rng(m=3, a=5, c=9):
        global seed
        seed = (a*seed + c) % m
        return seed/m
    print(rng())
    count = count + 1
    