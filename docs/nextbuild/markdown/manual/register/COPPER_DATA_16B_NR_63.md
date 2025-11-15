# COPPER_DATA_16B_NR_63

## Syntax

```
COPPER_DATA_16B_NR_63 = $63
```

## Description

**COPPER DATA 16-BIT WRITE REGISTER** (W)

[More info](https://wiki.specnext.dev/Copper_Data_16-bit_Write_Register)

Used to upload code to the [Copper](https://wiki.specnext.dev/Copper)

Similar to [Copper Data ($60)](https://wiki.specnext.dev/Copper_Data), allows to upload Copper instructions to the copper memory, but the difference is that writes are committed to copper memory in 16-bit words (only half-written instructions by using NextReg $60 may get executed, $63 prevents that).

The first write to this register is MSB of Copper Instruction destined for even copper instruction address.

The second write to this register is LSB of Copper Instruction destined for odd copper instruction address.

After any write, the copper address is auto-incremented to the next memory position.

After a write to an odd address, the entire 16-bits are written to Copper memory at once.

Requires: 

	#INCLUDE <nextlib.bas>
