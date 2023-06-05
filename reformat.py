# if line exceeds 2499 chars, split onto new line
# cannot separate variables or identifiers, which are seperated by commas
import shutil
import glob
import re
def main(filetoFormat):
    unchangedf = open(filetoFormat, "r")
    fileOutput = "temp.sql"
    # create new file
    changedf = open(fileOutput, "w")
    changedf.write("") # clearing file
    for line in unchangedf:
        try:
            comment = line.find('--')
            if comment != -1:
                line = line[:comment] + "\n"
            if len(line) > 2499:
                if line[2498] != ',':
                    # Find the index of the last comma before the 2499th character
                    last_comma_index = line.rfind(',', 0, 2498)
                    if last_comma_index != -1:
                        # Move the string after the last comma to a new line
                        line = line[:last_comma_index] + '\n' + ',' + '\n' + line[last_comma_index+1:]
                        changedf = open(fileOutput, "a")
                        changedf.write(line)
            elif len(line) < 2499:
                changedf = open(fileOutput, "a")
                changedf.write(line)
        except:
            continue
    changedf.close()
    unchangedf.close()
    shutil.move(fileOutput, filetoFormat)
if __name__ == "__main__":
    allfiles = glob.glob('*.sql')
    if allfiles:
        for filetoFormat in allfiles:
            main(filetoFormat)
    else:
        print("No file paths found")
