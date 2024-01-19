def main():
    input_string = input("Enter your string: ")
    def get_dict_string(string):
        remove_space = string.replace(" ","")
        dictionary = {}
        for char in remove_space:
            if char in dictionary:
                dictionary[char] +=1
            else:
                dictionary[char] =1
        return dictionary  
    final_string = get_dict_string(input_string)
    print(final_string)
if __name__ == "__main__":
    main()