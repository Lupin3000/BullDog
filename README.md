# BullDog

![BullDog](./img/bulldog.jpg)

Python USB OTG HID (_Keyboard_) for Raspberry PI Zero (_and other_)

> Inspired by [RubberDucky](https://shop.hak5.org/products/usb-rubber-ducky-deluxe), [O.MG cable](https://mg.lol/blog/omg-cable/) and other nice tools, I created this Python3 BullDog cli tool.
> As I was a little unhappy with the DuckyScript syntax, I developed the new Barking syntax.

## Preparation

If you need to create a USB OTG HID, [here](https://github.com/Lupin3000/Raspberry-PI-Tutorials) you will find all information (_for Raspberry PI Zero_).

```shell
# install git and pip (Python 3.x)
$ sudo apt install git python3-pip
```

## Usage

```shell
# clone repository
$ git clone https://github.com/Lupin3000/BullDog.git

# change into cloned directory
$ cd BullDog/

# install via pip3
$ pip3 install .

# show help (optional)
$ BullDog -h

# execute barking script
$ BullDog -b examples/macOS/woof.txt

# execute barking script with default delay
$ BullDog -b examples/macOS/woof.txt -d 0.05

# just test barking script (no need for /dev/hidg0)
$ BullDog -b examples/macOS/woof.txt -t
```

## The barking script

Example of the barking script `woof.txt` (_simple text file_)...

```
# This is a simple barking script example for macOS
#
#        ,--._______,-.
#       ,','  ,    .  ,_`-.
#      / /  ,' , _` ``. |  )
#     (,';'""`/ '"`-._ ` \/
#       : ,o.-`- ,o.  )\` -'
#       : , d8b ^-.   '|   `
#       |/ __:_     `. |  ,
#       | ( ,-.`-.    ;'  ;
#       | |  ,   `.      /
#       `-'`:::._,`.__),'
#

[CMD] GUI SPACE
[DELAY] 0.25
Terminal
[CMD] ENTER
[DELAY] 0.05
who am i
[CMD] ENTER
```

### Supported Keyboard Keys

**Standard/Shifted Keys**

Decimals from 4 till 39, 44, 45 till 56

**Modifier Keys**

- LEFT_CONTROL or RIGHT_CONTROL (_or simply **CONTROL**_)
- LEFT_SHIFT or RIGHT_SHIFT (_or simply **SHIFT**_)
- LEFT_ALT or RIGHT_ALT (_or simply **ALT**_)
- LEFT_GUI or RIGHT_GUI (_or simply **GUI** or **WIN**_)

**Command Keys**

ENTER, ESCAPE, BACKSPACE, TAB, SPACE, CAPS_LOCK, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, PRINT, SCROLL_LOCK, 
PAUSE, INSERT, HOME, PAGE_UP, DELETE, END, PAGE_DOWN, RIGHT_ARROW, LEFT_ARROW, DOWN_ARROW, UP_ARROW, LEFT_CONTROL, 
LEFT_SHIFT, LEFT_ALT, LEFT_GUI, RIGHT_CONTROL, RIGHT_SHIFT, RIGHT_ALT, RIGHT_GUI

**Keypad Keys**

Maybe some time later ;)

## ToDo's

- Add triple and quadruple keystrokes
- Testing keyboard on Windows/Linux/macOS (_not the Python code_)
- Direct Command Line input (_without Barking file_)
- DuckyScript reader
- more examples for different Operating Systems
