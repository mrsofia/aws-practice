import os

# writes the names of all files, directories, subdirectories,
# and files in subdirectories to 'paths.txt'

# use context manager for clean exit in case of failure
with open('paths.txt', 'w+') as f:

    for dirname, dirnames, filenames in os.walk('.'):
        for subdirname in dirnames:
            f.write(os.path.join(dirname, subdirname))
            f.write('\n')

        for filename in filenames:
            f.write(os.path.join(dirname, filename))
            f.write('\n')
