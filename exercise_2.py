def main():
    def get_combined_dict(my_dict_1, my_dict_2):
        combined_dict={}
        for key1 in my_dict_1:
            for key2 in my_dict_2:
                if (key1 == key2):
                    add = my_dict_1[key1] + my_dict_2[key2]
                    combined_dict[key1] = add
        return combined_dict
                
    
    my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
    my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
    combined_dict = get_combined_dict(my_dict_1, my_dict_2)
    print(combined_dict)
if __name__ == "__main__":
    main()