from Corpus_Maker import Corpus_Maker
import os
import sys

argv = sys.argv
if (len(argv) > 1):
    join = False
    if (argv[1] == '--main'):
        join = True
        _path = argv[2]
    else:
        _path = argv[1]
    x = Corpus_Maker(_path)
    x.make(ignore_punctions=False, join=join)
else:
    FOLDERPATH = './Full_set/'
    c = 1
    for folder in os.listdir(FOLDERPATH):
        if (folder == 'Combined'):
            continue
        addr = FOLDERPATH + folder
        print(addr)
        x = Corpus_Maker(addr)
        x.make(i=c)
        c += 1



