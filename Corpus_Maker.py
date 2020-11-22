from os import path, listdir
import sys
class Corpus_Maker:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        if (not self.folder_path.endswith('/')):
            self.folder_path = self.folder_path + '/'
        if (not path.exists(self.folder_path)):
            print("\nPath did not exist. exiting...\n")
            exit()

    def make(self):
        ofile = open(self.folder_path + 'corpus.txt', "w")
        folders = listdir(self.folder_path)
        for folder in folders:
            if ('.' in folder):
                continue
            filename = self.folder_path + folder + '/' + folder + '.txt'
            corpus = open(filename)
            for line in corpus.readlines():
                ofile.write(f'<s> {line.strip()} </s> ')
        ofile.close()
        print('all done!')

argv = sys.argv
if (len(argv) > 1):
    _path = argv[1]
else:
    print('\nnot path was given. exiting...\n')

x = Corpus_Maker(_path)
x.make()