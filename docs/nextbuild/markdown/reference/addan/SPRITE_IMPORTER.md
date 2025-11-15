# Sprite Importer

- [Sprite Importer](#sprite-importer)
  - [Overview](#overview)
  - [Uasage](#uasage)
  - [The Importer](#the-importer)
    - [Control Bar](#control-bar)
    - [Image Preview](#image-preview)
    - [Extracted Palette](#extracted-palette)
    - [Keyboard Shortcuts](#keyboard-shortcuts)
  - [Using in NextBuild](#using-in-nextbuild)
      - [Example 1 - Using an exported sprite sheet that was 64x64](#example-1---using-an-exported-sprite-sheet-that-was-64x64)
  - [File Format](#file-format)
  - [Related Functions](#related-functions)
    - [Links](#links)


## Overview

You can launch the `Sprite Importer` from the `command palette` by pressing `ctrl+shift+p` and typing `Sprite Importer`.

## Uasage 

The `Sprite Importer` is a tool for importing sprite files into the NextBuild project. It supports the following formats:
- `.spr` - Sprite file
- `.png` - PNG file
- `.bmp` - BMP file
- `.jpg` - JPG file
- `.gif` - GIF file
- `.webp` - WebP file

The `Sprite Importer` can also convert images into the following formats:
 - `nxi` : 256x192 x 256
 - `nxi` : 320x256 x 256
 - `nxi` : 640x256 x 16 **not currently supported**

## The Importer
```
┌──────────────────────────────────────────┐
│ 1 Control Bar                            │
├───────────────┬──────────────────────────┤
│ 2             │                          │
│               │                          │
│ Image Preview │                          │
│               │                          │
├─────────┬─────┘                          │
│ 3       │                                │
│ Select  │                                │
│         │                                │
├─────────┴───────┐                        │
│ 4 Sprite List   │                        │
├─────────────────┤                        │
│ 5 Palette       │                        │
├─────────────────┘                        │
└──────────────────────────────────────────┘
```
1. Control bar containing the action buttons 
2. Image Preview or the currently loaded image
3. Selected sprite 
4. Sprite List 
5. Extracted Palette 
   
### Control Bar 

Running from left to right you will see 
 - `Load New Image` : Load a new image from the file system
 - `Convert to NXI` : Convert the currently loaded image to a NXI file
 - `Otput Options` 
  - `Sprite` : 16x16 
  - `Tile` : 8x8 
- Bit Depth
  - `8` : 8 bit (256 colours)
  - `4` : 4 bit (16 colours)
- `Grid W/H` : Grid size of the total number of sprites or tiles 
- `Sprite Size` : Custom sprite size 
  - `Save to actual size ` : This will always pad the sprite to 16x16 or 8x8 boundary. 
- `Show Grid` : Show a cell grid on the import image 
- `Cell W/H` : Size of the cell grid (defaults to 16x16)
- `Load Target Palette` : Load a `.pal` file to use as the target palette for the conversion.
- 

### Image Preview 

This will display the currently loaded image. You can use the mouse to select a sprite or tile.
 - `Left Click` : Capture sprite and add to the selection preview
 - `Right Drag` : Change capture size, starts from the top left corner of the image
 - `Mouse Wheel` : Zoom in and out of the image
 - `cursor keys` : Move the selection preview
 - `space` : Select the current selection
 - `Numpad cursor keys` : Change the cell size 
 - `tab` : grab the sprite and move to the next grid position. This is so you can select multiple sprites and move them to the next grid position. **Note** you must have `Block Capture Mode` enabled to use this feature.

Following the `Image Preview` you will see : 
 - `Add Selection to List` : Add the current selection to the sprite list
 - `Export Sprite Sheet` : Export the current selection as a sprite shet, this good for saving panels used with [DrawImage](DRAWIMAGE.md)
 - `Export as Block` : 

Once you have sleected a sprite or tile you you will see it appear in the `Selection Preview` if you are happy with the selection you can click the `Add to Sprite List` button to add it to the sprite list.

### Extracted Palette 

Below the `Sprite list` you will see the `Extracted Palette` this is the palette that has been extracted from the image. This is useful for 16 colour images. You can load this palette back in when importing new sprites. 

### Keyboard Shortcuts 

## Using in NextBuild

#### Example 1 - Using an exported sprite sheet that was 64x64
 
```nextbuild
' Load the image into bank 32
LoadSDBank("pirate-win.nxi",0,0,0,32)  

' draw the image to the screen 0,0 - with frame 0 (frame 0 is the first frame of the image)
DrawImage(0,0,@image_pirate,0)

' Define the image in the bank
image_pirate:
    asm
        ; bank  spare  width  height 
        db  32, 64, 64
        ; offset in bank, if the image contains dimension as the first 2 bytes then you can omit the first 2 bytes
        dw 2
    end asm 
```

## File Format

## Related Functions


### Links 

[Editor Index](EDITORS_INDEX.md)
[Index](index.md)