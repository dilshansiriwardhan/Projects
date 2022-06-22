import os
import sys


for cwd , dirs , filenames in os.walk('.'):
    print(cwd[0])
    for dir in dirs:
        print(dir)
    