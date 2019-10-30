def date_fashion(you: int, date: int) -> int:
    """Return fashion values based on you and your date
    
    Arguments:
        you {int} -- your fashion value
        date {int} -- fashion value of your date
    
    Returns:
        int -- [description]
    """

    if (you <= 2 or date <= 2):
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1


assert date_fashion(5, 10) == 2
assert date_fashion(5, 2) == 0
assert date_fashion(5, 5) == 1
