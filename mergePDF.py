import sys, os
import PyPDF2
from os import listdir
from os.path import isfile, join
from tkinter import filedialog
from tkinter.filedialog import askdirectory, askopenfilename
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

merger = PdfFileMerger()

print("Welcome to PDF MERGER!")
should_we_merge= input("Would you like to merge all the files in one directory into a single file? (y/n) ")

if should_we_merge.lower() =='y':
    # ask where to put the final PDF:
    print(sys.argv)
    output_filename = input("Enter the desired file name:") + ".pdf"
    print("Select the desired folder for the final combined file.")
    mynewpdflocation = askdirectory()  #enter where you want the final file

    #ask where the files are
    print("Select the folder of the PDFs to be merged.")
    folder = askdirectory() #path to the folder directory;
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    mynewpdf = os.path.join(mynewpdflocation, output_filename.replace(" ", "")) #

    #merge the files:
    print("PDFs detected:")
    for filename in onlyfiles:
        if str(filename).endswith(".pdf"):
            print(filename)

    flip = input("Should the list be flipped? (y/n) ")

    if flip.lower() == 'y':
        onlyfiles = reversed(onlyfiles)

    for filename in onlyfiles:
        if str(filename).endswith(".pdf"):
            print('detected and merging: '+ filename)
            filepather = os.path.join(folder,filename)
            if "-B" in filename:
                merger.append(PdfFileReader(open(filepather, 'rb')), bookmark = filename[:-4], import_bookmarks=False)
            else:
                merger.append(PdfFileReader(open(filepather, 'rb')),import_bookmarks=False)
    merger.write(mynewpdf) #write the outputfile
    merger.close()
    print("Merging successful.")
if should_we_merge.lower() =='n':
    should_we_insert = input("Would you like to insert a PDF into another PDF? (y/n) ")
    if should_we_insert.lower() =='y':
        print("okay lets insert...select the file to be added.")
        addpath = askopenfilename()
        print("select the final file")
        finalpath = askopenfilename()
        pageinput =  input("What page should the file be placed after? ")
        if pageinput.isdigit():
            merger.append(finalpath,import_bookmarks=True)
            merger.merge(int(pageinput),addpath,)
            merger.addBookmark(addpath.split("/")[-1][:-4], int(pageinput),parent=None)
            print("Merge successful, where should the output file be located?")
            mynewpdflocation = askdirectory()  #enter where you want the final file
            output_filename = input("Enter the output file name:") + ".pdf"
            mynewpdf = os.path.join(mynewpdflocation, output_filename.replace(" ", ""))
            merger.write(mynewpdf) #write the outputfile
            merger.close()
            print("Success! Created: " + output_filename)
            print("Goodbye.")
        else:
            print("That is not a number! Please restart.")
    else:
        print("Goodbye.")
else:
    print("Goodbye.")



##################
# pdf_writer = PdfFileWriter()
# pdf_writer.addBlankPage(width=500,height=500)
# pdf_writer.write(open(os.path.join(mynewpdflocation, output_filename),'wb'))
# print('Created: ' + output_filename + '\n')


#pyinstaller
# pyinstaller --onefile --noupx mergePDF.py
