# define functions
def createOutputFile():
    fileName = input("Enter a file name to write the results to an output file\n")
    return fileName
    # end createOutputFile function

# sum of digits function
def sum_of_digits(numbers):
    sumT=0
    for digit_string in numbers:
        digit_int = int(digit_string)
        sumT = sumT + digit_int
    return sumT

# define the list
def numList(numbers,outFile):
    for s in range(len(numbers)):
        num = int(numbers[s])
        outFile.write(numbers[s].center(60) + "\n")
        # end FOR loop
    # end num list function

# output statements
def main():
    fileName = createOutputFile()
    outFile = open(fileName + ".txt", "w")
    
    numbers = input("Enter a series of single digit numbers (without spaces):")
    # call the sum function
    sumT = sum_of_digits(numbers)
    outFile.write("="*60 + "\n")
    # return input

    outFile.write(("There are "+ format(len(numbers), ",d") + " different number in the string.").center(60) + "\n")
    outFile.write("=" * 60 + "\n")
    outFile.write(("They are:").center(60) + "\n")
    outFile.write("=" * 60 + "\n")

    # call num list function
    numList(numbers,outFile)
    outFile.write("=" * 60 + "\n")
    outFile.write("The sum of the digits =" + format(sumT, ",d").center(60) + "\n")
    outFile.write("=" * 60 + "\n")
    outFile.close
main()

# close external file


# END PROGRAM
    
    
        
