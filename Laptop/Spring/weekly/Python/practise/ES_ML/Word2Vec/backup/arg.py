import argparse

#parser = ArgumentParser()

parser =argparse.ArgumentParser(description='Pass list of file names to be converted in word2Vec')

parser.add_argument("-l", "--list", nargs='+', type=str, dest = 'file', help='Enter list of files')
args = parser.parse_args()

fileList = args.file
files = fileList[0]
files.split(' ')
print(files.split(' '))
