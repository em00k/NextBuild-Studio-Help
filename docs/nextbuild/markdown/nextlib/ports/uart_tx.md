# UART TX ($133B)

## Port Information

| Property | Value |
|----------|-------|
| **Port Number** | $133B |
| **Decimal** | 4923 |
| **Bit Mask** | %0001 0011 0011 1011 |
| **Readable** | Yes |
| **Writable** | Yes |
| **Subsystem** | UART |

## Description

Sends byte to serial port. If read, tells if data in RX buffer.

## Port Data Format

### Read Operation - Status Register

| Bit | Function | Description |
|-----|----------|-------------|
| **7** | Break condition | 1 if the Rx is in a break condition<br/>External device has held Tx=0 for at least 20 bit periods |
| **6** | Framing error | 1 if the Rx experienced a framing error<br/>Clears on read, includes parity and stop bit errors |
| **5** | Error recovery | 1 if the next Rx byte was received after an error condition was detected (framing, overflow) |
| **4** | Tx buffer empty | 1 if the Tx buffer is empty |
| **3** | Rx buffer near full | 1 if the Rx buffer is near full (3/4 capacity) |
| **2** | Rx buffer overflow | 1 if the Rx buffer overflowed<br/>Clears on read |
| **1** | Tx buffer full | 1 if the Tx buffer is full |
| **0** | Rx data available | 1 if the Rx buffer contains bytes |

### Write Operation

Writing to this port sends a byte to the connected device via the UART transmitter.

## UART Status Monitoring

### Transmission Status
- **Bit 4**: Tx buffer empty - safe to send more data
- **Bit 1**: Tx buffer full - must wait before sending

### Reception Status  
- **Bit 0**: Data available in Rx buffer
- **Bit 3**: Rx buffer nearly full (3/4 capacity)
- **Bit 2**: Rx buffer overflow occurred

### Error Conditions
- **Bit 7**: Break condition detected
- **Bit 6**: Framing/parity/stop bit error
- **Bit 5**: Data received after error condition

## Usage Examples

### Send a Byte
```assembly
; Wait for Tx buffer to be ready
wait_tx_ready:
    IN A, ($133B)       ; Read UART status
    BIT 1, A            ; Test Tx buffer full flag
    JR NZ, wait_tx_ready ; Wait if buffer full

    ; Send the byte
    LD A, 'H'           ; Character to send
    OUT ($133B), A      ; Transmit byte
```

### Check for Received Data
```assembly
; Check if data is available
    IN A, ($133B)       ; Read UART status
    BIT 0, A            ; Test Rx data available
    JR Z, no_data       ; Jump if no data

    ; Data is available, read it
    IN A, ($143B)       ; Read from UART RX port
    ; Process received byte in A
    CALL process_data
no_data:
```

### Monitor Buffer Status
```assembly
uart_status_check:
    IN A, ($133B)       ; Read status register
    
    ; Check for errors first
    BIT 6, A            ; Framing error?
    JR NZ, handle_framing_error
    BIT 2, A            ; Overflow error?
    JR NZ, handle_overflow_error
    BIT 7, A            ; Break condition?
    JR NZ, handle_break_condition
    
    ; Check buffer levels
    BIT 3, A            ; Rx buffer near full?
    JR NZ, drain_rx_buffer
    BIT 0, A            ; Data available?
    JR NZ, read_available_data
    
    RET

handle_framing_error:
    ; Reading the status clears the error flag
    ; Take appropriate action for framing error
    CALL log_framing_error
    RET

handle_overflow_error:
    ; Reading the status clears the overflow flag
    ; Data has been lost, reset communication
    CALL reset_uart_comm
    RET
```

### Robust Data Transmission
```assembly
send_string:
    ; HL points to null-terminated string
send_loop:
    LD A, (HL)          ; Get next character
    OR A                ; Check for null terminator
    RET Z               ; Return if end of string
    
    ; Wait for transmitter ready
wait_tx:
    PUSH AF             ; Save character
    IN A, ($133B)       ; Read status
    BIT 1, A            ; Tx buffer full?
    JR NZ, wait_tx      ; Wait if full
    
    ; Check for transmission errors
    BIT 6, A            ; Framing error?
    JR NZ, tx_error     ; Handle error
    
    POP AF              ; Restore character
    OUT ($133B), A      ; Send character
    INC HL              ; Next character
    JR send_loop        ; Continue

tx_error:
    POP AF              ; Clean stack
    ; Handle transmission error
    RET
```

### High-Speed Data Transfer
```assembly
fast_transmit:
    ; BC = byte count, HL = data buffer
fast_tx_loop:
    ; Quick status check
    IN A, ($133B)
    BIT 1, A            ; Tx buffer full?
    JR NZ, fast_tx_loop ; Busy wait
    
    ; Send byte immediately
    LD A, (HL)
    OUT ($133B), A
    INC HL
    DEC BC
    LD A, B
    OR C
    JR NZ, fast_tx_loop
    RET
```

### Error Recovery Routine
```assembly
uart_error_recovery:
    IN A, ($133B)       ; Read status (clears some errors)
    
    ; Log error conditions
    BIT 7, A
    CALL NZ, log_break_condition
    BIT 6, A  
    CALL NZ, log_framing_error
    BIT 2, A
    CALL NZ, log_overflow_error
    
    ; Flush buffers if needed
    BIT 3, A            ; Rx near full?
    JR Z, recovery_done
    
flush_rx:
    IN A, ($143B)       ; Read and discard Rx data
    IN A, ($133B)       ; Check status again
    BIT 0, A            ; More data?
    JR NZ, flush_rx     ; Continue flushing
    
recovery_done:
    RET
```

## UART Configuration

### Related Ports
- [UART RX](uart_rx.md) ($143B) - Receive data and baud rate setting
- [UART Control](uart_control.md) ($153B) - UART configuration
- [UART Frame](uart_frame.md) ($163B) - Frame format settings

### Baud Rate Configuration
Baud rate is set via [UART RX](uart_rx.md) port ($143B) write operation.

### Buffer Management
- **Tx Buffer**: Internal transmit buffer (size varies)
- **Rx Buffer**: Internal receive buffer with overflow protection
- **Flow Control**: Monitor buffer status for optimal performance

## Programming Guidelines

### Best Practices
1. **Always check Tx buffer status** before sending
2. **Monitor error flags** and implement recovery
3. **Handle buffer overflow** gracefully
4. **Use interrupts** for high-speed communication (if available)
5. **Implement timeouts** for robust communication

### Performance Tips
- **Batch operations** when possible
- **Pre-check buffer status** before loops
- **Use error recovery** to maintain communication
- **Consider hardware flow control** for reliable transfers

### Error Handling
- **Read status register** to clear error flags
- **Implement retry logic** for failed transmissions
- **Log errors** for debugging purposes
- **Flush buffers** after error conditions

## Hardware Notes

### Electrical Interface
- **RS-232 compatible** voltage levels
- **ESP8266 WiFi module** connection supported
- **Serial debugging** capability

### Physical Connection
- **J9 connector** on Next board
- **Shared with ESP8266** WiFi module
- **External serial devices** via appropriate adapters

## Related Components

- [ESP8266-01](esp8266_01.md) - WiFi module using UART
- [Pi UART](pi_uart.md) - Raspberry Pi communication
- Serial debugging and development tools