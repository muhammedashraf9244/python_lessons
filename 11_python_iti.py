'''
Learn:
    - File handle
'''
'''
In python to handle with file use function open(path_file(str),mode(str))
mode is the states of open file 
types modes 
'a' : Append open file for appending values , If not exit create file
'r' : Read [Default mode] open file for reading if not found give error
'w' : Write open file for writing if not exit found error
'x' : create create file give error if found 
'''
# to find path of file use os module for handle of yout system beacuse current dir is different for os to other
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
# open file use relative path ./ => current_dir 
myfile=open(r"./open_file.txt")
# absolute file 
my_path_file=os.getcwd()+'/open_file.txt'
myfile=open(my_path_file)

# if path of file in dir called nfile if in windows dir is \dir\.. 
# so \nfile means \n new line so use r is raw string means do run command in it
myfile=open(r'/media/muhammed/New Volume/computer science/ITI_3_Python/python/fundemental_python_course/nfile/file.txt')

# print(f'Object file => {myfile}')  # print File Data Object
# print(f'File name => {myfile.name}')
# print(f'File mode => {myfile.mode}')
# print(f'File Encoding => {myfile.encoding}')

'''
Method in file 
read(number) defalut number = -1 meanse read all file if n read n characters in file
readline(number) defalut read all line but n read n characters in line read line by line next  
readlines() Return a list of lines from the stream.
closed is proprite for check if file closed or not if closed give True else give false
'''
# print(myfile.read())
# print(myfile.read(20))
# print(myfile.readline(10).strip())
# print(myfile.readline().strip())
# print(myfile.readline().strip())
# print(myfile.readlines())
# print(myfile.readlines(25))
print( myfile.closed)
'''
how use loop in file 
'''

for line in myfile:
    if 'python' in line : continue
    print(line.strip().title())

# Very Important close file after use 
myfile.close()
'''
Open in mode w for write if file not found give error 
write(str) write string 
writeline(multi_line_str) Write a list of lines to stream.
''' 
myfile1=open(my_path_file,"w")
# r means ingore escape characters 
# myfile1.write(r"\nHello python") # write \nHello python
# myfile1.write("\nHello python\n"* 10 ) # write \nHello python
mylist=["I love Python\n","I love java\n"]
myfile1.writelines(mylist)
myfile1.close()

'''
Append append in file use "a"
'''
myfile2=open(my_path_file,"a")
myfile2.writelines(mylist)
'''
Important function 
truncate(number) cut size of string in file and append again in file
tell() get Tell the current file position.
seek(number) make position point character of this number
'''
myfile2.truncate(5)
myfile2.write(" python ")
print('Tell the current file position ',myfile2.tell())
myfile2.close()

fl = open("some_file.txt", 'w')
fl.write('This is new content') 
print(fl.tell())
fl.seek(8) 
fl.write('old') 
fl.close() 
fl = open('some_file.txt', 'a') 
fl.write('\n content is appended')
