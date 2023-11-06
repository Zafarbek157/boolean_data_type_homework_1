def main(a):
    if a>=0:
        sqrt_a=int(a**0.5)
        return sqrt_a*sqrt_a==a
    else:
        return False
    print(main(16)) # true
    print(main(25)) # true
    print(main(10)) #false
    print(main(-4)) # false