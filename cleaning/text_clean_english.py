import os
import glob

path = "/Users/zeca/Desktop/corpus_cleaning/texts_english/*.txt"

for file in glob.glob(path):            # iterate over all files
    with open(file, "r") as input_file:
        filename = os.path.basename(file)   # get input file name
        output = ('%s_clean.txt' % filename)     # meaningfully name the output file
        with open(output, "w") as output:
            for line in input_file:
                line = line.replace('“', '')
                line = line.replace('”', '')
                line = line.strip()     # clear white space
                try:
                    int(line)  # check if line is a number
                except ValueError:
                    output.write(line + "\n")



