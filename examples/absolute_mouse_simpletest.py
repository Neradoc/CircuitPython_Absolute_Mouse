# SPDX-FileCopyrightText: 2022 Neradoc
# SPDX-License-Identifier: Unlicense

import time
import usb_hid
from absolute_mouse import Mouse

m = Mouse(usb_hid.devices)

# mouse_abs accept value from 0 to 32767 for both X and Y
# Note: Values are NOT pixels! 32767 = 100% (to right or to bottom)


def transpose(x, y):
    return ((x * 32767) // 1920, (y * 32767) // 1080)


positions = [(10, 40), (800, 800), (1600, 200)]

while True:
    time.sleep(2)
    for position in positions:
        print("MOVE", position, transpose(*position))
        m.move(*transpose(*position))
        time.sleep(2)
    # time.sleep(10)
    break
