# INITMUSIC

## Syntax

```
InitMusic(player bank, music bank)
```

## Description

Used to initialise a ProTracker 3 ``(.pt3)`` file to be played back on interrupt, that is updated once per frame **(@50 / 60 Hz)**. 

The commannd [SetUpIM()](SetUpIM.md) will automatically set up a system interrupt, call a replyer code to play back the music. Bundled with the player is also a version of Shiru's `AYFXEngine`. First you need to load in the binaries into your chosed banks:

	' -- Loadblock
	LoadSDBank("[]vt24000.bin",0,0,0,38)		' load the music replayer into bank 38
	LoadSDBank("[]music1.pt3",0,0,0,39)			' load music.pt3 into 39
	LoadSDBank("[]game.afb",0,0,0,41)			' load sfx into bank 41

Note the **[]** before the filename tells NBS to load the file from the system assets stored in `Scripts/system_data`. Once these are loaded you can run the initialisation code:

	' --
	InitSFX(41)					' init the SFX engine, sfx are in bank 41
	InitMusic(38,39,0000)		' init the music engine 38 has the player, 39 the pt3, 0000 offset
	SetUpIM()					' init the IM2 code
	EnableSFX					' Enables the AYFX, use DisableSFX to top
	EnableMusic					' Enables Music, use DisableMusic to stop

When you want to play an `AYFX` use the [PlaySFX()](PlaySFX.md) command: 

	PlaySFX(n)					

The `Interrupt Vector` is automatically generated at the start of your code, just after the HEAP and is stored in the library section of the final code. This is aligned to the nearest 256 boundary, because your interrupt vector table should always start on an ALIGNed address e.g : ``$fd00``  

## MyCustomISR 

NBS can also run a user defined `ISR` along side the system interrupt. To do this you need to create a function that will be called by the system interrupt. This function must be called `MyCustomISR` and must be declared as follows:

```
Sub MyCustomISR()
	' Your code here
End Sub
```

Then before you include the `nextlib.bas` file you need to define the `CUSTOMISR` macro, this is done by adding the following line to the top of your code:

```
#DEFINE CUSTOMISR
```

## Requires:
```
#DEFINE IM2
#INCLUDE <nextlib.bas>
#INCLUDE <nextlib_ints.bas>  
```

## Links 

- [InitSFX()](InitSFX.md)
- [PlaySFX()](PlaySFX.md)
- [EnableSFX()](EnableSFX.md)
- [EnableMusic()](EnableMusic.md)
- [DisableSFX()](DisableSFX.md)
- [DisableMusic()](DisableMusic.md)
- [LoadSDBank()](LoadSDBank.md)