import sys, os

print('Executing docker image ls...')
output = os.popen('docker image ls').read()
print(output)
print('Done, good bye: ' + sys.argv[1])
