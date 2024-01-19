def main():
    def unique_list(input_list):
        uniqueList = list(set(input_list))
        return uniqueList
    tempList =[]
    open = True
    while(open):
        list_add = (input("Enter a number to add to the list. type QUIT to stop : "))
        if( list_add == "QUIT"):
            open = False
        else:
            tempList.append(int(list_add))
    final_list = unique_list(tempList)
    print(final_list)
if __name__ == "__main__":
    main()