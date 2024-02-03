# file1 = open("alteredfiles/text.txt", "r")
# print(file1.read())
# file1.close()

# file2 = open("alteredfiles/text.txt", "a")
# file2.write("\n\nThis is a new line")
# file2.close()

# file3 = open("alteredfiles/text.txt", "w")
# file3.write("I have overwritten the file!")
# file3.close()

#copying files
newfilename = input("Enter a name for the new file: ")
newfile = open("alteredfiles/" + newfilename + ".txt", "w")
file1 = open("alteredfiles/text.txt", "r")
newfile.write(file1.read())
newfile.close()
