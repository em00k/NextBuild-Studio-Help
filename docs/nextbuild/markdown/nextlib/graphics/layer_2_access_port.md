# Layer 2 Access Port ($123B)

## Port Information

| Property | Value |
|----------|-------|
| **Port Number** | $123B |
| **Decimal** | 4667 |
| **Bit Mask** | %0001 0010 0011 1011 ?? |
| **Readable** | Yes |
| **Writable** | Yes |
| **Subsystem** | Layer 2 |

## Description

Enables Layer 2 and controls paging of layer 2 screen into lower memory.

## Port Data Format

### Read or Write-with-bit-4-zero (soft reset = 0)

| Bit | Description |
|-----|-------------|
| **7-6** | **Video RAM bank select (write/read paging)** |
|  | 00 = first 16K of layer 2 in the bottom 16K |
|  | 01 = second 16K of layer 2 in the bottom 16K |
|  | 10 = third 16K of layer 2 in the bottom 16K |
|  | 11 = first 48K of layer 2 in the bottom 48K (since core 3.0) |
| **5** | Reserved, write 0 |
| **4** | 0 |
| **3** | 0 = map [Layer 2 RAM Page Register](layer_2_ram_page_register.md) ($12), 1 = map [Layer 2 RAM Shadow Page Register](layer_2_ram_shadow_page_register.md) ($13) |
| **2** | Enable mapping for memory reads |
| **1** | Layer 2 visible - [Layer 2 RAM Page Register](layer_2_ram_page_register.md) ($12)<br/>Since core 3.0 this bit has mirror in [Display Control 1 Register](display_control_1_register.md) ($69) |
| **0** | Enable mapping for memory writes |

### Write-with-bit-4-set (since core 3.0.7) (soft reset = 0)

| Bit | Description |
|-----|-------------|
| **7-5** | Reserved, write 0 |
| **4** | 1 |
| **3** | Reserved, write 0 |
| **2-0** | 16ki bank relative offset (+0 .. +7) applied to Layer 2 memory mapping |

## Layer 2 Memory Mapping

### Basic Mapping Modes

The Layer 2 screen can be mapped into the Z80's address space for direct memory access:

- **Bits 7-6** select which portion of Layer 2 RAM to map
- **Bit 0** enables write access to the mapped area
- **Bit 2** enables read access to the mapped area
- **Bit 3** selects between main ($12) and shadow ($13) Layer 2 banks

### Display vs Memory Mapping

**Important**: The Layer 2 data being displayed are always driven by [Layer 2 RAM Page Register](layer_2_ram_page_register.md) ($12). The "shadow" register $13 affects only the memory mapping feature (when bit 3 is set), never the display data. To "flip" the data being displayed, write new bank value into register $12.

## Bank Offset Feature (Core 3.0.7+)

The bit 4 = 1 functionality was added in core 3.0.7 together with new Layer 2 display modes:

### Usage Pattern
1. Set up initial mapping like `%00'00'??'1'?` or `%11'00'??'1'?` to map first bank into bottom 16ki or 48ki of memory
2. Switch the mapped bank by writing relative offset value 0..7 to the port with bit 4 set
3. Example: `%0001'0011` modifies mapping to start with fourth (+3) bank of Layer 2

### Extended Mode Support
- Original mapping covered only first three banks (256x192 Layer 2 mode)
- New Layer 2 modes 320x256x8bpp and 640x256x4bpp occupy full five 16kiB banks
- Relative offsetting allows access to any of the five banks even with "first bank into bottom 16ki" mapping

## Usage Examples

### Enable Layer 2 Display
```assembly
LD A, %00000010     ; Enable Layer 2 visibility
LD BC,$123B
OUT (C),A
```

### Map First 16K for Writing
```assembly
LD A, %00000001     ; Map first 16K, enable write
LD BC,$123B
OUT (C),A
; Now write to $0000-$3FFF to access Layer 2
```

### Map Second 16K for Read/Write
```assembly
LD A, %01000101     ; Map second 16K, enable read+write
LD BC,$123B
OUT (C),A
; Access second third of Layer 2 at $0000-$3FFF
```

### Map Full 48K (Core 3.0+)
```assembly
LD A, %11000001     ; Map all 48K, enable write
LD BC,$123B
OUT (C),A
; Access entire Layer 2 at $0000-$BFFF
```

### Use Shadow Bank for Mapping
```assembly
LD A, %00001001     ; Map shadow bank, enable write
LD BC,$123B
OUT (C),A
; Write to shadow bank while display shows main bank
```

### Set Bank Offset (Core 3.0.7+)
```assembly
; First set up base mapping
LD A, %00000001     ; Map first bank, enable write
LD BC,$123B
OUT (C),A

; Then set offset to access 4th bank
LD A, %00010011     ; Bit 4 set, offset +3
LD BC,$123B
OUT (C),A
; Now $0000-$3FFF accesses 4th Layer 2 bank
```

## Layer 2 Display Modes

### 256x192 Mode (Standard)
- Uses 3 16KB banks (48KB total)
- Each bank = 64 lines × 256 pixels
- 1 byte per pixel (8-bit color)

### 320x256 Mode (Core 3.0+)
- Uses 5 16KB banks (80KB total)
- 320×256 pixels
- 1 byte per pixel (8-bit color)

### 640x256 Mode (Core 3.0+)
- Uses 5 banks (80KB total)  
- 640×256 pixels
- 4 bits per pixel (16 colors)

## Important Notes

### Memory Safety
- **Always disable system interrupts** when changing Layer 2 mapping
- **Original mapping** disabling writes will restore mapping to default
- **Be careful with stack placement** when mapping to lower memory

### Read/Write Control
- **Bit 0**: Controls write access to mapped area
- **Bit 2**: Controls read access to mapped area
- **Both can be enabled simultaneously** for full read/write access

### Core Version Dependencies
- **Core 3.0**: Added 48K mapping mode (bits 7-6 = 11)
- **Core 3.0.7**: Added bank offset feature (bit 4 = 1)

## Related Registers

- [Layer 2 RAM Page Register](layer_2_ram_page_register.md) ($12) - Controls displayed bank
- [Layer 2 RAM Shadow Page Register](layer_2_ram_shadow_page_register.md) ($13) - Shadow bank for mapping
- [Layer 2 Control Register](layer_2_control_register.md) ($70) - Display mode control
- [Display Control 1 Register](display_control_1_register.md) ($69) - Layer 2 visibility mirror
