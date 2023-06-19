def standard_deviation():
    # to store numbers that entered by user
    list_of_user_inputs = []

    # to store the values that comes after subtracting data value with average
    data_value_minus_average = []

    squared = []

    end_word = "end"

    while True:
        user_input = input("Enter a number to know the standard deviation: ")

        if user_input == end_word:
            print("Thanks for using std.dev calculator!")

            break
        else:
            list_of_user_inputs.append(float(user_input))

        user_input_avg = sum(list_of_user_inputs) / len(list_of_user_inputs)

        for i in list_of_user_inputs:
            data_value_minus_average.append(i - user_input_avg)

        for i in data_value_minus_average:
            squared.append(i * i)

        print("The std_dev is ", math.sqrt(sum(squared)/len(squared)))