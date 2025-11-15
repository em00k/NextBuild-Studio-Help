# ANTI_BRICK_NR_10

## Syntax

```
ANTI_BRICK_NR_10 = $10
```

## Description

Used within the Anti-brick system.

Read:
```

Bit     Effect
7       Reserved
6-2     Core ID
1       Button DRIVE (DivMMC) is pressed
0       Button M1 (Multiface) is pressed 
```
Write:
```
Bit 	Effect
7       Start selected core (reboot FPGA)
6-5 	Reserved, must be 0
4-0 	Core ID 0-31 (default is 2) (only in config mode) * 
```

* A write of an out of range core id is ignored; this is the preferred way to determine max id

Note that in normal running pressing the DivMMC or Multiface button creates an NMI which halts any running program, and the reflashable core must be loaded before any user code is run. This means that unless you are rewriting the entire firmware from scratch this register is probably not useful. 

## Remarks

More info : [https://wiki.specnext.dev/Anti-brick_Register](https://wiki.specnext.dev/Anti-brick_Register)

Requires: 

```
#INCLUDE <nextlib.bas>
```

## Links 

[Index](Index.md)
