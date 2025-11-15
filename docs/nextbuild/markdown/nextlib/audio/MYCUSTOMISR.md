# MYCUSTOMISR

## Syntax

```
Sub MyCustomISR()
	' Your code here
End Sub
```

## Description

## MyCustomISR() 

Is used to set up a custom interrupt routine set up by [SetUpIM()](SETUPIM.md). You can use `MyCustomISR()` to call code that you would like to run once per frame. Normally in NBS the system interrupt is disabled because we **cannot** guarantee that the sysvars that are used by the system interrupt will be available when the interrupt is called.

This means that `FRAMES`, and **ROM keyboard routines** are not available in the music interrupt. To simulate a `FRAMES` counter you could implement your own like so:

```Example
'!org=32768

#define CUSTOMISR                               ' we will be using a custom interrupt routine 
#define NOAYFX                                  ' we dont need any of the AY sound system 
#define IM2                                     ' We will be using interrupt IM2 
#define NEX                                     ' Making a NEX 
#include <nextlib.bas>                          ' include the nextlib 
#include <nextlib_ints.bas>                     ' if we're using interrupts we need this library too

' set a global variable that will be incremented by the ISR

dim c       as ubyte = 0 

' set up the interrupt routine (note it will start immediately)

SetUpIM()					' set up the interrupt routine, and call MyCustomISR()

do 

    WaitRaster(192)             ' wait for raster line 192
    print at 0,0; c             ' print the value of c to the screen
    
loop 

sub MyCustomISR()
    
    ' code inside this function will be called once per frame

    c = c + 1                     ' increment the value of c

end sub 
```

## Notes

You will note that we have to disable the AY sound system ``#define NOAYFX`` if we **just** want to use a custom routine on its own, and not with the music player. Remember to include ``#define CUSTOMISR`` - These must go before the ``#include <nextlib.bas>`` line.

## Requires:
```
#define CUSTOMISR           ' Use a custom ISR
#define NOAYFX              ' No AYFX
#define IM2                 ' Use IM2
#define NEX                 ' Make a NEX
#include <nextlib.bas>      
#include <nextlib_ints.bas> 
```

## Links 


- [InitMusic()](InitMusic.md)
- [InitSFX()](InitSFX.md)
- [PlaySFX()](PlaySFX.md)
- [SetUpIM()](SetUpIM.md)
- [EnableSFX()](EnableSFX.md)
- [EnableMusic()](EnableMusic.md)
- [DisableSFX()](DisableSFX.md)
- [DisableMusic()](DisableMusic.md)
- [LoadSDBank()](LoadSDBank.md)
