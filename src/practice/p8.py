from collections import deque
import sys
import time


fancy_loading = deque('>--------------------')
while True:
    print '\r%s' % ''.join(fancy_loading),
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)