# Memory 

## Table of contents 

- [Memory](#memory)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
- [Terminology](#terminology)
- [Commands for working with banks](#commands-for-working-with-banks)
  - [Example Paging](#example-paging)
  - [Graphic Banks](#graphic-banks)
    - [For 256x192:](#for-256x192)
    - [For 320x256:](#for-320x256)
  - [Traditional Banking](#traditional-banking)
  - [Remarks](#remarks)
    - [ASM mapping](#asm-mapping)
  - [Links](#links)

## Overview 

The ZX Spectrum Next can page in (swap) and out up to 224 8KB memory slots in positions [0-7] of the 64KB of addressable RAM, to expand the range of visible memory the CPU can read & write. This is quite a powerful system giving you access to up to nearly 2MB of RAM (further files can be loaded from SD card too). 

For information on how the memory is sliced up check the [Global Memory Map](GlobalMemory.md). NextBuild's commands support using the extended memory and does most of the heavy lifting meaning you can move things around in memory with simple commands. 

# Terminology 

Traditionally swapping memory banks has been known as `paging`, as you are turning the *page* on the memory for a clean sheet (at least one can imagine). The 128K ZX Spectrum had the ability to page in 16KB from [$c000-$ffff]. The Next supports the traditional (more cumbersome) method but also supports `paging` in banks of memory that are 8KB in size. NextZXOS refers to banks as 16KB slots, and with the two differing sizes people have wanted to have a verbal separation of the two by calling `8KB paging` and `16KB banking`. In NextBuild we almost always will be using 8KB paging, so you will see the two interchanged. 

When working with some components of the Next 16KB banks will be required, such as the [LAYER2_RAM_BANK_NR_12](LAYER2_RAM_BANK_NR_12.md). This means to set Layer2 start RAM bank from 8KB bank 32, the number is / 2. 
```
NextRegA(LAYER2_RAM_BANK_NR12,16)                   ; sets Layer2 RAM start at 8KB 32
```

# Commands for working with banks
A number of commands will take a bank parameter, this means the routine will use that bank as the source location, and does a clean up (stores the current bank, carries out the process, replaces the original bank). 

- [ClearBank](ClearBank.md)
- [CopyBank](CopyBank.md)
- [LoadSDBank](LoadSDBank.md)
- [NextRegA](NextRegA.md)

Manually paging in RAM can be done using the Next Registers: 

- [MMU0_0000_NR_50](MMU0_0000_NR_50.md)
  - $0000-$1fff *slot 0*
- [MMU1_2000_NR_51](MMU1_2000_NR_51.md)
  - $2000-$3fff *slot 1*
- [MMU2_4000_NR_52](MMU2_4000_NR_52.md)
  - $4000-$5fff *slot 2*
- [MMU3_6000_NR_53](MMU3_6000_NR_53.md)
  - $6000-$7fff *slot 3*
- [MMU4_8000_NR_54](MMU4_8000_NR_54.md)
  - $8000-$9fff *slot 4*
- [MMU5_A000_NR_55](MMU5_A000_NR_55.md)
  - $a000-$bfff *slot 5*
- [MMU6_C000_NR_56](MMU6_C000_NR_56.md)
  - $c000-$dfff *slot 6*
- [MMU7_E000_NR_57](MMU7_E000_NR_57.md)

## Example Paging 

Before paging care must be taken that running code isn't in the same slot as that being paged out, and if paging slots [0-2] system interrupts are not being used. Some of the keywords that come with ZX Basic Compiler rely on the SYSVARS being intact (See [System Variables](SystemVariables.md)). For this reason a number of routines have been patched to include a stub file, that always pages in the system default SYSVAR memory bank (bank $0a), and neatly replacing it after the call. 

To swap in bank 32 to slot 7 **[e000-ffff]**
```
NextRegA(MMU7_E000_NR_57,32)
```
similarly, you can specify the register value directly: 

```
NextRegA($57,32)
```
And finally a helper routine that wraps it up:
```
MMU8(7, 32)                 ; page in bank 32 to slot 7
```

## Graphic Banks

To move graphics from memory banks to the screen a number of commands have been included. For drawing software tiles, use ```LoadSDBank``` to load the tile data into memory, and then use the ```DoTilBank8```, ```DoTilBank16``` or ```DoTileBank32``` commands to draw the tile to the screen. 


### For 256x192:
```
DoTilBank8(bank, x, y, tile)        ; draw 8x8 tile from bank (all routines draw to layer2) 8 px
DoTilBank16(bank, x, y, tile)       ; draw 16x16 tile from bank 
DoTileBank32(bank,x, y, tile)       ; draw 32x32 tile 
```
### For 320x256:
```
FDoTilBank8(bank, x, y, tile)       ; draw 8x8 tile from bank
FDoTilBank16(bank, x, y, tile)      ; draw 16x16 tile from bank 
```
See [Graphics](_Graphics.md) for more information

## Traditional Banking 

NextBuild does allow you to page in memory in 16KB chunks at **[$c000-$ffff]** just like the traditional system, on the Next however we are not limited to 7 banks, but can page up to 112 banks

```
MMU16(16)                           ; page in 16KB to [$c000-$ffff]
```

## Remarks 

If you're looking to write the optimal code then it is recommended that you use ```NextReg``` commands inside of an asm block. 

### ASM mapping 
```
asm 
  getreg(MMU0_0000_NR_50)
  ld   b, a
  nextreg MMU0_0000_NR_50, 32     ; map bank 32 to slot 0
  ; do something
  ld   a, b
  nextreg MMU0_0000_NR_50, b      ; restore original bank
end asm 
```

## Links

- [NextRegA](NextRegA.md)
- [NextReg](NextReg.md)
