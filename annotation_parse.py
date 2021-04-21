#! /usr/local/bin/python3.4
import sys
import getopt
import csv
# Usage statement for the program.
def usage():
    print("Usage:cleofessarmiento_Assign4.py [-i FILE] [-o FILE]" +
          "\n""   -i: input file (CLC genomics csv-formatted); STDIN if not used." + "\n"
          "   -o: output file (csv-formatted); STDOUT if not used." + "\n")
# Beginning of code formating the CLC genomics csv file.
def formatSeq(inputfile, outputfile): 
    line = inputfile.readline()
    counter = 1
    tmp = ''
    tmp2 = ''
    tmp3 = ''
    tmp4 = ''
    array_dup_check = []
    # As long as it is not the end of the file it will loop.
    while line != "":
        line = inputfile.readline()
        if line == '':
            break
        # Breaks up the csv into an array.
        tmp = line.split(',')
        name = str(tmp[0]).replace('\'', '')
        field2 = str(tmp[1]).replace('\'', '')
        location = str(tmp[2]).replace('\'', '')
        tmp2 = str(tmp[3]).replace('\'','')
        tmp3 = tmp2.replace('\n','')
        qual = tmp3.replace('\r','')
        # Insert statements that prepares each lines into four parts of 
        # a MySQL insert statement.
        insert = 'INSERT IGNORE INTO S_aureus_JE2 VALUES ' + 
        ' (\'' + name + '\', \'' + field2 + '\', \''+ location+ '\', \'' + qual + '\');'
        outputfile.write(insert)
        outputfile.write('\n')
# Code to accept argument as a file and a name for the output file. 
def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "i:o:")
  except getopt.GetoptError as err:
    sys.stdout = sys.stderr
    print(str(err))
    usage()
    sys.exit(2)
  inputfile = sys.stdin
  outputfile = sys.stdout  
  for (opt, arg) in opts:
    if (opt == ("-i")):
      inputfile = open(arg, "r")
    if (opt == ("-o")):
      outputfile = open(arg, "w")
  # Function formats the input and outputs MySQL insert statements for each gene.
  formatSeq(inputfile, outputfile)
if __name__ == '__main__':
  main()
