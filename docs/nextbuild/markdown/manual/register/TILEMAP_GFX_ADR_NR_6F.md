# TILEMAP_GFX_ADR_NR_6F

## Syntax

```
TILEMAP_GFX_ADR_NR_6F = $6F
```

## Description

**TILE DEFINITIONS BASE ADDRESS REGISTER** (R/W)

More info : hhttps://wiki.specnext.dev/Tile_Definitions_Base_Address_Register

Base address of the tiles' graphics.

	 bits 7-6 ' Read back as zero, write values ignored
	 bits 5-0 ' bits 5-0 = MSB of address of the tile definitions in Bank 5

The value written is an offset into Bank 5 allowing [tile definitions](https://wiki.specnext.dev/Tilemap) to be placed at any multiple of 256 bytes.

Writing a physical MSB address as $40-$7F or $C0-$FF range is permitted (the top bits will be ignored).

The value read back may be treated as a full 8-bit value (with the top two bits equal to zero), i.e. upon writing value $EB the read of this register will produce value $2B (contrary to "reserved" bits in other registers, where read-value should be not assumed by code using it and masking by AND is recommended).

Default value after soft reset corresponds to the address **$4C00**, i.e. default value is **$0C**.  

Requires: 

	#INCLUDE <nextlib.bas>
