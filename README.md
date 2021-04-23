# BullDog

Python USB OTG HID (_Keyboard_)

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

the woof.txt (_text file_)...

```
# This is a simple barking script for macOS
[CMD] GUI SPACE
Terminal
[CMD] ENTER
who am i
[CMD] ENTER
```

## ToDo's

- Add triple and quadruple keystrokes
- Testing for Windows
- Testing for Linux
- Direct Command Line input (_without Barking file_)
- DuckyScript reader
- more examples for different Operating Systems