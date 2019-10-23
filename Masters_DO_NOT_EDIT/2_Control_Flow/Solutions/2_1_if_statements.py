

def cigar_party(cigars: int, is_weekend: bool) -> bool:
    """When squirrels get together for a party, they like to have cigars. 
    A squirrel party is successful when the number of cigars is between 40
    and 60, inclusive. Unless it is the weekend, in which case there is 
    no upper bound on the number of cigars. Return True if the party with the
    given values is successful, or False otherwise.

    
    Arguments:
        cigars {int} --  number of cigars
        is_weekend {bool} -- flag to determine if weekend

    Returns:
        bool -- whether the party was a success
    """

    if (40 <= cigars and cigars <= 60) and not(is_weekend):
        # check non-weekend condition
        return True

    elif is_weekend and cigars > 40:
        # weekend condition
        return True

    else:
        return False


# Call the function to test
assert(cigar_party(30, False))
assert(cigar_party(50, False))
assert(cigar_party(20, True))
assert(cigar_party(70, True))
assert(cigar_party(90, False))
