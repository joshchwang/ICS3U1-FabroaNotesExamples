def caught_speeding(speed: int, is_birthday: bool) -> int:
    """Indicate whether a speeding ticket should be distributed

    Arguments:
        speed {int} -- speed of driver
        is_birthday {bool} -- whether it is the driver's birthday

    Returns:
        int -- 0 = no ticket, 1 = small ticket, 2 = big ticket
    """
    if is_birthday:
        if speed > 85:
            return 2
        elif 66 <= speed <= 85:
            return 1
        else:
            return 0
    else:
        if speed > 80:
            return 2
        elif 61 <= speed <= 80:
            return 1
        else:
            return 0


assert caught_speeding(60, False) == 0
assert caught_speeding(65, False) == 1
assert caught_speeding(65, False) == 1