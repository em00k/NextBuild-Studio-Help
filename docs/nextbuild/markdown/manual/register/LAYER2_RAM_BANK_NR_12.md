# LAYER2_RAM_BANK_NR_12

## Syntax

```
LAYER2_RAM_BANK_NR_12 = $12
```

## Description

**LAYER 2 RAM PAGE REGISTER** More info : https://wiki.specnext.dev/Layer_2_RAM_Page_Register

Note that this register uses the 16kiB bank method, so if you set Nextreg $12,$C if you need to read the contents via 8kb banks you would need to multiply x 2 (16k bank $0C is identical to 8k pages $18 and $19).

Bits 6-0 store the number of the "SRAM page" (ie, bank) used for the standard Layer 2 screen. The default is 8. Because the layer 2 screen is 48kiB, it actually occupies 3 banks, and the number set here is the first; so by default, it occupies banks 8-10. Then later NextZXOS does reconfigure both this and shadow bank to 9 (banks 9-11). (bit 7 is reserved, use always 0)

For shadow bank paging see Layer_2 and Layer 2 RAM Shadow Page Register ($13).

Valid values are 0 to 109 (with 2MiB SRAM memory extension, 0 to 45 with default 1MiB memory).

The new 320x256x8 and 640x256x4 Layer 2 modes require 80kiB of memory, i.e. five 16k banks. The valid values are then 0 to 107 (2MiB extended) or 0 to 43 with default 1MiB model.

Requires: 

	#INCLUDE <nextlib.bas>
