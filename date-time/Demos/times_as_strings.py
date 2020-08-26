import time

epoch = time.gmtime(0)
epoch_offset = time.localtime(0)

# time.asctime()
print('----------------\ntime.asctime()\n----------------')
str_epoch = time.asctime(epoch)
print('epoch:\n', str_epoch)
str_epoch_offset = time.asctime(epoch_offset)
print('\nepoch offset for DST:\n', str_epoch_offset)
str_now = time.asctime()
print('\nnow:\n', str_now)

# time.ctime()
print('\n----------------\ntime.ctime()\n----------------')
str_epoch_offset = time.ctime(0)
print('epoch offset for DST:\n', str_epoch_offset)
str_now = time.ctime()
print('\nnow:\n', str_now)