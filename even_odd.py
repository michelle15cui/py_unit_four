def even_or_odd(number_1):
    number_1 = int(input("Please enter a number: "))
    if number_1 % 2 == 0:
        return(str(number_1) + " is a even number")
    if number_1 % 2 == 1:
        return(str(number_1) + " is a odd number")

def main():
    print(even_or_odd(11))
if __name__ == '__main__':
    main()