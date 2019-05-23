def replace_char(line):
    for word in line.split():
     for char in word:
       if( char == 'o' or char =='O' ):
           char.replace('0')
       elif(char == 'a' or char == 'A'):
           char.replace('4')
       elif(char == 'e' or char == 'E'):
          char.replace('3')
       elif(char == 'i' or char == 'I'):
          char.replace('1')
    







fin = open("/home/dinu/fizzbuzz-DineshKandasamy/openbookfinal-2019-DineshKandasamy9396/Book1.txt")
fout = open("/home/dinu/fizzbuzz-DineshKandasamy/openbookfinal-2019-DineshKandasamy9396/Copied_lines_file.txt")
for i in range(25):
 lines = fin.readlines()
 replace_char(lines)

