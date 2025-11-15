# COPPER_DATA_NR_60

## Syntax

```
COPPER_DATA_NR_60 = $60
```

## Description

**COPPER DATA** (W)

More info : https://wiki.specnext.dev/Copper_Data

Used to upload code to the [Copper](https://wiki.specnext.dev/Copper).

After the write, the index is auto-incremented to the next memory position. The index wraps to zero when the last BYTE of program RAM is written (position 2047).

Each Copper instruction is composed by two bytes (16 bits) - two writes are required to complete one instruction upload.

Requires: 

	#INCLUDE <nextlib.bas>
