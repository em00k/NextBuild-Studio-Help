# InitPalette

## Syntax

```
InitPalette(Palette, Bank, Start, NrOfCols, Offset)
```

## Description

Uploads a palette to the selected palette system see [Palettes](palettes.md). You can this command with only the first two parameters set, the rest will be set to 0 (default).

The parameters are as follows:
- Palette: The palette to upload to see [Palettes](palettes.md), available options are:
    - ULA_PALETTE_P1
    - ULA_PALETTE_P2
    - L2_PALETTE_P1
    - L2_PALETTE_P2
    - SPR_PALETTE_P1
    - SPR_PALETTE_P2
    - TILE_PALETTE_P1
    - TILE_PALETTE_P2
- Bank: The bank to upload the palette from
- Start: The start index of the palette, default is 0
- NrOfCols: The number of colours to upload, default is 256
- Offset: The offset index in the palette to upload the palette to, default is 0

## Examples

Upload the palette from bank 32 to the first palette of Layer 2
```
InitPalette(L2_PALETTE_P1, 32)
```
Upload the palette from bank 42, starting at index 16 and uploading 16 colours to the second palette of Layer 2:
```
InitPalette(L2_PALETTE_P2, 42, 16, 16, 16)
```

## Links

* [Layer2](_Layer2.md)
* [ShowLayer2](ShowLayer2.md)
* [Palettes](palettes.md)