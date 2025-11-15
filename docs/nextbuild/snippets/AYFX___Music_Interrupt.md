---
name: AYFX & Music Interrupt
prefix: Template
description: >-
  This code will produce a code block for uysing Shiru's AYFX and playing PT3
  files on interrupt. The interrupt is dynamically created.
---

```

' -- Load block 
LoadSDBank("music.pt3",0,0,0,${1|34:line}) 				' load music.pt3 into bank 34
LoadSDBank("vt24000.bin",0,0,0,33) 				' load the music replayer into bank 33
' -- 

InitSFX(36)							            ' init the SFX engine, sfx are in bank 36
InitMusic(${2|34},$1,0000)				            ' init the music engine 33 has the player, 34 the pt3, 0000 the offset in bank 34
SetUpIM()							            ' init the IM2 code 
EnableSFX							            ' Enables the AYFX, use DisableSFX to top
EnableMusic 						            ' Enables Music, use DisableMusic to stop 
'PlaySFX(nr)                                    ' Plays SFX 
```
