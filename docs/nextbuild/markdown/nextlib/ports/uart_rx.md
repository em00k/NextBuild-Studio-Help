# UART RX ($143B)

## Port Information

| Property | Value |
|----------|-------|
| **Port Number** | $143B |
| **Decimal** | 5179 |
| **Bit Mask** | %0001 0100 0011 1011 |
| **Readable** | Yes |
| **Writable** | Yes |
| **Subsystem** | UART |

## Description

Reads data from serial port, write sets the baudrate.

## Port Operations

### Read Operation - Receive Data

Read a byte from the receive buffer. **If the buffer is empty, 0 is returned.**

**Important**: Always check [UART TX](uart_tx.md) ($133B) status bit 0 to verify data is available before reading to distinguish between actual zero bytes and empty buffer.

### Write Operation - Baud Rate Configuration

Writes the lower 14-bits of the UART's prescalar value that determines baud rate.

#### Prescalar Format

| Bit 7 | Function | Bits 6:0 |
|-------|----------|----------|
| **1** | Upper part | Upper 7-bits of the 14-bit prescalar value |
| **0** | Lower part | Lower 7-bits of the 14-bit prescalar value |

## Baud Rate Calculation

The UART's baud rate is determined by the prescalar according to this formula:

```
prescalar = Fsys / baudrate
```

Where:
- **Fsys** = system clock from [Video Timing Register](video_timing_register.md) ($11)
- **baudrate** = desired communication speed

### Example Calculation

If the system is HDMI, nextreg 0x11 indicates that Fsys = 27,000,000 Hz.
The prescalar for a baud rate of 115,200 is:

```
prescalar = 27,000,000 / 115,200 = 234 (decimal) = $EA (hex)
```

## Common Baud Rates

### Standard Baud Rates (Fsys = 27 MHz)

| Baud Rate | Prescalar (Dec) | Prescalar (Hex) | Upper 7-bits | Lower 7-bits |
|-----------|-----------------|-----------------|--------------|--------------|
| 9,600 | 2,812 | $AFC | $15 | $7C |
| 19,200 | 1,406 | $57E | $0A | $7E |
| 38,400 | 703 | $2BF | $05 | $3F |
| 57,600 | 468 | $1D4 | $03 | $54 |
| 115,200 | 234 | $0EA | $01 | $6A |
| 230,400 | 117 | $075 | $00 | $75 |

### Standard Baud Rates (Fsys = 28 MHz)

| Baud Rate | Prescalar (Dec) | Prescalar (Hex) | Upper 7-bits | Lower 7-bits |
|-----------|-----------------|-----------------|--------------|--------------|
| 9,600 | 2,916 | $B64 | $16 | $64 |
| 19,200 | 1,458 | $5B2 | $0B | $32 |
| 38,400 | 729 | $2D9 | $05 | $59 |
| 57,600 | 486 | $1E6 | $03 | $66 |
| 115,200 | 243 | $0F3 | $01 | $73 |
| 230,400 | 121 | $079 | $00 | $79 |

## Usage Examples

### Set Baud Rate to 115,200
```assembly
; For Fsys = 27 MHz, prescalar = 234 ($EA)
; Upper 7 bits = $01, Lower 7 bits = $6A

; Set lower 7 bits (bit 7 = 0)
LD A, %01101010      ; $6A with bit 7 = 0
OUT ($143B), A

; Set upper 7 bits (bit 7 = 1)  
LD A, %10000001      ; $01 with bit 7 = 1
OUT ($143B), A
```

### Set Baud Rate to 9,600
```assembly
; For Fsys = 27 MHz, prescalar = 2812 ($AFC)
; Upper 7 bits = $15, Lower 7 bits = $7C

; Set lower 7 bits
LD A, %01111100      ; $7C with bit 7 = 0
OUT ($143B), A

; Set upper 7 bits
LD A, %10010101      ; $15 with bit 7 = 1
OUT ($143B), A
```

### Read Received Data Safely
```assembly
receive_byte:
    ; Check if data is available
    IN A, ($133B)       ; Read UART TX status
    BIT 0, A            ; Test Rx data available bit
    RET Z               ; Return if no data (Z flag set)
    
    ; Data is available, read it
    IN A, ($143B)       ; Read received byte
    ; A now contains the received byte
    ; Z flag is clear indicating data was read
    RET

; Alternative with error checking
receive_byte_safe:
    ; Check status and errors
    IN A, ($133B)       ; Read status
    BIT 6, A            ; Framing error?
    JR NZ, rx_error     ; Handle error
    BIT 2, A            ; Buffer overflow?
    JR NZ, rx_error     ; Handle error
    BIT 0, A            ; Data available?
    RET Z               ; Return if no data
    
    ; Read the byte
    IN A, ($143B)
    RET                 ; Success

rx_error:
    ; Handle receive error
    SCF                 ; Set carry flag to indicate error
    RET
```

