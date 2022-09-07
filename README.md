# CircuitPython_Absolute_Mouse

This is demonstration of custom USB_HID to make a mouse device that send absolute coordinate (as opposed to normal mouse that do relative move).
This is working on Windows (and maybe other operating system, not tested yet).

# How to use

Make sure [adafruit_hid](https://github.com/adafruit/Adafruit_CircuitPython_HID) is installed.

- Copy the `mouse_abs` module into the board's `/lib/` directory.
- Copy the `boot.py` file, or adapt it to tour needs.
- The code.py file contains a simple example that moves the mouse to different points.

# Demo

As seen on `Show and Tell` on 20/04/2022 : https://www.youtube.com/watch?v=belKMexuOZA&t=1310s

# Credit

* @dglaude for originally creating the abs_mouse module.
* @danh for all learn guide and the USB-HID code in the core of CircuitPython and in library.
* @bitboy85 for providing working code for mouse_abs: https://gist.github.com/bitboy85/cdcd0e7e04082db414b5f1d23ab09005
* @jfurcean John Furcean for the WiiChuck library: https://github.com/jfurcean/CircuitPython_WiiChuck

