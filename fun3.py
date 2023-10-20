def solve(numheads, numlegs):
    rabbit = (numlegs-2*numheads)/2
    chicken = numheads - rabbit
    print("rabbit:", rabbit, "chicken:", chicken)