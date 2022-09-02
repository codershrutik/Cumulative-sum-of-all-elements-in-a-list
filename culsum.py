my_list = [44,4345,435,4565,6768,23]

initial_val = 0

cumsum = []

for i in my_list:
    initial_val += i
    cumsum.append(initial_val)

print('The cumulative sums of the list', cumsum)