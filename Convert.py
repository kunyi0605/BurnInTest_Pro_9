import os

inpath = r"C:/Jenkins-Report/"
expath = r"C:/Jenkins-Report/"
encoding1 = "utf-16"
encoding2 = "ansi"
 
input_filename = "BurnInTest_result.log"
input_pathfile = os.path.join(inpath, input_filename)

output_filename = "new_BurnInTest_result.log"
output_pathfile = os.path.join(expath, output_filename)


with open(input_pathfile, 'r', encoding=encoding1) as file_in:
    lines = []
    for line in file_in:
        lines.append(line)

with open(output_pathfile, 'w', encoding='ANSI') as f:
    for line in lines:
        f.write(line)