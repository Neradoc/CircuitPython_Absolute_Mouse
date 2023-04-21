# SPDX-FileCopyrightText: 2017 Dan Halbert for Adafruit Industries
# SPDX-FileCopyrightText: 2021 David Glaude
# SPDX-FileCopyrightText: Copyright (c) 2023 Neradoc
#
# SPDX-License-Identifier: MIT
"""
`absolute_mouse`
================================================================================

A library for a custom mouse device that sends absolute coordinates.


* Author(s): David Glaude, Neradoc

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

import time
from adafruit_hid import find_device

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/Neradoc/CircuitPython_absolute_mouse.git"


class Mouse:
    """Send USB HID mouse reports."""

    LEFT_BUTTON = 1
    """Left mouse button."""
    RIGHT_BUTTON = 2
    """Right mouse button."""
    MIDDLE_BUTTON = 4
    """Middle mouse button."""

    def __init__(self, devices):
        """Create a Mouse object that will send USB mouse HID reports.

        Devices can be a list of devices that includes a keyboard device or a keyboard device
        itself. A device is any object that implements ``send_report()``, ``usage_page`` and
        ``usage``.
        """
        self._mouse_device = find_device(devices, usage_page=0x1, usage=0x02)
        # print(dir(devices))
        # Reuse this bytearray to send mouse reports.
        # report[0] buttons pressed (LEFT, MIDDLE, RIGHT)
        # report[1] x1 movement
        # report[2] x2 movement
        # report[3] y1 movement
        # report[4] y2 movement
        # report[5] wheel movement
        self.report = bytearray(6)

        # Do a no-op to test if HID device is ready.
        # If not, wait a bit and try once more.
        try:
            self._send_no_move()
        except OSError:
            time.sleep(1)
            self._send_no_move()

    def press(self, buttons):
        """Press the given mouse buttons.

        :param buttons: a bitwise-or'd combination of ``LEFT_BUTTON``,
            ``MIDDLE_BUTTON``, and ``RIGHT_BUTTON``.

        Examples::

            # Press the left button.
            m.press(Mouse.LEFT_BUTTON)

            # Press the left and right buttons simultaneously.
            m.press(Mouse.LEFT_BUTTON | Mouse.RIGHT_BUTTON)
        """
        self.report[0] |= buttons
        self._send_no_move()

    def release(self, buttons):
        """Release the given mouse buttons.

        :param buttons: a bitwise-or'd combination of ``LEFT_BUTTON``,
            ``MIDDLE_BUTTON``, and ``RIGHT_BUTTON``.
        """
        self.report[0] &= ~buttons
        self._send_no_move()

    def release_all(self):
        """Release all the mouse buttons."""
        self.report[0] = 0
        self._send_no_move()

    def click(self, buttons):
        """Press and release the given mouse buttons.

        :param buttons: a bitwise-or'd combination of ``LEFT_BUTTON``,
            ``MIDDLE_BUTTON``, and ``RIGHT_BUTTON``.

        Examples::

            # Click the left button.
            m.click(Mouse.LEFT_BUTTON)

            # Double-click the left button.
            m.click(Mouse.LEFT_BUTTON)
            m.click(Mouse.LEFT_BUTTON)
        """
        self.press(buttons)
        self.release(buttons)

    def move(self, x=0, y=0, wheel=0):
        """Move the mouse and turn the wheel as directed.

        :param x: Set pointer on x axis. 32767 = 100% to the right
        :param y: Set pointer on y axis. 32767 = 100% to the bottom
        :param wheel: Rotate the wheel this amount. Negative is toward the user, positive
            is away from the user. The scrolling effect depends on the host.

        Examples::

            # Move 100 to the left. Do not move up and down. Do not roll the scroll wheel.
            m.move(1000, 3000, 0)
            # Same, with keyword arguments.
            m.move(x=1000, y=3000, wheel=0)


            # Roll the mouse wheel away from the user.
            m.move(wheel=1)
        """

        # Wheel
        while wheel != 0:
            partial_wheel = self._limit(wheel)
            print(wheel)
            self.report[5] = partial_wheel & 0xFF
            self._mouse_device.send_report(self.report)
            wheel -= partial_wheel

        # Coordinates
        x = self._limit_coord(x)
        y = self._limit_coord(y)
        # HID reports use little endian
        x1, x2 = (x & 0xFFFFFFFF).to_bytes(2, "little")
        y1, y2 = (y & 0xFFFFFFFF).to_bytes(2, "little")
        # print(x1)
        # print(x2)
        # print(y1)
        # print(y2)
        self.report[1] = x1
        self.report[2] = x2
        self.report[3] = y1
        self.report[4] = y2
        self._mouse_device.send_report(self.report)

    def _send_no_move(self):
        """Send a button-only report."""
        self.report[1] = 0
        self.report[2] = 0
        self.report[3] = 0
        self.report[4] = 0
        self._mouse_device.send_report(self.report)

    @staticmethod
    def _limit(dist):
        return min(127, max(-127, dist))

    @staticmethod
    def _limit_coord(coord):
        return min(32767, max(0, coord))
