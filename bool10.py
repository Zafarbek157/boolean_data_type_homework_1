def chek_perfect_square(a):
    if a>=0:
        sqrt_a=int(a**0.5)
        return sqrt_a*sqrt_a==a
    else:
        return False
    print(chek_perfect_square(16)) # true
    print(chek_perfect_square(25)) # true
    print(chek_perfect_square(10)) #false
    print(chek_perfect_square(-4)) # false