# Mapped Spectrum Ports

## A Note on Partial Decoding

Most Spectrum peripherals did not actually decode all 16 bits of the address bus; they checked only for certain bits, and would respond if those bit values were set correctly, regardless of the other bits. The "bitmask" column for each port shows the bits that are tested for by the device. Traditionally all "unused" bits are set to 1 to avoid conflicts with other devices, which is the basis of the given port numbers; but alternate port numbers may be used in some cases. However, beware of creating clashes: in particular any port which does not intend to access the ULA should have the LSB set, as the ULA checks only for a reset LSB.

It is not known if the Next's built-in devices will have this decoding restriction, but it seems a safe presumption that they will not except where needed by legacy code.

On the other hand, partial decoding can allow use of the multiple output opcodes such as OTIR, which normally places the loop counter on the top half of the address bus - thus making it useless except for devices which ignore this top half. This is the reason why some of the Next registers do ignore the top half of the port address.

## Port Reference Table

| Port | Hex | Dec | Mask | Description |
|------|-----|-----|------|-------------|
| [Keyboard](keyboard.md) | $**FE | 254 | %xxxx xxxx ---- ---0 where only one bit in x is 0 | Series of specific ports that read keyboard key presses. |
| [I2C Clock](i2c_clock.md) | $103B | 4155 | %0001 0000 0011 1011 ?? | Sets and reads the I2C SCL line. |
| [I2C Data](i2c_data.md) | $113B | 4411 | %0001 0001 0011 1011 ?? | Sets and reads the I2C SDA line |
| [Layer 2 Access Port](layer_2_access_port.md) | $123B | 4667 | %0001 0010 0011 1011 ?? | Enables Layer 2 and controls paging of layer 2 screen into lower memory. |
| [UART TX](uart_tx.md) | $133B | 4923 | %0001 0011 0011 1011 | Sends byte to serial port. If read, tells if data in RX buffer |
| [UART RX](uart_rx.md) | $143B | 5179 | %0001 0100 0011 1011 | Reads data from serial port, write sets the baudrate |
| [UART Control](uart_control.md) | $153B | 5435 | %0001 0101 0011 1011 | Configuration of UART interfaces |
| [UART Frame](uart_frame.md) | $163B | 5691 | %0001 0110 0011 1011 | UART Frame |
| [CTC Channels](ctc_channels.md) | $183B | 6203 | %0001 1XXX 0011 1011 | CTC 8 channels 0x183b - 0x1f3b |
| [Plus 3 Memory Paging Control](plus_3_memory_paging_control.md) | $1FFD | 8189 | %0001 ---- ---- --0- | Controls ROM paging and special paging options from the +2a/+3. |
| [TBBlue Register Select](tbblue_register_select.md) | $243B | 9275 | %0010 0100 0011 1011 | Selects active port for TBBlue/Next feature configuration. |
| [TBBlue Register Access](tbblue_register_access.md) | $253B | 9531 | %0010 0101 0011 1011 | Reads and/or writes the selected TBBlue control register. |
| [Sprite Status/Slot Select](sprite_status_slot_select.md) | $303B | 12347 | %0011 0000 0011 1011 ?? | Sets active sprite-attribute index and pattern-slot index, reads sprite status. |
| [Memory Paging Control](memory_paging_control.md) | $7FFD | 32765 | %01-- ---- ---- --0- | Selects active RAM, ROM, and displayed screen. |
| [AY Info](ay_info.md) | $BFF5 | 49141 | 1011111111110101 | AY information |
| [Sound Chip Register Write](sound_chip_register_write.md) | $BFFD | 49149 | %10-- ---- ---- --0- | Writes to the selected register of the selected sound chip. |
| [Next Memory Bank Select](next_memory_bank_select.md) | $DFFD | 57341 | %1101 1111 1111 1101 | Provides additional bank select bits for extended memory. |
| [DIVMMC](divmmc.md) | $E3 | 227 |  | Divmmc control |
| [Pentagon 1024 Paging](pentagon_1024_paging.md) | $EFF7 | 61431 | 1110111111110111 | Paging in Pentagon 1024K mode |
| [Kempston Mouse Buttons](kempston_mouse_buttons.md) | $FADF | 64223 | %---- ---0 --0- ---- | Reads buttons on Kempston Mouse. |
| [Kempston Mouse X](kempston_mouse_x.md) | $FBDF | 64479 | %---- -0-1 --0- ---- | X coordinate of Kempston Mouse, 0-255. |
| [Kempston Mouse Y](kempston_mouse_y.md) | $FFDF | 65503 | %---- -1-1 --0- ---- | Y coordinate of Kempston Mouse, 0-255. |
| [Turbo Sound Next Control](turbo_sound_next_control.md) | $FFFD | 65533 | %11-- ---- ---- --0- | Controls stereo channels and selects active sound chip and sound chip channel. |
| [MB02 DMA Port](mb02_dma_port.md) | $xx0B | 11 | ---- ---- 0000 1011 | Controls Z8410 DMA chip via MB02 standard. |
| [Kempston Joystick](kempston_joystick.md) | $xx1F | 31 | %---- ---- 0001 1111 | Reads movement of joysticks using Kempston interface. |
| [Kempston Joystick 2, Joystick I/O](kempston_joystick_2_joystick_io.md) | $xx37 | 55 |  | Kempston interface second joystick variant and controls joystick I/O. |
| [Sprite Attribute Upload](sprite_attribute_upload.md) | $xx57 | 87 | %---- ---- 0101 0111 | Uploads sprite positions, visibility, colour type and effect flags. |
| [Sprite Pattern Upload](sprite_pattern_upload.md) | $xx5B | 91 | %---- ---- 0101 1011 ?? | Used to upload the pattern of the selected sprite. |
| [Datagear DMA Port](datagear_dma_port.md) | $xx6B | 107 | ---- ---- 0110 1011 | Controls zxnDMA chip |
| [SpecDrum DAC Output](specdrum_dac_output.md) | $xxDF | 223 | %---- ---- --01 1111 | Output to SpecDrum DAC. |
| [ULA Control Port](ula_control_port.md) | $xxFE | 254 |  | Controls border color and base Spectrum audio settings. |
| [Timex Sinclair Video Mode Control](timex_sinclair_video_mode_control.md) | $xxFF | 255 |  | Controls Timex Sinclair video modes and colours in hi-res mode. |

## Port Decoding Guidelines

### Key Points:
- **ULA Access**: Ports with LSB = 0 access the ULA
- **Non-ULA Access**: Should have LSB = 1 to avoid ULA conflicts
- **Partial Decoding**: Many devices only check specific address bits
- **OTIR Compatibility**: Some Next registers ignore high address bits
- **Bitmask**: Shows which address bits are actually decoded by each device

### Legacy Compatibility:
- Next maintains compatibility with original Spectrum port decoding
- Built-in Next devices may have full address decoding except where legacy compatibility is required