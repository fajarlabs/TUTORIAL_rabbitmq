#!/usr/bin/python

import os
STORE_PATH = "/tmp/store.log"

if os.path.exists(STORE_PATH) and os.path.getsize(STORE_PATH) > 2242880:
    os.system("rm "+STORE_PATH)

# create new file if not exist
with open(STORE_PATH, 'w'):
    pass