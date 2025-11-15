# AYFX Audio Effects Editor

- [AYFX Audio Effects Editor](#ayfx-audio-effects-editor)
  - [Overview](#overview)
  - [Uasage](#uasage)
  - [The Editor](#the-editor)
    - [Control Bar](#control-bar)
    - [Tone Entry](#tone-entry)
    - [Note Entry](#note-entry)
    - [Keyboard Shortcuts](#keyboard-shortcuts)
    - [Multi-Channel Support (WIP Not complete)](#multi-channel-support-wip-not-complete)
    - [Audio Editing](#audio-editing)
    - [Keyboard Shortcuts](#keyboard-shortcuts-1)
    - [File Operations](#file-operations)
  - [Using in NextBuild](#using-in-nextbuild)
  - [File Format](#file-format)
  - [Credits](#credits)
  - [Related Functions](#related-functions)
    - [Links](#links)


## Overview

The AYFX Audio Effects Editor is a port of Remy Sharp's javascript conversion from the original AYFX. It uses the AYFX format developed by Shiru for creating compact, efficient sound effects that can be played using the AY-3-8910 sound chip. 

**At the moment, multichannel is not fully functional**

## Uasage 

The editor can be opened by clicking on an ```.afb``` file in the explorer or using the ```Command Palette``` which you can open by pressing ```ctrl+shift+p``` and typing ```AYFX```. You will see options to create a new bank or open an existing bank.

## The Editor
```
┌──────────────────────────────────────┐
│ AYFXEditor  Play Copy Paste..     1  │
├──────────────────────────────────────┤
│Pos T N Tone Noise Vol  ─T─── N── V── │
│ 0  / -  02E   00   0F  ─────  ──  ── │
│ 1  / -  04A   00   0F  ─────  ──  ── │
│ 2  / -  05C   00   0F  ─────  ──  ── │
│ 3  / /  06F   10   0F  ─────  ──  ── │
│                                   2  │
├──────────────────────────────────────┤
│ Musical                              │
│ Notes                             3  │
│                                      │
└──────────────────────────────────────┘
```
1. Control bar containing the action buttons 
2. Tone1 entry panel 
3. Virtual keyboard and octave selector
   
### Control Bar 

Running from left to right you will see 
- Effect Name 
- Curret effect number being edited of ```Total effects```
- Single channel mode (others are currently disabled)
- The following button
  - Play    Plays the current effect 
  - Copy    Copy the current effect
  - Paste   Paste the effect from the buffer
  - Clear   Clear all values in effect
  - Delete  Deletes the current effect
  - Insert  Inserts a blank effect at the current effect
  - Blank   Inserts an empty ```sample``` (empty row) into the current effect
  - Save    Save the AFB 
  - 
Included is the import function with 4 preset SYFX banks. These sound effects get used ```all``` the time, so using them directly wont make your title stand out. ```Importing``` will ***OVERWRITE*** your current sound effects! Be warned. 

### Tone Entry 

The tone entry is broken in 3 distinct elements.
- `Pos` - The tone position, the last eneabled position will dictate the effect size `0 - 255`
- `Tone` `Tone Bar` - All control the same ```tone``` value `$000 - $2FF`
- `Noise` `Noise Bar` - Control the amount of white noise `$00 - $1F`
- `Vol` Controls the amount of amplitude `$00 - $1F`

You can use your mouse to explore the way in which you can interact with the note entry.

### Note Entry 

```
Keybaord entry : 
Keyboard Keys on the top rom
Associated note on the bottom row
┌────┬─┬─────┬─┬────┬────┬─┬─────┬─┬─────┬──┬───┬───┐
│ Q ││2││ W ││3││ R │ T ││5││ Y ││6││ U ││7││ I │
│   ││ ││   ││ ││   │   ││ ││   ││ ││   ││ ││   │
│ C ││#││ D ││#││ E │ F ││#││ G ││#││ A ││#││ B │
└────┴─┴─────┴─┴────┴────┴─┴─────┴─┴─────┴─┴────┴───┘
```

You can click on the `Musical Notes` keyboard or use keys ``QWERTYU235678`` and notes will begin to record. Pressing ``INSERT`` will enter a break or gap. Press `1` will play the effect. Selecting a row with your mouse near the ```Pos``` counter, you can then use the ``cursor keys`` to to move forward and backwards. 

### Keyboard Shortcuts 
- **F1**: Open this help documentation
- **Arrow Keys**: Navigate through frames
- **Page Up/Down**: Change octave
- **Home/End**: Jump to start/end
- **Space/Enter**: Play current effect or all channels
- **Numpad + / -**: Back and forwards through effects
- **Ctrl X C V**: Make a selection with mouse & shift, then cut copy or paste
- **1**: Play individual channels A
- **Tab**: Switch through elements
- **Q-8**: Enter musical notes
- **N**: Enter noise
- **Delete**: Remove frames (clears selected position)
- **Insert**: Add space at selection (rest)

### Multi-Channel Support (WIP Not complete)
- **3 Tone Channels**: Edit effects for channels A, B, and C simultaneously
- **Channel Modes**: Single, Dual, or Triple channel editing
- **Real-time Preview**: Play individual channels or mixed audio
- **Synchronized Editing**: Optional cursor synchronization across channels

### Audio Editing
- **Tone Control**: Set frequency values for musical notes
- **Noise Control**: Add noise effects (shared across channels)
- **Volume Envelope**: Create dynamic volume changes
- **Note Entry**: Use keyboard or mouse to enter notes
- **Effect Chaining**: Create consecutive effects for complex compositions
- **Realtime**: Hear the tones as you enter
- **Play on the Keyboard**: Enter notes with Q,2,W,3,E,R,5,T,6,Y,7,U,8

### Keyboard Shortcuts

### File Operations


## Using in NextBuild

To use AYFX effects in your NextBuild programs:

```nextbuild
#DEFINE IM2
#INCLUDE <nextlib.bas>

' Load the AYFX bank
LoadSDBank("effects.afb", 40)
InitSFX(40)

' Enable sound effects
EnableSFX

' Play effect number 5
PlaySFX(5)
```

## File Format

AYFX files (.afb) contain banks of up to 256 sound effects. Each effect can contain:
- Tone enable/disable flags
- Noise enable/disable flags  
- Frequency values (0-4095)
- Noise values (0-31)
- Volume levels (0-15)

## Credits

- AYFX routines & PC editor [Shiru](https://shiru.untergrund.net/software.shtml)
- This editor was ported from [Remy Sharp's port to js](https://zx.remysharp.com/audio/) 

## Related Functions

- [InitSFX](InitSFX.md) - Initialize sound effects
- [PlaySFX](PlaySFX.md) - Play a sound effect
- [EnableSFX](EnableSFX.md) - Enable sound effects
- [DisableSFX](DisableSFX.md) - Disable sound effects

### Links 

[Editor Index](EDITORS_INDEX.md)
[Index](index.md)