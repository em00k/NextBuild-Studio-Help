# LAYER2_RAM_SHADOW_BANK_NR_13

## Syntax

```
LAYER2_RAM_SHADOW_BANK_NR_13 = $13
```

## Description

**LAYER 2 RAM SHADOW PAGE REGISTER** More info : https://wiki.specnext.dev/Layer_2_RAM_Shadow_Page_Register

Sets the bank number where the Layer 2 shadow screen begins.

Bits 6-0 store the number of the "SRAM page" (ie, bank) used for the shadow Layer 2 screen. The default is 11. Because the layer 2 screen is 48kiB, it actually occupies 3 banks, and the number set here is the first; so by default, it occupies banks 11-13. (bit 7 is reserved, use 0)

For shadow bank paging see Layer_2

Valid values are 0 to 109 (with 2MiB SRAM memory extension, 0 to 45 with default 1MiB memory).

Requires: 

	#INCLUDE <nextlib.bas>
