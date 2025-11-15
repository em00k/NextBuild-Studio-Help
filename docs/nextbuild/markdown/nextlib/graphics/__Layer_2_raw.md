# Layer 2

## Notice

> **Work in Progress**
>
> This page is a work in progress. It is not complete and may contain errors. For now, please refer to [the official Layer 2 documentation](https://wiki.specnext.dev/Layer2) where this information is taken from.

---

## Overview

Layer 2 provides an additional screen layer at:
- **256x192** (256 colours)
- **320x256** (256 colours)
- **640x256** (16 colours)

In these modes, every pixel is individually coloured. Layer 2 may appear in place of, behind, or above the ULA-generated/Tilemap layer.

- The Layer 2 screen occupies **48kiB** or **80kiB**, stored in 3 (or 5) consecutive banks.
- By default, banks **9-11** are used for the visible and "shadow" Layer 2 screen (the HW after power-on defaults to 8-10 for displayed and 11-13 for shadow screen, but that gets modified by NextZXOS booting up).
- These can be set using:
  - `Layer 2 RAM Page Register` (`$12`)
  - `Layer 2 RAM Shadow Page Register` (`$13`)

> **Note:** Avoid banks 5, 7, and 8 for Layer 2 screen unless you are familiar with SRAM/BRAM and ULA screen memory handling in the Next's FPGA.

Each pixel of Layer 2 is assigned **1 byte of video memory** (in 8bpp modes):
- **256x192**: 48kiB (3 banks of 16kiB)
- **320x256/640x256**: 80kiB (5 banks of 16kiB)

### Bank Layout
- **256x192**: Divided horizontally into 3 banks of 64 lines each (16kiB per bank)
- **320x256/640x256**: Divided vertically into 5 banks of 64 (128) columns each

---

## Layer 2 Control

Layer 2 is controlled via:
- `Layer 2 Access Port` (`$123B` / `4667`)
- `Layer 2 Control Register` (`$70`)

The port is bit-mapped as follows:

| Bit | Description |
|-----|-------------|
| 7-6 | Video RAM bank select (write/read paging) |
| 5-4 | Reserved, write 0 |
| 3   | Use Shadow Layer 2 for paging - `Layer 2 RAM Shadow Page Register` (`$13`) |
| 2   | Enable Layer 2 read-only paging |
| 1   | Layer 2 visible - `Layer 2 RAM Page Register` (`$12`) |
| 0   | Enable Layer 2 write-only paging |

> Since core 3.0, this bit has a mirror in `Display Control 1 Register` (`$69`).

---

## Paging and Memory Mapping

- When **bit 0** of `$123B` is set to 1, the appropriate area of Layer 2 video memory (as set by bits 6-7) is accessed by writes into slot 1 (`$0000-$3fff`).
  - **Note:** You cannot read Layer 2 via this mapping; reads return ROM/RAM as usual.
- When **bit 2** is set to 1 (core 3.0+), `$0000-$3fff` is remapped for read, allowing read access into Layer 2 bank selected by bits 3, 6, and 7 (writes still go to regular ROM/RAM).
- With **bits 0 and 2** set, you create alternative read+write mapping of RAM (like MM0+MMU1 registers).

> **Special Memory Note:**
> Bank 5 and first half of Bank 7, when accessed by regular means, are overshadowed by fast BRAM for ULA/Tilemap graphics. Layer 2 mapping circumvents this, accessing main SRAM. Avoid using bank 5, 7, and 8 for Layer 2 unless you know what you're doing.

### Bank Selection
- **Bits 6 and 7**: Select which third of Layer 2 is mapped (0..2)
- **Value 3** (core 3.0+): Whole 48kiB of Layer 2 is mapped into `$0000-$bfff` (be careful with code, stack, and interrupts)

### Bank Offset Feature (core 3.x)
- Set bank-offset variable (0..7) by writing value 16..23 to the port (bit 4 set)
- Example: If first bank is 9, and you use value 21 (+5 offset), bank 14 (9+5) is mapped into `$0000..$3FFF`
- This allows mapping full 80kiB of pixel data into the bottom 16kiB/48kiB window

---

## Layer 2 Control Register (`$70`)
- Select Layer 2 mode
- Modify palette offset (added to top four bits of each pixel)
- Set up Layer 2 clip window for each mode (`Clip Window Layer 2 Register` (`$18`))

---

## Accessing Layer 2 Memory

- You can use regular banking ports to switch in one of the Layer 2 banks in slot at `$C000` (or use ZX Next MMU registers to map RAM elsewhere)
- This allows normal read/write access
- Write to Layer 2 via slot 1 for convenience and fast graphics data copying

---

## Pixel Layout

- **256x192 mode:**
  - Pixels in English reading order, no ULA-style interlacing
  - 256 pixels per line
  - Upper byte of address = Y coordinate (within selected third)
  - Lower byte = X coordinate

- **320x256 (8bpp) mode:**
  - Pixels stored top-to-bottom, left-to-right
  - 256 pixels per column
  - Upper byte of address = X coordinate (for a range)
  - Lower byte = Y coordinate
  - 80kiB total pixel memory (5 banks)

- **640x256 (4bpp) mode:**
  - Same as 320x256, but each byte = 2 pixels (top nibble = left, bottom nibble = right)

---

## Tips & Notes

- **Clear Layer 2** before drawing; it may contain random data at startup.
- **Scrolling:** Use `Layer 2 X Offset Register` (`$16`), `Layer 2 X Offset MSB Register` (`$71`), and `Layer 2 Y Offset Register` (`$17`).
- **Visibility:** Since core 3.0, Layer 2 visibility is not affected by ZX128 ULA-shadow (Bank 7) screen.
- **Performance:** (Obsolete for core 3.0+) Visible Layer 2 would slow CPU to 7MHz.

---

## Double Buffering

To use a double-buffered scheme for Layer 2:
- `Layer 2 RAM Page Register` (`$12`) is **display related** (change to display new Layer 2 when ready, or modify during frame to compose from various memory areas)
- `Layer 2 RAM Shadow Page Register` (`$13`) is **write-over-ROM paging** only (Layer 2 Access Port `$123B` / `4667`) 