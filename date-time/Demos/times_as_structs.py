import time

# time.gmtime()
print('----------------\ntime.gmtime()\n----------------')
epoch = time.gmtime(0)
print('epoch:\n', epoch)
now = time.gmtime()
print('\nnow:\n', now)
yesterday = time.gmtime(time.time() - 60*60*24)
print('\nyesterday:\n', yesterday)
tomorrow = time.gmtime(time.time() + 60*60*24)
print('\ntomorrow:\n', tomorrow)

# time.localtime()
print('\n----------------\ntime.localtime()\n----------------')
epoch_offset = time.localtime(0) # Gives localtime of epoch
print('epoch offset for DST:\n', epoch_offset)
now = time.localtime()
print('\nnow:\n', now)
yesterday = time.localtime(time.time() - 60*60*24)
print('\nyesterday:\n', yesterday)
tomorrow = time.localtime(time.time() + 60*60*24)
print('\ntomorrow:\n', tomorrow)

# time.mktime()
print('\n----------------\ntime.mktime()\n----------------')
seconds_since_epoch = time.mktime(time.localtime())
print('seconds since epoch:\n', seconds_since_epoch)