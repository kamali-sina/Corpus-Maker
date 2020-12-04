from os import path, listdir
from os.path import isfile, isdir
import sys

PUNCTUATIONS = ['.','\'', ',',';',':','"', '`', '#', '(', ')', '{', '}',
                '[', ']','?','/','-','!', '$', '*', '&', '%']

OFILE_PATH = './Full_set/Combined/corpus-'

DIGIT_TAG = '<d>'

class Corpus_Maker:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        if (not self.folder_path.endswith('/')):
            self.folder_path = self.folder_path + '/'
        if (not self.folder_check(folder_path)):
            print(f"\nfolder Path {folder_path} was invalid. exiting...\n")
            exit()

    def folder_check(self, path):
        try:
            if (isdir(path)):
                return True
            return False
        except:
            return False

    def get_files(self, path):
        if (not path.endswith('/')):
            path = path + '/'
        if (not self.folder_check(path)):
            print('path was invalid')
            return []
        folders = [path]
        files = []
        while (len(folders) != 0):
            folder = folders.pop(0)
            temp = listdir(folder)
            for f in temp:
                fpath = folder + f 
                if (isfile(fpath)):
                    files.append(fpath)
                else:
                    folders.append(fpath + '/')
        return files

    def make(self, ignore_punctions=False, join=False, i=1):
        v_set = set()
        l = 0
        ofile = open(self.folder_path + 'corpus.txt', "w")
        files = self.get_files(self.folder_path)
        for afile in files:
            if (not afile.endswith('.txt')):
                continue
            corpus = open(afile)
            for line in corpus.readlines():
                if (join):
                    line = line.strip()
                    splitted_line = line.split()
                    l += len(splitted_line)
                    v_set.update(splitted_line)
                    ofile.write(f' {" ".join(splitted_line)} ')
                else:
                    line = line.strip()
                    if (not ignore_punctions):
                        for punc in PUNCTUATIONS:
                            line = line.replace(punc, f' {punc} ')
                    splitted_line = line.split()
                    for index in range(len(splitted_line)):
                        if (splitted_line[index].isnumeric()):
                            splitted_line[index] = DIGIT_TAG
                    l += len(splitted_line)
                    v_set.update(splitted_line)
                    ofile.write(f'<s> {" ".join(splitted_line)} </s> ')
        ofile.close()
        print(f'corpus has v: {len(v_set)} and l: {l}')