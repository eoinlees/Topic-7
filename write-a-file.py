# Eoin Lees
# How to write to a file

#Note - W writes to a new file each time deleting the origional.
#Note - a appends new text to file keeping origional. 
with open('myfile.txt', 'a') as f:
    print(f.tell())
    f.write("\nHello from the First Line again!\n")
    print(f.tell())
