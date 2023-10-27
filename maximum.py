def max(num_1, num_2):
    if num_1 > num_2:
        return(num_1, "is bigger than ", num_2)
    else:
        return(num_2, " is bigger than ",num_1)



def main():
    print( max(7, 19))

main()