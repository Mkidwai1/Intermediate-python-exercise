def main():
    total = 0
    count = 1
    while count<6:
        try:
            add = int(input("Enter int #" + str(count) + ": "))
            total+=add
            count+=1
        except ValueError:
            add =int(input("INVALID INPUT. Enter int #" + str(count) + ": "))
            total+=add
            count+=1
    print(total)
if __name__ == "__main__":
    main()