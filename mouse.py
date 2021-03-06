import time

import uinput

def main():
    events = (
        uinput.REL_X,
        uinput.REL_Y,
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        )

    device = uinput.Device(events)

    for i in range(10):
        # syn=False to emit an "atomic" (5, 5) event.
        device.emit(uinput.REL_X, 5, syn=False)
        device.emit(uinput.REL_Y, 5)

        # Just for demonstration purposes: shows the motion. In real
        # application, this is of course unnecessary.
        time.sleep(0.01)

if __name__ == "__main__":
    main()
