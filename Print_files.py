from os import listdir
from os.path import isfile, join
from tkinter.filedialog import askdirectory

folder = askdirectory()

onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]

for filename in onlyfiles:
    print('\includepdf[link,linkname=' + filename + ',pages=-]{' + filename+'}')
    print('\n')
    print(r'\bookmark[dest={' + filename + r'.1}{' + filename + '.1}{'+ filename + '}')
