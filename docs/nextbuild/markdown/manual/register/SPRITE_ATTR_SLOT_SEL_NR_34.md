# SPRITE_ATTR_SLOT_SEL_NR_34

## Syntax

```
SPRITE_ATTR_SLOT_SEL_NR_34 = $34
```

## Description

**SPRITE PORT-MIRROR INDEX REGISTER**

More info : https://wiki.specnext.dev/Sprite_port-mirror_Index_Register

Selects sprite index 0..127 to be affected by writes to other Sprite ports (and mirrors).

If sprite id lockstep in Peripheral 4 Register ($09) is enabled, write to this registers has same effect as writing to Sprite Status/Slot Select ($303B / 12347).

I.e. bit 7 offsets pattern writes by 128 bytes (second half of 0..63 pattern slot), and bits 6-0 contain index 0..63 (for patterns) or 0..127 for sprite attributes, resetting those indices for ports Sprite Attribute Upload ($xx57 / 87) and Sprite Pattern Upload ($xx5B / 91) and for following NextRegs $35..$39 and $75..$79.

Index-increments caused by write to NextRegs $75..$79 will propagate also to current index of port $xx57 and reset current attribute (next write to port $xx57 after index change will modify first byte of attributes).

The index increment caused by sending full attribute set to port $xx57, or by writing to port $303B, will also propagate to this register, affecting next writes to registers $35..$39/$75..$79.

If sprite id lockstep in Peripheral 4 Register ($09) is disabled, bit 7 is ignored and bits 6-0 value selects index 0..127 for NextRegs $35..$39 and $75..$79 (decoupled from ports $xx57/$303B completely).

The read will in every mode return the sprite id (not pattern id) and bit 7 always reads back as zero.

Requires: 

	#INCLUDE <nextlib.bas>
