# Project 9: Obstacle Detector using Proximity and Motion Sensor

- This is a modified copy of atSign's own README.md, it contained a lot of relevant information so it is reused.
- Also disclaimer this repo only consist of the backend data being sent, my group mates who worked on the front end has their own repo.

# Table of Contents

- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Instructions](#instructions)
  * [0. Wiring your Pico](#0-Wiring-your-Pico)
  * [1. Getting the right Micropython Firmware for your Pico W](#1-getting-the-right-micropython-firmware-for-your-pico-w)
  * [2. Getting Started - Blinking the LED](#2-getting-started---blinking-the-led)
  * [3. Git Cloning](#3-git-cloning)
  * [4. Using our project](#4-Using-our-project)

# Prerequisites

- [VSCode](https://code.visualstudio.com/Download) with the [Pico-W-Go extension](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go)
- [Git](https://git-scm.com/) and your own [GitHub](https://github.com) account
- A [Raspberry Pi Pico W](https://www.canakit.com/raspberry-pi-pico-w.html) and [a data micro-USB to USB-A cable](https://m.media-amazon.com/images/I/61kT7kpt2hL._AC_SY450_.jpg) (to connect your Pico to your Computer)
- [FileZilla](https://filezilla-project.org/) or any other FTP software.
- One [atSign](https://my.atsign.com/go) and its [.atKeys file](https://www.youtube.com/watch?v=2Uy-sLQdQcA&ab_channel=Atsign)

# Instructions

## 0. Wiring your Pico

Even before installing Micropython you can start wiring the pico, personally I chose to soder the board but this is optional, once you have the pico on the breadboard, you can follow the image below to set up the wiring:
<img src="https://cdn.discordapp.com/attachments/892140741076353034/1036014548337049710/unknown.png" />

Our project uses two sensors, but just one sensor would work fine as well. on the sensors you can see letters next to the connectors, to which you would connect using the jumper cables.
- G is the ground connection(38 is what we used)
- V is the power connection(36)
- S is the data connection(GP27 and GP26)

## 1. Getting the right Micropython Firmware for your Pico W

1. Go to [atsign-foundation/micropython/releases](https://github.com/atsign-foundation/micropython/releases) and download the `.uf2` file. This `.uf2` file is specially built firmware to allow a certain encryption that Atsign uses (AES-256 CTR mode) to work on the Pico W. Big shoutout to @realvarx for developing all the Atsign encryption for the Pico W. 

2. Unplug your Pico W from your computer. Hold down the BOOTSEL button on the Pico W and then plug back the Pico W into your computer (all while holding down the BOOTSEL button). Once the Pico W is plugged in, you can let go of the BOOTSEL button. Your Pico W should now be in bootloader mode. 

You should see the Pico on your computer as a USB drive (see image below).

<img src="https://i.imgur.com/msoBukM.png" />

3. Drag and drop the `firmware.uf2` file into the Pico W. This will flash the Pico W with the new firmware. Now the Pico W should automatically restart so no need to unplug/replug it.

## 2. Getting Started - Blinking the LED

Now let's create our first project.

1. Open VSCode and create and open an empty folder where your project will be.

2. Get the [Pico-W-Go extension](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go)

3. Create a file named `blink.py` and write the following code:

```py
# blink.py

import machine
import time

led = machine.Pin("LED", machine.Pin.OUT) # "LED" is the on board LED

# blink ten times
for i in range(10):
    print('Blinking... %s' %str(i+1))
    led.toggle()
    time.sleep(0.5)
```

Note: You could also name this file- `main.py`. However, `main.py` is the default file that the Pico W will run when it starts up. But with the [Pico-W-Go extension](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go), you can choose *when* to run a file (regardless of name) which is how we will be running our files from here on out. I recommend not having a `main.py` at all since it tends to bug out the Pico W trying to run your experimental code as soon as it boots which can get annoying.


4. Open the command pallette via `Ctrl + Shift + P` (or `Cmd + Shift + P` if you are on a Mac) and type `Configure Project` and press Enter. The extension should setup your current folder as a Pico W project by initializing a `.vscode/` hidden folder and a `.picowgo` hidden file. Now, any Pico-W-Go commands should work. You can also access Pico-W-Go commands by clicking on "All Commands" at the bottom of VSCode.

VSCode bottom toolbar with Pico-W-Go commands:

<img width=500px src="https://i.ibb.co/g3jm53c/image.png">

6. Now try connecting to your Pico W and see if it works. You can do this by clicking on the "Connect" button.

7. Make sure you have your `blink.py` python file open in the editor and Run the "Run current file" command. You should see the onboard LED blink 10 times.

## 4. Using our project

1. The code can be used as is once changes are made to certain hard coded names like wifi and @signs used for tranferring data. @signs generated needs to go into the /keys folder, wifi info can be changed in settings.json along with the @sign that will be assigned to the pico, once the personal info has been changed, this code will work as is
