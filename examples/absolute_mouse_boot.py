# SPDX-FileCopyrightText: 2022 Neradoc
# SPDX-License-Identifier: Unlicense

import usb_hid
from absolute_mouse.descriptor import device

usb_hid.enable((usb_hid.Device.KEYBOARD, device))
