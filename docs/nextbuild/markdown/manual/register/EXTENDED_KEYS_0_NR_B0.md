# EXTENDED_KEYS_0_NR_B0

## Syntax

```
EXTENDED_KEYS_0_NR_B0 = $B0
```

## Description

EXTENDED_KEYS_0_NR_B0 = $B0

|Number=$B0
|Readable=Yes
|Writable=No
|ShortDesc=Read Next keyboard compound keys separately

| Bit || Description |
|-
| 7 || 1 if ; pressed |
|-
| 6 || 1 if " pressed |
|-
| 5 || 1 if , pressed |
|-
| 4 || 1 if . pressed |
|-
| 3 || 1 if UP pressed |
|-
| 2 || 1 if DOWN pressed |
|-
| 1 || 1 if LEFT pressed |
|-
| 0 || 1 if RIGHT pressed |

  * Nextreg 0x68 bit 4 stops extended keys from making entries in the 8x5 matrix

More info : https://wiki.specnext.dev/Extended_Keys_0_Register

Requires: 

	#INCLUDE <nextlib.bas>
