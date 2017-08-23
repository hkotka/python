#!/usr/bin/env python3

import os
import time

source = ['/home/henkka/files', '/home/henkka/files2']

target_dir = '/home/henkka/backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

