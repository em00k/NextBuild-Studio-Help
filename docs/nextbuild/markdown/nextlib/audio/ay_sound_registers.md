# AY Sound Chip Registers

## Register Overview

The AY-3-8912 sound chip provides 3 channels of tone generation, noise generation, and envelope control. Registers are accessed via [Sound Chip Register Write](sound_chip_register_write.md) ($BFFD) after selecting the register with [Turbo Sound Next Control](turbo_sound_next_control.md) ($FFFD).

| Register | Function |
|----------|----------|
| 0 | Channel A Fine Tune |
| 1 | Channel A Coarse Tune (4 bits) |
| 2 | Channel B Fine Tune |
| 3 | Channel B Coarse Tune (4 bits) |
| 4 | Channel C Fine Tune |
| 5 | Channel C Coarse Tune (4 bits) |
| 6 | Noise Period (5 bits) |
| 7 | Tone enable flags |
| 8 | Channel A amplitude |
| 9 | Channel B amplitude |
| 10 | Channel C amplitude |
| 11 | Envelope period fine |
| 12 | Envelope period coarse |
| 13 | Envelope shape |

## Detailed Register Descriptions

### Registers 0-5: Tone Generation

#### Channel Frequency Control
- **Registers 0,1**: Channel A frequency (12-bit value)
- **Registers 2,3**: Channel B frequency (12-bit value)  
- **Registers 4,5**: Channel C frequency (12-bit value)

**Fine tune registers** (0,2,4): Lower 8 bits of frequency value
**Coarse tune registers** (1,3,5): Upper 4 bits of frequency value (bits 0-3 only)

**Frequency calculation**: `Tone Period = Clock Frequency / (16 × Register Value)`

### Register 6: Noise Period (5 bits)

Controls the frequency of the noise generator. Only bits 0-4 are used.

**Noise frequency**: `Noise Period = Clock Frequency / (16 × Register Value)`

### Register 7: Tone/Noise Enable Flags

| Bit | Function | Logic |
|-----|----------|-------|
| 0 | Channel A tone enable | 0 = enabled, 1 = disabled |
| 1 | Channel B tone enable | 0 = enabled, 1 = disabled |
| 2 | Channel C tone enable | 0 = enabled, 1 = disabled |
| 3 | Channel A noise enable | 0 = enabled, 1 = disabled |
| 4 | Channel B noise enable | 0 = enabled, 1 = disabled |
| 5 | Channel C noise enable | 0 = enabled, 1 = disabled |
| 6-7 | Unused | - |

**Note**: Enable bits are **inverted** - 0 means enabled, 1 means disabled.

### Registers 8-10: Channel Amplitude

Controls the volume and envelope settings for each channel.

| Bit | Function |
|-----|----------|
| 0-3 | Fixed amplitude level (0-15) |
| 4 | Amplitude mode: 0 = fixed, 1 = envelope |
| 5-7 | Unused |

- **Bit 4 = 0**: Use fixed amplitude from bits 0-3
- **Bit 4 = 1**: Use envelope generator (bits 0-3 ignored)

### Registers 11-12: Envelope Period

**Register 11**: Envelope period fine (lower 8 bits)
**Register 12**: Envelope period coarse (upper 8 bits)

**Envelope frequency**: `Envelope Period = Clock Frequency / (256 × Register Value)`

### Register 13: Envelope Shape

Controls the behavior of the envelope generator using bits 0-3:

| Bit | Name | Function |
|-----|------|----------|
| **0** | **Hold** | 1 = perform one cycle then hold at end value<br/>0 = cycle continuously |
| **1** | **Alternate** | 1 = alter direction after each cycle<br/>0 = reset after each cycle<br/>If Hold=1: chooses held value (0=final, 1=initial) |
| **2** | **Attack** | 1 = count up, 0 = count down |
| **3** | **Continue** | 0 = one cycle then drop to 0 (overrides Hold)<br/>1 = follow Hold setting |

## Usage Examples

### Play a Note on Channel A
```assembly
; Set Channel A to 440Hz (approximately)
LD BC, $FFFD        ; Select register port
LD A, 0             ; Register 0 (Channel A fine)
OUT (C), A
LD BC, $BFFD        ; Data port
LD A, $EE           ; Fine tune value
OUT (C), A

LD BC, $FFFD        ; Select register port  
LD A, 1             ; Register 1 (Channel A coarse)
OUT (C), A
LD BC, $BFFD        ; Data port
LD A, $01           ; Coarse tune value
OUT (C), A

; Enable tone on Channel A
LD BC, $FFFD
LD A, 7             ; Register 7 (enable)
OUT (C), A
LD BC, $BFFD
LD A, %11111110     ; Enable tone A, disable others
OUT (C), A

; Set volume
LD BC, $FFFD
LD A, 8             ; Register 8 (Channel A amplitude)
OUT (C), A
LD BC, $BFFD
LD A, 15            ; Maximum volume, fixed amplitude
OUT (C), A
```

### Configure Envelope
```assembly
; Set envelope period
LD BC, $FFFD
LD A, 11            ; Register 11 (envelope fine)
OUT (C), A
LD BC, $BFFD
LD A, $00           ; Fine period
OUT (C), A

LD BC, $FFFD
LD A, 12            ; Register 12 (envelope coarse)
OUT (C), A
LD BC, $BFFD
LD A, $10           ; Coarse period
OUT (C), A

; Set envelope shape - attack, continue, no hold
LD BC, $FFFD
LD A, 13            ; Register 13 (envelope shape)
OUT (C), A
LD BC, $BFFD
LD A, %00001100     ; Attack=1, Continue=1
OUT (C), A

; Use envelope on Channel A
LD BC, $FFFD
LD A, 8             ; Register 8 (Channel A amplitude)
OUT (C), A
LD BC, $BFFD
LD A, %00010000     ; Use envelope (bit 4=1)
OUT (C), A
```

### Enable Noise
```assembly
; Set noise period
LD BC, $FFFD
LD A, 6             ; Register 6 (noise period)
OUT (C), A
LD BC, $BFFD
LD A, $10           ; Noise period value
OUT (C), A

; Enable noise on Channel A, disable tone
LD BC, $FFFD
LD A, 7             ; Register 7 (enable flags)
OUT (C), A
LD BC, $BFFD
LD A, %11110001     ; Disable tone A, enable noise A
OUT (C), A
```

## Frequency Tables

### Common Musical Notes (Approximate Register Values)

| Note | Frequency (Hz) | 12-bit Value | Fine (R0/2/4) | Coarse (R1/3/5) |
|------|----------------|--------------|---------------|-----------------|
| C4 | 261.63 | $0D5D | $5D | $0D |
| D4 | 293.66 | $0BE8 | $E8 | $0B |
| E4 | 329.63 | $0A7C | $7C | $0A |
| F4 | 349.23 | $09D9 | $D9 | $09 |
| G4 | 392.00 | $0894 | $94 | $08 |
| A4 | 440.00 | $0789 | $89 | $07 |
| B4 | 493.88 | $06AD | $AD | $06 |

## Programming Tips

1. **Use both tone and noise** for rich sound effects
2. **Envelope generator** provides automatic volume control
3. **Multiple AY chips** available on Next for complex arrangements
4. **Register selection** must be done before data writes
5. **Frequency calculation** helps with musical note accuracy

## Related Ports

- [Turbo Sound Next Control](turbo_sound_next_control.md) ($FFFD) - Register selection
- [Sound Chip Register Write](sound_chip_register_write.md) ($BFFD) - Data writing
- [AY Info](ay_info.md) ($BFF5) - Chip information