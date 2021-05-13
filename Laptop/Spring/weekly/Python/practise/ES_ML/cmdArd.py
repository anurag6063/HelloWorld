import argparse

#parser = ArgumentParser()

parser =argparse.ArgumentParser(description='This is a sample parser')

parser.add_argument("echo")
args = parser.parse_args()
print(args)