### Receive String with Timeout
```assembly
; Receive string into buffer at HL, max length in B
; Returns with carry set on timeout/error
receive_string:
    LD C, 0             ; Character count
    LD D, 255           ; Timeout counter

receive_loop:
    ; Check for timeout
    DEC D
    JR Z, receive_timeout

    ; Check for data
    IN A, ($133B)       ; Read status
    BIT 0, A            ; Data available?
    JR Z, receive_wait  ; Wait if no data
    
    ; Read character
    IN A, ($143B)
    
    ; Check for end of string (CR or LF)
    CP 13               ; Carriage return?
    JR Z, receive_done
    CP 10               ; Line feed?
    JR Z, receive_done
    
    ; Store character
    LD (HL), A
    INC HL
    INC C
    
    ; Check buffer full
    LD A, C
    CP B                ; Compare with max length
    JR Z, receive_done  ; Buffer full
    
    JR receive_loop

receive_wait:
    ; Small delay before retry
    PUSH BC
    LD BC, 1000         ; Delay loop
delay_loop:
    DEC BC
    LD A, B
    OR C
    JR NZ, delay_loop
    POP BC
    JR receive_loop

receive_timeout:
    SCF                 ; Set carry for timeout
    RET

receive_done:
    XOR A
    LD (HL), A          ; Null terminate string
    OR A                ; Clear carry for success
    RET
```

### Configure UART for ESP8266
```assembly
; Set up UART for ESP8266 communication at 115,200 baud
setup_esp_uart:
    ; Calculate prescalar for current video timing
    ; For most cases, this will be 27 MHz
    
    ; Set 115,200 baud (prescalar = 234 for 27 MHz)
    LD A, %01101010      ; Lower 7 bits: $6A
    OUT ($143B), A
    LD A, %10000001      ; Upper 7 bits: $01  
    OUT ($143B), A
    
    ; Optionally configure frame format
    ; (see UART Control and UART Frame ports)
    
    RET
```

### Dynamic Baud Rate Setting
```assembly
; Set baud rate from 16-bit prescalar value in BC
set_baud_rate:
    ; Set lower 7 bits
    LD A, C
    AND %01111111       ; Mask bit 7
    OUT ($143B), A
    
    ; Set upper 7 bits  
    LD A, B
    AND %01111111       ; Mask bit 7
    OR %10000000        ; Set bit 7
    OUT ($143B), A
    
    RET

; Calculate prescalar for given baud rate
; Input: DE = desired baud rate
; Output: BC = prescalar value
calculate_prescalar:
    ; This is a simplified version - real implementation
    ; would need 32-bit division
    ; Assumes Fsys = 27,000,000
    
    ; For demonstration, handle common rates
    LD BC, 27000000 / 115200    ; Default to 115,200
    
    ; Compare with common rates and set accordingly
    LD HL, 115200
    OR A
    SBC HL, DE
    JR Z, calc_done
    
    ; Add more rate calculations as needed
    
calc_done:
    RET
```

## Important Notes

### Data Availability
- **Always check** [UART TX](uart_tx.md) status bit 0 before reading
- **Empty buffer** returns 0, same as a received null byte
- **Use status checking** to distinguish between cases

### Baud Rate Setting
- **14-bit prescalar** provides fine-grained control
- **Two writes required** (lower then upper, or vice versa)
- **System clock dependent** - check [Video Timing Register](video_timing_register.md) ($11)

### System Clock Variations
- **HDMI mode**: Typically 27 MHz
- **VGA mode**: May use different clock
- **Check nextreg $11** for actual system frequency

## Related Ports

- [UART TX](uart_tx.md) ($133B) - Transmit data and status
- [UART Control](uart_control.md) ($153B) - UART configuration  
- [UART Frame](uart_frame.md) ($163B) - Frame format settings
- [Video Timing Register](video_timing_register.md) ($11) - System clock reference

## Programming Tips

1. **Always verify data availability** before reading
2. **Set baud rate before** beginning communication
3. **Handle receive errors** gracefully
4. **Use appropriate timeouts** for reliable communication
5. **Consider system clock changes** when setting baud rates
6. **Test with known good devices** during development