## Input 

There are vairous ways to handle input in NextBuild. 

### Keyboard

### Example

```nextbuild
#include <keys.bas>
dim i as ubyte 

do 
    ' detect keybaord P 
    if GetKeyScanCode()=KEYP
        print ink 7;at 0,0;"p is pressed" 
        i = 7
    end if 

    if i > 0 
        i = i - 1 
        print at 0,0; over 1; ink i;"                "       
    endif 

    WaitRaster(192) 

loop 
```

To detect multiple keys you will use ``MultiKeys`` : 

```

do 
    ' detect keybaord P 
    if MultiKeys(KEYP) & Multikeys(KEYSPACE)
        print ink 7;at 0,0;"keys are pressed" 
        i = 7
    end if 

    if i > 0 
        i = i - 1 
        print at 0,0; over 1; ink i;"                "       
    endif 

    WaitRaster(192) 

loop 
```
The codes for each key are defined in the ``keys.bas`` file. 

``KEYA-KEYZ`` ``KEY0-KEY9`` ``KEYSPACE`` ``KEYENTER`` ``KEYSYMBOL`` ``KEYCAPS``

### Joystick 

```nextbuild
dim j as ubyte 
dim i as ubyte 
do 
    ' port 31 if kempston 1, 51 kempston 2
    j = in 31           ' Kempston 1
    ' up and down 
    if j band BIT_UP
        print at 0,0; "up"
    elseif j band BIT_DOWN
        print at 0,0; "down"
    endif 
    ' left and right 
    if j band BIT_LEFT
        print at 0,0; "left"
    elseif j band BIT_RIGHT 
        print at 0,0; "right"
    endif 
    ' fade the ink 
    if i > 0 
        i = i - 1 
        print at 0,0; over 1; ink i;"                "       
    endif 
    WaitRaster(192) 
loop
```
The joystick bit is bitmapped as follows : 

| Bit | Kempston joystick | MD controller |
|-----|-------------------|---------------|
| 7   | 0                 | start button  |
| 6   | 0                 | A button      |
| 5   | Fire 2            | C button      |
| 4   | Fire 1            | B button      |
| 3   | up                | up            |
| 2   | down              | down          |
| 1   | left              | left          |
| 0   | right             | right         |

For all bits: **0** = not pressed / **1** = pressed 

## Links

- [keys.bas](keys.bas)

