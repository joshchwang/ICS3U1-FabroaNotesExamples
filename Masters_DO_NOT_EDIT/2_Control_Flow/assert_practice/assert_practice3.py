def love6(a,b):
    if(a== 6 or b == 6 or a+b == 6 or a-b==6 or b-a ==6):
        return(True)
    else:
        return(False)
assert(love6(6,5))== True
assert(love6(10,4))== True
assert(love6(3,2))== False
assert(love6(2,4))== True