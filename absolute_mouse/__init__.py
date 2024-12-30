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
import struct
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
        # Reuse this bytearray to send mouse reports.
        # report[0] buttons pressed (LEFT, MIDDLE, RIGHT)
        # report[1] x1 movement
        # report[2] x2 movement
        # report[3] y1 movement
        # report[4] y2 movement
        # report[5] wheel movement
        self.report = bytearray(6)

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
        self._mouse_device.send_report(self.report)

    def release(self, buttons):
        """Release the given mouse buttons.

        :param buttons: a bitwise-or'd combination of ``LEFT_BUTTON``,
            ``MIDDLE_BUTTON``, and ``RIGHT_BUTTON``.
        """
        self.report[0] &= ~buttons
        self._mouse_device.send_report(self.report)

    def release_all(self):
        """Release all the mouse buttons."""
        self.report[0] = 0
        self._mouse_device.send_report(self.report)

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

    def move(self, x=None, y=None, wheel=0):
        """
        Place the mouse at the indicated position and turn the mouse wheel.
        Moves to the coordinates before wheeling.
        Does not move the mouse if x and y are not provided or ``None``.

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

        # Coordinates
        if x is not None:
            x = self._limit_coord(x)
            self.report[1:3] = struct.pack("<H", x)
        if y is not None:
            y = self._limit_coord(y)
            self.report[3:5] = struct.pack("<H", y)
        if (x, y) != (None, None):
            self._mouse_device.send_report(self.report)

        # Wheel
        while wheel != 0:
            partial_wheel = self._limit(wheel)
            self.report[5] = partial_wheel & 0xFF
            self._mouse_device.send_report(self.report)
            wheel -= partial_wheel

    @staticmethod
    def _limit(dist):
        return min(127, max(-127, int(dist)))

    @staticmethod
    def _limit_coord(coord):
        return min(32767, max(0, int(coord)))
