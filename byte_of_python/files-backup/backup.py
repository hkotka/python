#!/usr/bin/env python3
import os
import time
from sys import argv
import func_help

source = ['/home/henkka/backup/files1', '/home/henkka/backup/files2']
target_dir = '/home/henkka/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

zip_command = "zip -qr "

# User can pass additional commandline arguments for different options
if len(argv) > 0:
    i = 0
# Display program help message
    for arg in argv:
        if arg == '--help':
            func_help.helpMsg()
            break
# Add directories into additional sources for backup
        elif arg == '-d':
            if i+2 <= len(argv):
                source.append(argv[i+1])
            else:
                break
# Run zip program with verbose output if the user passes -v argument
        elif arg == '-v':
            zip_command = "zip -rv "
        i += 1

# Take the user input comment as a name of the zip file
comment = input('Enter a comment -->')
if comment == 0: # check if comment was entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

zip_commandFinal = zip_command+"{0} {1}".format(target, ' '.join(source))

# Create the subdirectory if it isn‚t already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

if os.system(zip_commandFinal) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
