---
isManualOnly: true
--- 

# Palette Editor

- [Palette Editor](#palette-editor)
  - [Overview](#overview)
  - [Formats supported](#formats-supported)
  - [Usage](#usage)
  - [The Editor](#the-editor)
    - [Control Bar](#control-bar)
    - [Palette Merge Tool](#palette-merge-tool)
    - [Using in NextBuild](#using-in-nextbuild)
    - [Example 1 - Load a palette](#example-1---load-a-palette)
  - [File Format](#file-format)
  - [Further Reading](#further-reading)
  - [Related Functions](#related-functions)
    - [Links](#links)


## Overview

The Palette Editor is a tool for editing ZX Spectrum Next palette files. For more information on palettes see [`Palettes`](PALETTES.md).

## Formats supported

The import format will be detected automatically.

- Import
  - `.pal` : ZX Spectrum Next palette file
  - `.pal` : Jasc Palette file / Gimp Palette file
  - `.rgb` : RGB Palette file

- Export
  - `.pal` : ZX Spectrum Next palette file

## Usage 

 - `Left Click` : Select a colour 
 - `Shift + Left Click` : Select start of range
 - `Right Click` : Select a secondary colour / end of range
 - `T` : Toggle index values 
 - `ctrl+c` : Copy selected colour / range
 - `ctrl+v` : Paste copied colour / range
 
## The Editor
```
┌──────────────────────────────────────┐
│  1 Control Bar                       │
├──────────────────────────────────────┤
│   ┌────────────────┐   ┌──────────┐  │
│   │                │   │ 3        │  │
│   │ 2 Palette      │   └──────────┘  │
│   │                │                 │
│   │                │   ┌──────────┐  │
│   │                │   │ 4        │  │
│   │                │   │          │  │
│   └────────────────┘   └──────────┘  │
│            ┌───────────┐             │
│            │ 5         │             │
│            └───────────┘             │
├──────────────────────────────────────┤
│ 6  Actions                           │
└──────────────────────────────────────┘

```
1. Control bar containing the action buttons 
2. The currently loaded palette / default palette 
3. RGB controls for the selected colour
4. Colour information for the selected colour 
5. Additional colour converted values 
6. Actions for the palette 
   
### Control Bar 

Running from left to right you will see 
   - `Undo / Redo` : Undo / Redo the last action
   - `Default Palette` : Load the default palette
   - `Import...` : Imports palette from a file (multi formats)
   - `Import from image` : Imports palette from an image
   - `Sort Palette` : Sort the palette by colour by `hue`, `saturation`, `brightness`
   - `Generate Gradient` : Generate a gradient palette
   - `Generate Harmonies` : Generate a harmony palette
   - `Reduce Palette` : Reduce the palette to 16 colours

Note the `Save Changes` button is only available if you have made changes to the palette and located in number `4`

### Palette Merge Tool 

This tool allows you to merge spectrum Next palettes together. You can select the target palette index to `merge` into along with the number of colours to `merge` from the source palette.

### Using in NextBuild

Once you have made changes and save the `.pal` file you can use within your programs.
### Example 1 - Load a palette 
```nextbuild

' Load the palette into bank 40
LoadSDBank("palette.pal", 40)

' Upload the palette, all 256 colours will be uploaded
InitPalette(40, L2_PALETTE_1)
```

```



## File Format

AYFX files (.afb) contain banks of up to 256 sound effects. Each effect can contain:
- Tone enable/disable flags
- Noise enable/disable flags  
- Frequency values (0-4095)
- Noise values (0-31)
- Volume levels (0-15)

## Further Reading



## Related Functions

- [InitPalette](InitPalette.md) - Initialize & palette
- [PalUpload](SetPalette.md) - Upload palette
- [Palette](Palette.md) - Palette index


### Links 

[Editor Index](EDITORS_INDEX.md)
[Index](index.md)