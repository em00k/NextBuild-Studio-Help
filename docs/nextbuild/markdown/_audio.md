# Music & Sound FX

The ZX Spectrum Next comes with 3 x AY8910 programmable sound generators that are each capable of producing square tones on 3 seperate channels ```A,B```or ```C``` giving a total of **9** channel AY audio. 

Each chip can be selected by setting the correct value on port ```$FFDD``` 

```
  ' select chip 1
  out $FFDD, $fd 
  ' select chip 2
  out $FFDD, $fe 
  ' select chip 3
  out $FFDD, $ff
```

It is possible to play music using 1 x AY and sounds effects on another. NextBuild comes with commands that assist you in playing music and sound effects together. 

The AY sound module runs on an Interrupt, which means it will carry on playing in the background while the action continues. For the AY sound module to work we need to set this up before hand.

# Example 1 

To play music (```.pt3``` files either 3 or 6 channels) and sound effects (```.afb``` AYFX bank files) you will need the following files :

- Music Player (```ts24000.bin```)
- AYFX Bank    (```.afb```)
- Music File   (```.pt3```)

**Load block:**
First we load the `vt24000.bin` into a memory bank, lets pick bank `33` for this example: 
```
LoadSDBank("vt24000.bin",0,0,0,33)
```
Lets load a music file into bank `34` and sound fx into bank `36`
```
LoadSDBank("shoes.pt3",0,0,0,34) 
LoadSDBank("game.afb",0,0,0,36)
```
These commands instruct NextBuild to include these files in the final `.`NEX` file. Now we Need to issue some commands to start the music module. It is important to call the commands in correct sequence.

Initialise the sounds fx bank as `36`:
```
InitSFX(36)
```
Initialise the music, setting the player bank to `33`, point to music bank 34, and an offet into bank `34` of `0 bytes` (this so we can pack more than one song in a bank):
```
InitMusic(33,34,0000)
```
Now setup the interrupt and *enable* SFX and music:
```
SetUpIM()
EnableSFX
EnableMusicstop 
```
Music should start to play, to play a sound effect from the `.afb` bank:
```
PlaySFX(n)
```
To control audio once playback has started: 

*Disable playback*
```
DisableMusic 
DisableSFX 
```
*Enable playback*
```
EnableMusic
EnableSFX
```

A complete example can be found in the [NextBuild_Examples/SOUND/TurboSoundAYFX/SimpleMusic_SFXbas.bas](/NextBuild_Examples/SOUND/TurboSoundAYFX/SimpleMusic_SFXbas.bas)

# Direct Manipulation 

You can address each of the AY chips independantly using the classic port values: 
```
  ' Select AY chip 1
  out $ffdd, $fd  
  ' AY select register 0-13
  out $ffdd, reg 
  out $bffd, value 

  ' Example of making a tone 
  
    _ay(0, 34)          ' set tone 
    _ay(1, 130)         ' high byte
    _ay(8, 15)          ' set volume 
    _ay(7, %00111110)   ' enable channel A tone, disable noise 

    sub _ay(__a as ubyte,__b as ubyte)
        out $fffd, __a 
        out $bffd, __b 
    end sub 

   do : loop            ' loop forever
```
Each channel can be controlled using the following `registers`:

| Register | Function |
|:--------:|:---------|
| 0        | Channel A Fine Tune |
| 1        | Channel A Coarse Tune (4 bits) |
| 2        | Channel B Fine Tune |
| 3        | Channel B Coarse Tune (4 bits) |
| 4        | Channel C Fine Tune |
| 5        | Channel C Coarse Tune (4 bits) |
| 6        | Noise Period (5 bits) |
| 7        | Tone enable flags.<br>Bits 0 – 2 enable tone on channels A, B, C respectively (inverted: 0 = enabled).<br>Bits 3 – 5 enable noise on A, B, C (inverted similarly). |
| 8        | Channel A amplitude.<br>Bits 0 – 3 set fixed amplitude if bit 4 = 0. If bit 4 = 1, the envelope generator is used instead (bits 0 – 3 ignored). |
| 9        | Channel B amplitude, same as above. |
| 10       | Channel C amplitude, same as above. |
| 11       | Envelope period fine. |
| 12       | Envelope period coarse. |
| 13       | Envelope shape bits:<br>- **Bit 0 “Hold”**: 1 = one cycle then hold end value; 0 = continuous cycles.<br>- **Bit 1 “Alternate”**: 1 = alternate direction each cycle; 0 = reset each cycle. If Hold=1, chooses whether to hold final (0) or initial (1) value.<br>- **Bit 2 “Attack”**: 1 = count up; 0 = count down.<br>- **Bit 3 “Continue”**: 1 = follow Hold; 0 = perform one cycle then drop amplitude to 0 (overrides Hold). |

