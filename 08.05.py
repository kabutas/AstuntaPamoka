# Create a program that allows a user to enter a series of numbers, and then calculates the average of all the numbers.
# The program should also print the list of all the numbers, as well as the average.

num_series_string = input("Enter series of numbers: ")
num_series_seperated = (num_series_string.split(sep=" "))
float_list = []

for i in num_series_seperated:
    if i != "":
        float_list.append(float(i))

print(f"You entered numbers: {float_list}\nAverage number was: {round(sum(float_list) / len(float_list), 2)}")
