dictionary = dict()


with open("file3.txt") as f:
    for line in f:
        (lastname, firstname, age) = line.split()
        name = lastname + ' ' + firstname
        dictionary[age] = str(name)

sorted_dict = sorted(dictionary.items())  # list of tuples ('17', 'Hui Sosovich')

with open ("output3.txt", "w") as f:
    for elem in sorted_dict:
        f.write(str(elem[1]))
        f.write(' ')
        f.write(str(elem[0]))
        f.write('\n')