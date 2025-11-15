# Kempston Joystick ($xx1F)

## Port Information

| Property | Value |
|----------|-------|
| **Port Number** | $xx1F |
| **Decimal** | 31 |
| **Bit Mask** | %---- ---- 0001 1111 |
| **Readable** | Yes |
| **Writable** | No |
| **Subsystem** | Input |

## Description

Reads movement of joysticks using Kempston interface.

## Port Data Format

| Bit | Function | Kempston Joystick | MD Controller |
|-----|----------|-------------------|---------------|
| **7** | 0 | - | Start button |
| **6** | 0 | - | A button |
| **5** | Fire 2 | Fire 2 | C button |
| **4** | Fire 1 | Fire 1 | B button |
| **3** | Up | Up | Up |
| **2** | Down | Down | Down |
| **1** | Left | Left | Left |
| **0** | Right | Right | Right |

**For all bits: 0 = not pressed / 1 = pressed**

## Controller Support

### Standard Kempston Joystick
- **Bits 0-4**: Direction (Up/Down/Left/Right) and Fire buttons
- **Bits 5-7**: Always read as 0

### Mega Drive (MD) Controllers
- **Full 6-button support** for compatible controllers
- **Additional buttons**: A, B, C, Start mapped to upper bits
- **Core 3.1.4+**: X/Y/Z/Mode buttons not read by FPGA

## Important Notes

### Button Mapping Changes (Core 3.1.4+)
Since core 3.1.4:
- **Fire 1** is confirmed as "B" button (not "C" as some documentation stated)
- **X/Y/Z/Mode buttons** of 6-button controllers are not read by the FPGA
- Previous documentation mentioning "C" button for Fire 1 was incorrect

### Software Compatibility
**Important for non-programmers**: The Next board reads all available buttons (Fire1/B, Fire2/C, A, Start) and provides their state through this port, but this **does not guarantee software will respond** to extra buttons.

#### Legacy Software Limitations
- **Majority of legacy software** was designed for single fire button joysticks
- **Fire 2 support** appeared very late in ZX Spectrum's lifecycle
- **Multi-button support** requires specific game code or patches

#### Modern Support Requirements
For full MD controller support, software needs:
- **Explicit multi-button code** in new ZX Next productions
- **Patched versions** of legacy games
- **Awareness of extended button set** in game design

## Usage Examples

### Read Basic Joystick State
```assembly
IN A, ($1F)         ; Read joystick port
AND %00011111       ; Mask off unused bits
; Now test individual bits:
; bit 0 = right, bit 1 = left
; bit 2 = down, bit 3 = up, bit 4 = fire1
```

### Test Specific Directions
```assembly
; Check if moving right
IN A, ($1F)
BIT 0, A
JR NZ, moving_right

; Check if moving up
IN A, ($1F)
BIT 3, A
JR NZ, moving_up

; Check diagonal movement (up-right)
IN A, ($1F)
AND %00001001       ; Test up and right bits
CP %00001001        ; Both pressed?
JR Z, moving_up_right
```

### Test Fire Buttons
```assembly
; Test primary fire button (Fire 1/B)
IN A, ($1F)
BIT 4, A
JR NZ, fire1_pressed

; Test secondary fire button (Fire 2/C)
IN A, ($1F)
BIT 5, A
JR NZ, fire2_pressed
```

### Test MD Controller Extra Buttons
```assembly
; Test A button (MD controllers)
IN A, ($1F)
BIT 6, A
JR NZ, a_button_pressed

; Test Start button (MD controllers)
IN A, ($1F)
BIT 7, A
JR NZ, start_pressed
```

### Complete Button Reading
```assembly
joystick_read:
    IN A, ($1F)         ; Read full joystick state
    LD B, A             ; Store in B for processing
    
    ; Test directions
    BIT 0, B
    CALL NZ, handle_right
    BIT 1, B  
    CALL NZ, handle_left
    BIT 2, B
    CALL NZ, handle_down
    BIT 3, B
    CALL NZ, handle_up
    
    ; Test fire buttons
    BIT 4, B
    CALL NZ, handle_fire1
    BIT 5, B
    CALL NZ, handle_fire2
    
    ; Test MD extra buttons
    BIT 6, B
    CALL NZ, handle_a_button
    BIT 7, B
    CALL NZ, handle_start
    
    RET
```

## Joystick Configuration

### Port Assignment
Joysticks can be configured via:
- [Peripheral 1 Register](peripheral_1_register.md) ($05) - Basic joystick mode selection
- **NMI Menu**: Settings → Joysticks for hardware configuration
- **Boot Menu**: Joystick port configuration

### Supported Controller Types
- **Standard Kempston** joysticks (5 inputs: 4 directions + 1 fire)
- **Mega Drive** 3-button controllers
- **Mega Drive** 6-button controllers (partial support)
- **Compatible** third-party controllers

## Programming Guidelines

### Multi-Button Game Design
```assembly
; Example: Game with multiple actions
check_buttons:
    IN A, ($1F)
    
    ; Primary actions (all games should support)
    BIT 4, A            ; Fire 1/B - primary action
    CALL NZ, primary_fire
    
    ; Secondary actions (enhanced games)
    BIT 5, A            ; Fire 2/C - secondary action  
    CALL NZ, secondary_fire
    BIT 6, A            ; A button - special action
    CALL NZ, special_action
    BIT 7, A            ; Start - pause/menu
    CALL NZ, pause_game
    
    RET
```

### Legacy Compatibility
```assembly
; Ensure compatibility with single-button games
legacy_fire_check:
    IN A, ($1F)
    AND %00010000       ; Test only Fire 1/B button
    RET Z               ; Return if not pressed
    ; Handle fire button press
    CALL fire_action
    RET
```

## Related Ports

- [Kempston Joystick 2, Joystick I/O](kempston_joystick_2_joystick_io.md) ($xx37) - Secondary joystick
- [Peripheral 1 Register](peripheral_1_register.md) ($05) - Joystick mode configuration  
- [Extended MD Pad Buttons](extended_md_pad_buttons.md) ($B2) - Additional MD button reading

## Hardware Notes

### Connection Types
- **DB9 connector** standard for most controllers
- **Mega Drive controllers** directly compatible
- **Adapters available** for other controller types

### Button Response
- **Immediate response** - no polling required
- **Hardware debouncing** handled by controller
- **Multiple buttons** can be pressed simultaneously

## Compatibility Matrix

| Controller Type | Directions | Fire 1 | Fire 2 | A | Start | X/Y/Z/Mode |
|-----------------|------------|---------|---------|---|-------|------------|
| Standard Kempston | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| MD 3-button | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| MD 6-button | ✓ | ✓ | ✓ | ✓ | ✓ | ✗* |

*X/Y/Z/Mode buttons not read by FPGA since core 3.1.4