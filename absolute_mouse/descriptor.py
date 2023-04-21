import usb_hid

# https://stackoverflow.com/questions/36750287/two-byte-report-count-for-hid-report-descriptor
# fmt: off
device = usb_hid.Device(
    report_descriptor=bytes((
        # Absolute mouse
        0x05, 0x01,    # Usage Page (Generic Desktop)
        0x09, 0x02,  # Usage (Mouse)
        0xA1, 0x01,  # Collection (Application)
        0x09, 0x01,  # Usage (Pointer)
        0xA1, 0x00,  # Collection (Physical)
        0x85, 0x0B,  # Report ID  [11 is SET at RUNTIME]
        # Buttons
        0x05, 0x09,  # Usage Page (Button)
        0x19, 0x01,  # Usage Minimum (0x01)
        0x29, 0x05,  # Usage Maximum (0x05)
        0x15, 0x00,  # Logical Minimum (0)
        0x25, 0x01,  # Logical Maximum (1)
        0x95, 0x05,  # Report Count (5)
        0x75, 0x01,  # Report Size (1)
        0x81, 0x02,  # Input
                     # (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
        0x75, 0x03,  # Report Size (3)
        0x95, 0x01,  # Report Count (1)
        0x81, 0x03,  # Input
                        # (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position)
        # Movement
        0x05, 0x01,        # Usage Page (Generic Desktop Ctrls)
        0x09, 0x30,        # Usage (X)
        0x09, 0x31,        # Usage (Y)
        0x15, 0x00,        # LOGICAL_MINIMUM (0)
        0x26, 0xFF, 0x7F,  # LOGICAL_MAXIMUM (32767)
        # 0x35, 0x00,        # Physical Minimum (0)
        # 0x46, 0xff, 0x7f,  # Physical Maximum (32767)
        0x75, 0x10,        # REPORT_SIZE (16)
        0x95, 0x02,        # REPORT_COUNT (2)
        0x81, 0x02,        # Input (Data,Var,Rel,No Wrap,Linear,Preferred State,No Null Position)
        # Wheel
        0x09, 0x38,   # Usage (Wheel)
        0x15, 0x81,   # Logical Minimum (-127)
        0x25, 0x7F,   # Logical Maximum (127)
        # 0x35, 0x81,   # Physical Minimum (same as logical)
        # 0x45, 0x7f,   # Physical Maximum (same as logical)
        0x75, 0x08,   # Report Size (8)
        0x95, 0x01,   # Report Count (1)
        0x81, 0x06,   # Input (Data,Var,Rel,No Wrap,Linear,Preferred State,No Null Position)
        0xC0,         # End Collection
        0xC0,         # End Collection
    )),
    usage_page=1,
    usage=2,
    in_report_lengths=(6,), # Number of bytes in the send report
    # 1 byte for buttons, 2 bytes for x, 2 bytes for y, 1 byte for wheel
    out_report_lengths=(0,),
    report_ids=(11,),
)
# fmt: on
