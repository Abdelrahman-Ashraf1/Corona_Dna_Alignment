# Python3 program to find the most
# frequent element in an array.

def mostFrequent(arr, n):
    # Sort the array
    arr.sort()

    # find the max frequency using
    # linear traversal
    max_count = 1;
    res = arr[0];
    curr_count = 1

    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            curr_count += 1

        else:
            if (curr_count > max_count):
                max_count = curr_count
                res = arr[i - 1]

            curr_count = 1

    # If last element is most frequent
    if (curr_count > max_count):
        max_count = curr_count
        res = arr[n - 1]

    return res


files = ["seq (1)_edited.txt", "seq (2)_edited.txt", "seq (3)_edited.txt", "seq (3)_edited.txt", "seq (4)_edited.txt",
         "seq (5)_edited.txt", "seq (6)_edited.txt", "seq (7)_edited.txt", "seq (8)_edited.txt", "seq (9)_edited.txt",
         "seq (10)_edited.txt"]



d = {}
for x in range(len(files)):
    with open(files[x], 'r') as f:
        d["string{0}".format(x)] = f.read()

# for z in range(10):
#     print(len(d["string{0}".format(x)]))

first_letter_of_each_coloumn_of_sequences = []
for y in range(29744):
    for x in range(len(d)):
        seq = d["string{0}".format(x)]
        first_value = seq[y]
        first_letter_of_each_coloumn_of_sequences.append(first_value)
    print(mostFrequent(first_letter_of_each_coloumn_of_sequences, 10) , end='')
    first_letter_of_each_coloumn_of_sequences.clear()


