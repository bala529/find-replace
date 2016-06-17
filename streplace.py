#!/usr/bin/env python3
import glob
import inspect,os

# @auther: Balasubramaniyan Sundaresan, balu.ls@live.com
#Python script to find and replace string inside any given directory. Also will list the changed made on each file. It will scan through sub-directories. 
#This script assumes that the directory to start the search is under /home


#getting current directory and displaying it.
def_dir= os.getcwd()
print ("\n############################ Find and replace ##################################\n")
print ( " Input the directory to search for a string and then to replace it.")
print ( " Author: Balasubramaniyan Sundaresan(balu), Email: balu.ls@live.com")
print ( "\nCurrent Directory:",def_dir)
print("\n")

dname= input("DIRECTORY NAME: ");
print ("\n")

x=0

#sets current path to /home, but it can be hardcoded to anylocation. 

print("Seaching..... from '/home'\n")
for root, dirs, files in os.walk("/home"):
    if x==0:
        for name in dirs:
            if name==dname:
                path = os.path.join(root, name)
                print("FOUND AT LOCATION: %s \n" % path)        
                x=1        
    if x==1:
        break

if x==0:
    print("DIRECTORY YOU ARE LOOKING FOR IS NOT FOUND!")
    exit(0)

find = input("FIND STRING: ");
print ("\n")


replace= input("REPLACE STRING: ");
print ("\n")

#changing path to the directory mentioned above
os.chdir(path)
list1 = []

#collecting the path of all the files residing under the mentioned directory
for root, dirs, files in os.walk(path):
    for name in files:
        filepath= os.path.join(root,name)
        list1.append(filepath)

#print (list1)
# Find and replace

for filepath in list1:
    f = open( filepath, 'r+' )
    contents = f.read()
    if find in contents:
        print ("\n********************************************************************************")
        print (" \n String FOUND @ '%s'" % filepath)
        print ("\n\t\t####BEFORE replace#### \n",contents)
        newdata = contents.replace(find,replace)    
        f.close()
        f= open( filepath, 'w+')
        f.write(newdata)
        f.close()
        f = open (filepath,'r+')
        replaced = f.read()
        print ("\n\t\t####AFTER replace##### \n",replaced)
        f.close()
    else:
        print("STRING NOT FOUND in '%s'" % filepath)
        print("\n")
        f.close()

#end