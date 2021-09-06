# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    regex_inp = input()
    try:
        regex = re.compile(regex_inp)
    except re.error:
        print(False)
    else:
        print(True)
