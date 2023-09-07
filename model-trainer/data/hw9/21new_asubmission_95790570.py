def input_tracker(number):
    string_list = []
    input_dict={}
    for i in range(number):
#@#
        user_inp = input("Please enter an object to be counted: ")
        string_list.append(user_inp)
    for i in string_list:
        input_dict[i]=string_list.count(i)
    return(input_dict)
#@#
def main():
if __name__ == '__main__':
    main()
#@#