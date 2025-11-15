# NextBuild Sprite Editor

- [NextBuild Sprite Editor](#nextbuild-sprite-editor)
  - [Overview](#overview)
  - [Uasage](#uasage)
  - [The Editor](#the-editor)
    - [Control Bar](#control-bar)
    - [Sprite List](#sprite-list)
    - [Palette](#palette)
    - [Sprite Detail](#sprite-detail)
    - [Keyboard Shortcuts](#keyboard-shortcuts)
  - [Using in NextBuild](#using-in-nextbuild)
  - [File Format](#file-format)
    - [Remarks](#remarks)
  - [Further Reading](#further-reading)
  - [Other Editors](#other-editors)
    - [Links](#links)


## Overview

Creating sprite for yoru productions can now be done directly in NextBuild Studio. While its not a complete replacement for a more traditional tool like Pro Motion or Photoshop, it will help bridge the gap for the time when you're writing code and need to make adjustments, confirm sprite patterns and so on (most of the editors in NBS did start out as simple viewers).

## Uasage 

The editor can be opened by clicking on an ```.spr``` file in the explorer or using the ```Command Palette``` which you can open by pressing ```ctrl+shift+p``` and typing ```Sprite```. You will see options to create a new bank or open an existing sprite file.

## The Editor
```
┌──────────────────────────────────────┐
│ Control Panel                     1  │
├──────────────────────────────────────┤
│                                 4    │
│   ┌───────────┐     ┌───────────┐    │
│   │         2 │     │         3 │    │
│   │           │     │           │    │
│   │           │     │           │    │
│   │           │     │           │    │
│   │           │     │           │    │
│   └───────────┘     └───────────┘    │
│                                      │
│                                      │
└──────────────────────────────────────┘
```

1. Control bar containing the action buttons 
2. Sprite Detail 
3. Palette 
4. Sprite List 
   
### Control Bar 

- View mode : Selects the current sprite mode
  - `8-bit` sprites (256 colors)
  - `4-bit` sprites (16 colors)
  - `8x8` font (256 colors)
  - `8x8` tiles (16 colors)
- Brush : Selects the size of the "brush", a grid of sprites
  - `1x1`, `1x2`, `1x3`, `2x1`, `2x2` 
  - `3x1`, `3x2`, `3x3`, `2x6`, `2x4`
- `Palette offset` : Sets the 16 colour palette offset, this is a multiplier from `0 - 15`
- `Scale` : Scales the size of the sprite list 
- `Show grid` : Show or hide the sprite list grid
- `Load Palette` : load a palette file
- `Default palette` : apply the default RGB 8-bit index - I hate this and will probably replace the default with something much nicer....
- `Save Palette` : save the current palette as a `.pal`
- `Merge Palette` : merge the current palette with the default palette

### Sprite List 

The sprite list is a grid of sprites, you can select a sprite by clicking on it. The sprite list is updated as you edit the sprite. For managing sprites you can use the following keys:
- `right click` : Copy a sprite to the clipboard
- `alt+left click` : Paste a sprite from the clipboard
- `insert` : insert a new sprite
- `ctrl+shift+right click` : delete a sprite
- `left right cursors` : move the selected sprite left and right
  
Use the mouse and hold left click to move the sprite around and change the order.
Once a sprite is selected it will appear in the sprite detail panel.

### Palette 

The palette shows all 256 colours in the current sprite mode. You can select a colour by clicking on it. The default palette will always be loaded on startup, and you cannot edit the default palette (as it is meant to match the default palette of the hardware). For this reas when you attempt to make a change, you will be asked if you want to create a new palette, save it then display it. 

- `left click drag` : move a colours order in the palette (swap)
- `ctrl+left click & drag` : will swap two colours in the palette and remap the sprite pixels
- `ctrl+right click & drag` : will copy and drag a colour to a new position in the palette

You can select any colour and use the RGB sliders that are clampe to 0 - 7. You can open the colour picker by clikcing `Edit Colour` in the control bar. To set the `priority` bit, you can use the `Priority` checkbox.

Through the panel you will see the colour the cursor is hovering over. 

### Sprite Detail 

This is where you can edit the sprite. You can use the mouse to move the sprite around and change the order. You can also use the keyboard to move the sprite around.

- `left click` : draw with the primary colour
- `right click` : draw with the secondary colour
- `alt+left or right click` : pick up the primary or secondary colour

Above the sprite detail you will see a number of tranforms buttons, these will work on the entire brush selected, so if you have a 3x3 brush selected, the entire brush will be transformed as one.

- `Flip Horizontal` : flip the sprite horizontally
- `Flip Vertical` : flip the sprite vertically
- `Rotate 90` : rotate the sprite 90 degrees
- `Rotate 270` : rotate the sprite 270 degrees
- `Shift Left` : shift the sprite left
- `Shift Right` : shift the sprite right
- `Shift Up` : shift the sprite up
- `Shift Down` : shift the sprite down
- `Bin` : bin the sprite
- `Paint Can` : fill the sprite with the primary colour

Currently `UNDO` is disabled, but will be added in the future. :-)

**Save your work regularly**

The sprite editor is a work in progress and may not be stable. Please save your work regularly.

### Keyboard Shortcuts 
- **F1**: Open this help documentation

## Using in NextBuild

To use AYFX effects in your NextBuild programs:

```nextbuild
#DEFINE IM2
#INCLUDE <nextlib.bas>

' Load the sprites into bank 40
LoadSDBank("sprites.spr",0,0,0, 40)
' upload 64 sprites to Sprite RAM 
InitSprites2(63,40)
' update the sprites to the screen
UpdateSprites(32,32, 0, 0, 0, 0)
' enable the sprite display
NextReg($15,1)
' wait for a key press
WaitKey()
' disable the sprite display
NextReg($15,0)
```

## File Format

All the following files contain the same type of data, it is merely the way in which it is displayed that determines what type of sprite it is.

- `.spr` : 16x16 pixels
  - 256 colours
  - 16 colours (4-bit) with palette offset
- `.nxt` `.til` : 8x8 tiles 
  - 16 colours (4-bit)
- `.fnt` `.spr` : 8x8 font 
  - 256 colours

There is also `1-bit` tile mode that is identical to classic ZX Spectrum fonts. As there are considerable editors and fonts already available for this format, I have not included it in the editor.

### Remarks 

The *Sprite Editor* is a work in progress, the design layout is *not* optimal so expect some changes in the future.

## Further Reading

- AYFX routines & PC editor [Shiru](https://shiru.untergrund.net/software.shtml)
- This editor was ported from [Remy Sharp's port to js](https://zx.remysharp.com/audio/) 

## Other Editors

- [Editor Index](EDITOR_INDEX.md)

### Links 

[Index](index.md)