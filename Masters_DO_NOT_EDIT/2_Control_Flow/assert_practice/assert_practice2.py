def alarm_clock(day,vacation):
    if(day<6 and day > 0 and vacation == False):
        return("7:00")
    elif(day==0 or day==6) and vacation == False:
        return("10:00")
    elif(day<6 and day >0 and vacation == True):
        return("10:00")
    elif(day==0 or day==6 and vacation == True):
        return("off")
assert(alarm_clock(4,True))== "10:00"
assert(alarm_clock(5,False))=="7:00"
assert(alarm_clock(6,False))=="10:00"
assert(alarm_clock(0, True)) == "off"