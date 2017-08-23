#!/usr/bin/env python3

import os
import time

source = ['/home/henkka/files', '/home/henkka/files2']

target_dir = '/home/henkka/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# Take the user input comment as a name of the zip file
comment = input('Enter a comment -->')
if len(comment) == 0: # check if comment was entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn‚t already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

