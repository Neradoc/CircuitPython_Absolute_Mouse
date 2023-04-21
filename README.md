# CircuitPython_Absolute_Mouse

This is a library for a custom mouse device that sends absolute coordinate (as opposed to a normal mouse that does relative movement).
This is working on Windows (and maybe other operating system, not tested yet).

# How to use

Make sure [adafruit_hid](https://github.com/adafruit/Adafruit_CircuitPython_HID) is installed.

- Copy the `absolute_mouse` whole directory into the board's `/lib/` directory.
- Copy the content of `examples/absolute_mouse_boot.py` to your `boot.py` (create it if needed).
- Eject the board and reset it so that the new USB device is setup on the computer.
- The simple test file contains an example that moves the mouse to different points.

# Demo

As seen on `Show and Tell` on 20/04/2022 : https://www.youtube.com/watch?v=belKMexuOZA&t=1310s

# Credit

* @dglaude for originally creating the abs_mouse module.
* @danh for all learn guide and the USB-HID code in the core of CircuitPython and in library.
* @bitboy85 for providing working code for mouse_abs: https://gist.github.com/bitboy85/cdcd0e7e04082db414b5f1d23ab09005
* @jfurcean John Furcean for the WiiChuck library: https://github.com/jfurcean/CircuitPython_WiiChuck

