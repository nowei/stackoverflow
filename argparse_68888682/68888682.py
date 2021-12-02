import argparse
parser = argparse.ArgumentParser()
def check_slash(string):
     if string and len(string) > 0 and string[0] == '/':
         return string
     else:
         return 'C:/Program Files/' + string


parser.add_argument('execCmd' , type=check_slash)
args = parser.parse_args()

print(args)