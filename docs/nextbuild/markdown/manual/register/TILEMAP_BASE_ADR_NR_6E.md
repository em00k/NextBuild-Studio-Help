# TILEMAP_BASE_ADR_NR_6E

## Syntax

```
TILEMAP_BASE_ADR_NR_6E = $6E
```

## Description

**TILEMAP BASE ADDRESS REGISTER** (R/W)

More info : https://wiki.specnext.dev/Tilemap_Base_Address_Register

Base address of the 40x32 or 80x32 tile map (similar to text-mode of other computers).

	bits 7-6 ' Read back as zero, write values ignored
	 bits 5-0 ' MSB of address of the tile map in Bank 5

The value written is an offset into Bank 5 allowing the [tilemap](https://wiki.specnext.dev/Tilemap) to be placed at any multiple of 256 bytes.

Writing a physical MSB address as $40-$7F or $C0-$FF range is permitted (the top bits will be ignored).

The value read back may be treated as a full 8-bit value (with the top two bits equal to zero), i.e. upon writing value $45 the read of this register will produce value $05 (contrary to "reserved" bits in other registers, where read-value should be not assumed by code using it and masking by AND is recommended).Default value after soft reset corresponds to the address **$6C00**, i.e. default value is **$2C**.

Requires: 

	#INCLUDE <nextlib.bas>
