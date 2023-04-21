Introduction
============


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/Neradoc/CircuitPython_absolute_mouse/workflows/Build%20CI/badge.svg
    :target: https://github.com/Neradoc/CircuitPython_absolute_mouse/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A library for a custom HID mouse device that sends absolute coordinates.


Dependencies
=============

This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Usage Example
=============

Copy the content of ``examples/absolute_mouse_boot.py`` to your boot.py (create it if needed).

The simple test file contains an example that moves the mouse to different points.

Original version seen on Show and Tell on 20/04/2022 `Check the video <https://www.youtube.com/watch?v=belKMexuOZA&t=1310s>`_.

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install absolute_mouse

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/Neradoc/CircuitPython_absolute_mouse/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.


Credit
======

* @dglaude for originally creating the abs_mouse module.
* @danh for all learn guide and the USB-HID code in the core of CircuitPython and in library.
* @bitboy85 for providing working code for mouse_abs: https://gist.github.com/bitboy85/cdcd0e7e04082db414b5f1d23ab09005
* @jfurcean John Furcean for the WiiChuck library: https://github.com/jfurcean/CircuitPython_WiiChuck
