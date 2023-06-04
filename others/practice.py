def test():
    for i in range(10):
        print(i)
    print()

    for i in range(5, 10):
        print(i)
    print()

    for i in range(0, 9, 2):
        print(i)
    print()

    for i in range(100, 69, -3):
        print(i)
    
def cal():
    sum = 0
    for i in range(10):
        number = float(input("please enter a number: "))
        if number == 0:
            break
        sum += number
    
    print(f"sum is: {sum}")



if __name__ == "__main__":
    test()
