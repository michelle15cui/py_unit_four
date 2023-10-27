def is_triangle(a, b, c):
    if a >= (b + c) or b >= (a + c) or c >= (a + b):
        print("No, it can't be a triangle")
    else:
        print("Yes! it can be a triangle!")
    pass



def main():
    a = int(input("Please enter the length for the first stick: "))
    b = int(input("Please enter the length for the second stick:"))
    c = int(input("Please enter the length for the third stick:"))
    is_triangle(a, b, c)
    pass


if __name__ == '__main__':
    main()

