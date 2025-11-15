---
name: 'InitPalette(pallete_sel[, bank, start index, number of colours, offset in bank])'
prefix: InitPalette
description: 'Uploads a palette to the selected palette system see [InitPalette](initpalette.md). You can this command with only the first parameter set, the rest will be set to 0 (default).'
---

```
InitPalette(${1|ULA_PALETTE_P1,ULA_PALETTE_P2,L2_PALETTE_P1,L2_PALETTE_P2,SPR_PALETTE_P1,SPR_PALETTE_P2,TILE_PALETTE_P1,TILE_PALETTE_P2|},${2:0},${3:0},${4:0},${5:0})
```
