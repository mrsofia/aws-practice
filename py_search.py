import os

with open('paths.txt', 'w+') as f:

    for dirname, dirnames, filenames in os.walk('.'):
        for subdirname in dirnames:
            f.write(os.path.join(dirname, subdirname))
            f.write('\n')

        for filename in filenames:
            f.write(os.path.join(dirname, filename))
            f.write('\n')
