# Global Memory Map

## Table of Contents
 - [Memory Introduction](#memory-introduction)
 - [Z80 Visible Memory](#z80-visible-memory)

# Memory Introduction 

The total available RAM space of the Next is 768k on an unexpanded Next, or 1792k on a Next expanded to 2Mb. (The base Next has 1mb of memory but 256k of it is reserved for the ROMs and firmware.)

The Z80 processor in the Next can access only 64k of memory at a time, and so the memory is divided into banks which are used in determining which memory it sees. Spectrum 128k memory management, and NextBASIC, use 16k banks. Next memory management via machine code uses 8k banks.


|16k-bank | 8k-bank |True Address |Size |Description
|:-:|:-:|:-:|:-:|:--|
|- | - | $000000-$00ffff  |64K 	| ZX Spectrum ROM | 
|- | - | $010000-$013fff  |16K 	| EsxDOS ROM |
|- | - | $014000-$017fff  |16K 	| Multiface ROM |
|- | - | $018000-$01bfff  |16K 	| Multiface Extra ROM |
|- | - | $01c000-$01ffff  |16K 	| Multiface RAM |
|- | - | $020000-$03ffff  |128K | DivMMC RAM |
|0-7 |0-15 |$040000-$05ffff |128K |Standard 128K RAM |
|8-15 |16-31 |$060000-$07ffff |128K |Extra RAM|
|16-47 |32-95 |$080000-$0fffff |512K |1st extra IC RAM (available on unexpanded Next) |
|48-79 |96-159 |$100000-$17ffff |512K |2nd extra IC RAM (only available on expanded Next)| 
|80-111 |160-223 |$180000-$1fffff |512K |3rd extra IC RAM (only available on expanded Next)|

Additionally, the first few pages have certain uses and traits summarised below:

|16k-bank | 8k-bank |Description
|:-:|:-:|:--|
|0 | 0-1 |Standard RAM, maybe used by EsxDOS. Initially mapped to $c000-$ffff.|
|1 | 2-3 |Standard RAM, contended on 128, may be used by EsxDOS, RAMdisk on NextZXOS.|
|2 | 4-5 | Standard RAM. Initially mapped to $8000-$bfff.|
|3 | 6-7 | Standard RAM, contended on 128, may be used by EsxDOS, RAMdisk on NextZXOS.|
|4 | 8-9 | Standard RAM, contended on +2/+3, RAMdisk on NextZXOS.|
|5 | 10-11 | ULA Screen, contended except on Pentagon, cannot be used by NextBASIC commands. Initially mapped to $4000-$7fff.|
|6 | 12-13 | Standard RAM, contended on +2/+3, RAMdisk on NextZXOS.|
|7 | 14-15 | ULA Shadow Screen, contended except on Pentagon, NextZXOS Workspace, cannot be used by NextBASIC commands |
|8 | 16-17 | Next RAM, Default Layer 2, NextZXOS screen and extra data, cannot be used by NextBASIC commands |
|9-10 |	18-21 | Next RAM, Rest of default Layer 2 |
|11-13|	22-27 | Next RAM, Default Layer 2 Shadow Screen |

**NOTE** Please note that NextZXOS moves the Layer 2 bank assignments. Therefore, Layer 2, after NextZXOS boots, is mapped to 16k-banks 9-11 (8k-banks 18-23). The Layer 2 shadow memory is also assigned to 16k-banks 9-11 (8k-banks 18-23).
Z80 Visible Memory map

## Z80 Visible Memory

At start up, the 16-bit address space of the Z80 is mapped to memory as follows:

|Area |16k-slot |8k-slot |Default 16k-bank |Default 8k-bank |Description
|:-:|:-:|:-:|:-:|:-:|:--|
|$0000-$1fff |1 |0 |ROM |ROM (255) | Normally ROM. R/W redirect by Layer 2. IRQ and NMI routines here.
|$2000-$3fff |	|1 |ROM |(255) | Normally ROM. R/W redirect by Layer 2.
|$4000-$5fff |2 |2 | 5 	|10 | Normally used for normal/shadow ULA screen.
|$6000-$7fff |	|3 |    |11	| Timex ULA extended attribute/graphics area.
|$8000-$9fff |3	|3 | 2 	|4 	| Free RAM.
|$a000-$bfff |	|5 |  	|5  | Free RAM.
|$c000-$dfff |4	|4 | 0 	|0 	| Free RAM. Only this area is remappable by 128 memory management.
|$e000-$ffff |	|7 |  	|1 	| Free RAM. Only this area is remappable by 128 memory management. 

## Remarks 

The ZX Spectrum Next can page in any of the 8KB memory banks into any slot using [MMU8(s,n)](MMU8.md) or via NextRegs : 

```
#INCLUDE <nextlib.bas>
NextRegA(MMU2_4000_NR_52,22)        ' sets slot 2 (2000-3fff) with bank 22
```

Care needs to be taken that interrupts are correctly handled (NextBuild disables system interrupts on startup).

## Links 

[Memory](Memory.md) 