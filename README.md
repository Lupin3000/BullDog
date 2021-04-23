# BullDog

![BullDog](./img/bulldog.jpg)

Python USB OTG HID (_Keyboard_) for Raspberry PI Zero (_and other_)

> Inspired by [RubberDucky](https://shop.hak5.org/products/usb-rubber-ducky-deluxe), [O.MG cable](https://mg.lol/blog/omg-cable/) and other nice tools, I created this Python BullDog barking. As I was a little unhappy with the DuckyScript syntax, I changed this.

## Preparation

If you need to create a USB OTG HID, [here](https://github.com/Lupin3000/Raspberry-PI-Tutorials) you will find all information (_for Raspberry PI Zero_).

## Usage

```shell
# clone repository
$ git clone https://github.com/Lupin3000/BullDog.git

# change file permissions
$ chmod u+x BullDog.py

# show help (optional)
$ ./BullDog.py -h

# simple barking
$ ./BullDog.py examples/macOS/woof.txt

# simple barking with default delay
$ ./BullDog.py examples/macOS/woof.txt -d 0.05

# just debug (no need for /dev/hidg0)
$ ./BullDog.py examples/macOS/woof.txt -t
```

Example of the woof.txt (_text file_)...

```
# This is a simple barking script for macOS
[CMD] GUI SPACE
Terminal
[CMD] ENTER
who am i
[CMD] ENTER
```

### Supported Keyboard Keys

**Standard/Shifted Keys**

Decimals from 4 till 39, 44, 45 till 56

**Modifier Keys**

- LEFT_CONTROL or RIGHT_CONTROL or CONTROL
- LEFT_SHIFT or RIGHT_SHIFT or SHIFT
- LEFT_ALT or RIGHT_ALT or ALT
- LEFT_GUI or RIGHT_GUI or GUI or WIN

**Command Keys**

ENTER, ESCAPE, BACKSPACE, TAB, SPACE, CAPS_LOCK, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, PRINT, SCROLL_LOCK, 
PAUSE, INSERT, HOME, PAGE_UP, DELETE, END, PAGE_DOWN, RIGHT_ARROW, LEFT_ARROW, DOWN_ARROW, UP_ARROW, LEFT_CONTROL, 
LEFT_SHIFT, LEFT_ALT, LEFT_GUI, RIGHT_CONTROL, RIGHT_SHIFT, RIGHT_ALT, RIGHT_GUI

**Keypad Keys**

Maybe some time later ;)

## ToDo's

- Add triple and quadruple keystrokes
- Testing for Windows
- Testing for Linux
- Direct Command Line input (_without Barking file_)
- DuckyScript reader
- more examples for different Operating Systems
