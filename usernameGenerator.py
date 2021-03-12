import argparse
__author__ = 'L0ng_'
 
parser = argparse.ArgumentParser(description='This is a script to generate possible usernames with first and last name. By L0ng_')
parser.add_argument('-i', '--input-file', help='File with list of names', required=True)
parser.add_argument('-o', '--output-file', help='Output file with usernames', required=False)
args = parser.parse_args()

# names = John Doe
inputFile = open(args.input_file, 'r')
names = inputFile.readlines()
inputFile.close()

usernameList = []

for fullName in names:
    nameArray = fullName.replace('\n', '').split(' ')
    first = nameArray[0].lower()
    last = nameArray[1].lower()

    ## first.last
    # john.doe
    name = "{first}.{last}".format(first=first, last=last)
    usernameList.append(name)

    # John.doe
    name = "{first}.{last}".format(first=first.capitalize(), last=last)
    usernameList.append(name)

    # john.Doe
    name = "{first}.{last}".format(first=first, last=last.capitalize())
    usernameList.append(name)

    # John.Doe
    name = "{first}.{last}".format(first=first.capitalize(), last=last.capitalize())
    usernameList.append(name)

    # JOHN.doe
    name = "{first}.{last}".format(first=first.upper(), last=last)
    usernameList.append(name)

    # john.DOE
    name = "{first}.{last}".format(first=first, last=last.upper())
    usernameList.append(name)

    # JOHN.Doe
    name = "{first}.{last}".format(first=first.upper(), last=last.capitalize())
    usernameList.append(name)

    # John.DOE
    name = "{first}.{last}".format(first=first.capitalize(), last=last.upper())
    usernameList.append(name)

    # JOHN.DOE
    name = "{first}.{last}".format(first=first.upper(), last=last.upper())
    usernameList.append(name)

    ## last.first
    # doe.john
    name = "{last}.{first}".format(first=first, last=last)
    usernameList.append(name)

    # doe.John
    name = "{last}.{first}".format(first=first.capitalize(), last=last)
    usernameList.append(name)

    # Doe.john
    name = "{last}.{first}".format(first=first, last=last.capitalize())
    usernameList.append(name)

    # Doe.John
    name = "{last}.{first}".format(first=first.capitalize(), last=last.capitalize())
    usernameList.append(name)

    # doe.JOHN
    name = "{last}.{first}".format(first=first.upper(), last=last)
    usernameList.append(name)

    # Doe.JOHN
    name = "{last}.{first}".format(first=first.upper(), last=last.capitalize())
    usernameList.append(name)

    # DOE.john
    name = "{last}.{first}".format(first=first, last=last.upper())
    usernameList.append(name)

    # DOE.John
    name = "{last}.{first}".format(first=first.capitalize(), last=last.upper())
    usernameList.append(name)

    # DOE.JOHN
    name = "{last}.{first}".format(first=first.upper(), last=last.upper())
    usernameList.append(name)

    ## first.l
    # John.d
    name = "{first}.{last}".format(first=first, last=last[0])
    usernameList.append(name)

    # John.D
    name = "{first}.{last}".format(first=first, last=last[0].upper())
    usernameList.append(name)

    # John.d
    name = "{first}.{last}".format(first=first.capitalize(), last=last[0])
    usernameList.append(name)

    # John.D
    name = "{first}.{last}".format(first=first.capitalize(), last=last[0].upper())
    usernameList.append(name)

    # JOHN.D
    name = "{first}.{last}".format(first=first.upper(), last=last[0].upper())
    usernameList.append(name)

    # JOHN.d
    name = "{first}.{last}".format(first=first.upper(), last=last[0])
    usernameList.append(name)

    ## last.f
    # doe.j
    name = "{last}.{first}".format(first=first[0], last=last)
    usernameList.append(name)

    # doe.J
    name = "{last}.{first}".format(first=first[0].upper(), last=last)
    usernameList.append(name)

    # Doe.j
    name = "{last}.{first}".format(first=first[0], last=last.capitalize())
    usernameList.append(name)

    # Doe.J
    name = "{last}.{first}".format(first=first[0].upper(), last=last.capitalize())
    usernameList.append(name)

    # DOE.j
    name = "{last}.{first}".format(first=first[0], last=last.upper())
    usernameList.append(name)

    # DOE.J
    name = "{last}.{first}".format(first=first[0].upper(), last=last.upper())
    usernameList.append(name)

    ## f.last
    # j.doe
    name = "{first}.{last}".format(first=first[0], last=last)
    usernameList.append(name)

    # J.doe
    name = "{first}.{last}".format(first=first[0].upper(), last=last)
    usernameList.append(name)

    # j.Doe
    name = "{first}.{last}".format(first=first[0], last=last.capitalize())
    usernameList.append(name)

    # J.Doe
    name = "{first}.{last}".format(first=first[0].upper(), last=last.capitalize())
    usernameList.append(name)

    # j.DOE
    name = "{first}.{last}".format(first=first[0], last=last.upper())
    usernameList.append(name)

    # J.DOE
    name = "{first}.{last}".format(first=first[0].upper(), last=last.upper())
    usernameList.append(name)

    ## l.first
    # d.john
    name = "{last}.{first}".format(first=first, last=last[0])
    usernameList.append(name)

    # d.John
    name = "{last}.{first}".format(first=first.capitalize(), last=last[0])
    usernameList.append(name)

    # D.john
    name = "{last}.{first}".format(first=first, last=last[0].upper())
    usernameList.append(name)

    # D.John
    name = "{last}.{first}".format(first=first.capitalize(), last=last[0].upper())
    usernameList.append(name)

    # d.JOHN
    name = "{last}.{first}".format(first=first.upper(), last=last[0])
    usernameList.append(name)

    # D.JOHN
    name = "{last}.{first}".format(first=first.upper(), last=last[0].upper())
    usernameList.append(name)

# Check if has an output file
writeFile = False
if args.output_file != None:
    writeFile = True

    # Clear file
    outputfile = open(args.output_file, 'w')
    outputfile.write('')
    outputfile.close()

    # Open file to write
    outputfile = open(args.output_file, 'a')

# Print or write the putput
for username in usernameList:
    if writeFile == False:
        print(username)
    else:
        outputfile.write('%s\n' %username)

# Close output file
if writeFile == True:
    outputfile.close()
