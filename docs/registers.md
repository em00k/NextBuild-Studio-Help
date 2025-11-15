# Registers

## Hardware Registers

| Register | Name                 Description                                     |
|---------|:----------------------------------------------------------------------|
| $00 | [MACHINE_ID_NR_00](MACHINE_ID_NR_00.md) - Identifies TBBlue board type. Should always be 10 (binary 0000 1010) on Next.|
| $01 | [NEXT_VERSION_NR_01](NEXT_VERSION_NR_01.md) - Identifies core (FPGA image) version.|
| $02 | [NEXT_RESET_NR_02](NEXT_RESET_NR_02.md) - Identifies type of last reset. Can be written to force reset.|
| $03 | [MACHINE_TYPE_NR_03](MACHINE_TYPE_NR_03.md) - Identifies timing and machine type.|
| $04 | [ROM_MAPPING_NR_04](ROM_MAPPING_NR_04.md) - In config mode, allows RAM to be mapped to ROM area.|
| $05 | [PERIPHERAL_1_NR_05](PERIPHERAL_1_NR_05.md) - Sets joystick mode, video frequency and Scandoubler.|
| $06 | [PERIPHERAL_2_NR_06](PERIPHERAL_2_NR_06.md) - Enables CPU Speed key, DivMMC, Multiface, Mouse and AY audio.|
| $07 | [TURBO_CONTROL_NR_07](TURBO_CONTROL_NR_07.md) - Sets CPU Speed, reads actual speed.|
| $08 | [PERIPHERAL_3_NR_08](PERIPHERAL_3_NR_08.md) - ABC/ACB Stereo, Internal Speaker, SpecDrum, Timex Video Modes, Turbo Sound Next, RAM contention and [un]lock 128k paging.|
| $09 | [PERIPHERAL_4_NR_09](PERIPHERAL_4_NR_09.md) - Sets scanlines, AY mono output, Sprite-id lockstep, reset DivMMC mapram and disable HDMI audio.|
| $0A | [PERIPHERAL_5_NR_0A](PERIPHERAL_5_NR_0A.md) - Multiface type, Divmmc automap, Mouse buttons and DPI config.|
| $0B | [JOYSTICK_I_O_MODE_NR_0B](JOYSTICK_I_O_MODE_NR_0B.md) - Joystick port I/O control.|
| $0E | [NEXT_VERSION_MINOR_NR_0E](NEXT_VERSION_MINOR_NR_0E.md) - Identifies core (FPGA image) version (sub minor number).|
| $0F | [BOARD_ID_NR_0F](BOARD_ID_NR_0F.md) - Spectrum next issue ID.|
| $10 | [ANTI_BRICK_NR_10](ANTI_BRICK_NR_10.md) - Used within the Anti-brick system.|
| $11 | [VIDEO_TIMING_NR_11](VIDEO_TIMING_NR_11.md) - Sets video output timing variant.|
| $12 | [LAYER2_RAM_BANK_NR_12](LAYER2_RAM_BANK_NR_12.md) - Sets the bank number where Layer 2 video memory begins.|
| $13 | [LAYER2_RAM_SHADOW_BANK_NR_13](LAYER2_RAM_SHADOW_BANK_NR_13.md) - Sets the bank number where the Layer 2 shadow screen begins.|
| $14 | [GLOBAL_TRANSPARENCY_NR_14](GLOBAL_TRANSPARENCY_NR_14.md) - Sets the "transparent" colour for Layer 2, ULA and LoRes pixel data.|
| $15 | [SPRITE_CONTROL_NR_15](SPRITE_CONTROL_NR_15.md) - Enables/disables Sprites and Lores Layer, and chooses priority of sprites and Layer 2.|
| $16 | [LAYER2_XOFFSET_NR_16](LAYER2_XOFFSET_NR_16.md) - Sets the pixel offset used for drawing Layer 2 graphics on the screen.|
| $17 | [LAYER2_YOFFSET_NR_17](LAYER2_YOFFSET_NR_17.md) - Sets the Y offset used when drawing Layer 2 graphics on the screen.|
| $18 | [CLIP_LAYER2_NR_18](CLIP_LAYER2_NR_18.md) - Sets and reads clip-window for Layer 2.|
| $19 | [CLIP_SPRITE_NR_19](CLIP_SPRITE_NR_19.md) - Sets and reads clip-window for Sprites.|
| $1A | [CLIP_ULA_LORES_NR_1A](CLIP_ULA_LORES_NR_1A.md) - Sets and reads clip-window for ULA/LoRes layer.|
| $1B | [CLIP_TILEMAP_NR_1B](CLIP_TILEMAP_NR_1B.md) - Sets and reads clip-window for Tilemap.|
| $1C | [CLIP_WINDOW_CONTROL_NR_1C](CLIP_WINDOW_CONTROL_NR_1C.md) - Controls (resets) the clip-window registers indices.|
| $1E | [VIDEO_LINE_MSB_NR_1E](VIDEO_LINE_MSB_NR_1E.md) - Holds the MSB (only, as bit 0) of the raster line currently being drawn.|
| $1F | [VIDEO_LINE_LSB_NR_1F](VIDEO_LINE_LSB_NR_1F.md) - Holds the eight LSBs of the raster line currently being drawn.|
| $20 | [GENERATE_MASKABLE_INTERRUPT_NR_20](GENERATE_MASKABLE_INTERRUPT_NR_20.md) - Trigger interrupt.|
| $22 | [VIDEO_INTERUPT_CONTROL_NR_22](VIDEO_INTERUPT_CONTROL_NR_22.md) - Controls the timing of raster interrupts and the ULA frame interrupt.|
| $23 | [VIDEO_INTERUPT_VALUE_NR_23](VIDEO_INTERUPT_VALUE_NR_23.md) - Holds the eight LSBs of the line on which a raster interrupt should occur.|
| $24 | [RESERVED_NR_24](RESERVED_NR_24.md) - n/a.|
| $26 | [ULA_XOFFSET_NR_26](ULA_XOFFSET_NR_26.md) - Pixel X offset (0..255) to use when drawing ULA Layer.|
| $27 | [ULA_YOFFSET_NR_27](ULA_YOFFSET_NR_27.md) - Pixel Y offset (0..191) to use when drawing ULA Layer.|
| $28 | [HIGH_ADRESS_KEYMAP_NR_28](HIGH_ADRESS_KEYMAP_NR_28.md) - PS/2 Keymap address MSB, read (pending) first byte of palette colour.|
| $29 | [LOW_ADRESS_KEYMAP_NR_29](LOW_ADRESS_KEYMAP_NR_29.md) - PS/2 Keymap address LSB.|
| $2A | [HIGH_DATA_TO_KEYMAP_NR_2A](HIGH_DATA_TO_KEYMAP_NR_2A.md) - High data to PS/2 Keymap (MSB of data in bit 0).|
| $2B | [LOW_DATA_TO_KEYMAP_NR_2B](LOW_DATA_TO_KEYMAP_NR_2B.md) - Low eight LSBs of PS/2 Keymap data.|
| $2C | [DAC_B_MIRROR_NR_2C](DAC_B_MIRROR_NR_2C.md) - DAC B mirror, read current I2S left MSB.|
| $2D | [DAC_AD_MIRROR_NR_2D](DAC_AD_MIRROR_NR_2D.md) - SpecDrum port 0xDF / DAC A+D mirror, read current I2S LSB.|
| $2E | [DAC_C_MIRROR_NR_2E](DAC_C_MIRROR_NR_2E.md) - DAC C mirror, read current I2S right MSB.|
| $2F | [TILEMAP_XOFFSET_MSB_NR_2F](TILEMAP_XOFFSET_MSB_NR_2F.md) - Sets the pixel offset (two high bits) used for drawing Tilemap graphics on the screen.|
| $30 | [TILEMAP_XOFFSET_LSB_NR_30](TILEMAP_XOFFSET_LSB_NR_30.md) - Sets the pixel offset (eight low bits) used for drawing Tilemap graphics on the screen.|
| $31 | [TILEMAP_YOFFSET_NR_31](TILEMAP_YOFFSET_NR_31.md) - Sets the pixel offset used for drawing Tilemap graphics on the screen.|
| $32 | [LORES_XOFFSET_NR_32](LORES_XOFFSET_NR_32.md) - Pixel X offset (0..255) to use when drawing LoRes Layer.|
| $33 | [LORES_YOFFSET_NR_33](LORES_YOFFSET_NR_33.md) - Pixel Y offset (0..191) to use when drawing LoRes Layer.|
| $34 | [SPRITE_ATTR_SLOT_SEL_NR_34](SPRITE_ATTR_SLOT_SEL_NR_34.md) - Selects sprite index 0..127 to be affected by writes to other Sprite ports (and mirrors).|
| $35 | [SPRITE_ATTR0_NR_35](SPRITE_ATTR0_NR_35.md) - Nextreg port-mirror to write directly into "byte 1" of Sprite Attribute Upload ($xx57 / 87).|
| $36 | [SPRITE_ATTR1_NR_36](SPRITE_ATTR1_NR_36.md) - Nextreg port-mirror to write directly into "byte 2" of Sprite Attribute Upload ($xx57 / 87).|
| $37 | [SPRITE_ATTR2_NR_37](SPRITE_ATTR2_NR_37.md) - Nextreg port-mirror to write directly into "byte 3" of Sprite Attribute Upload ($xx57 / 87).|
| $38 | [SPRITE_ATTR3_NR_38](SPRITE_ATTR3_NR_38.md) - Nextreg port-mirror to write directly into "byte 4" of Sprite Attribute Upload ($xx57 / 87).|
| $39 | [SPRITE_ATTR4_NR_39](SPRITE_ATTR4_NR_39.md) - Nextreg port-mirror to write directly into "byte 5" of Sprite Attribute Upload ($xx57 / 87).|
| $40 | [PALETTE_INDEX_NR_40](PALETTE_INDEX_NR_40.md) - Chooses an palette element (index) to manipulate with.|
| $41 | [PALETTE_VALUE_NR_41](PALETTE_VALUE_NR_41.md) - Use to set/read 8-bit colours of the ULANext palette.|
| $42 | [PALETTE_FORMAT_NR_42](PALETTE_FORMAT_NR_42.md) - Specifies mask to extract ink colour from attribute cell value in ULANext mode.|
| $43 | [PALETTE_CONTROL_NR_43](PALETTE_CONTROL_NR_43.md) - Enables or disables Enhanced ULA interpretation of attribute values and toggles active palette.|
| $44 | [PALETTE_VALUE_9BIT_NR_44](PALETTE_VALUE_9BIT_NR_44.md) - Use to set 9-bit (2-byte) colours of the Enhanced ULA palette, or to read second byte of colour.|
| $4A | [TRANSPARENCY_FALLBACK_COL_NR_4A](TRANSPARENCY_FALLBACK_COL_NR_4A.md) - 8-bit colour to be used when all layers contain transparent pixel.|
| $4B | [SPRITE_TRANSPARENCY_I_NR_4B](SPRITE_TRANSPARENCY_I_NR_4B.md) - Index into sprite palette (of "transparent" colour).|
| $4C | [TILEMAP_TRANSPARENCY_I_NR_4C](TILEMAP_TRANSPARENCY_I_NR_4C.md) - Index into Tilemap palette (of "transparent" colour).|
| $50 | [MMU0_0000_NR_50](MMU0_0000_NR_50.md) - Selects the 8k-bank stored in 8k-slot 0 (see Memory map).|
| $51 | [MMU1_2000_NR_51](MMU1_2000_NR_51.md) - Selects the 8k-bank stored in 8k-slot 1 (see Memory map).|
| $52 | [MMU2_4000_NR_52](MMU2_4000_NR_52.md) - Selects the 8k-bank stored in 8k-slot 2 (see Memory map).|
| $53 | [MMU3_6000_NR_53](MMU3_6000_NR_53.md) - Selects the 8k-bank stored in 8k-slot 3 (see Memory map).|
| $54 | [MMU4_8000_NR_54](MMU4_8000_NR_54.md) - Selects the 8k-bank stored in 8k-slot 4 (see Memory map).|
| $55 | [MMU5_A000_NR_55](MMU5_A000_NR_55.md) - Selects the 8k-bank stored in 8k-slot 5 (see Memory map).|
| $56 | [MMU6_C000_NR_56](MMU6_C000_NR_56.md) - Selects the 8k-bank stored in 8k-slot 6 (see Memory map).|
| $57 | [MMU7_E000_NR_57](MMU7_E000_NR_57.md) - Selects the 8k-bank stored in 8k-slot 7 (see Memory map).|
| $60 | [COPPER_DATA_NR_60](COPPER_DATA_NR_60.md) - Used to upload code to the Copper.|
| $61 | [COPPER_CONTROL_LO_NR_61](COPPER_CONTROL_LO_NR_61.md) - Holds low byte of Copper control bits.|
| $62 | [COPPER_CONTROL_HI_NR_62](COPPER_CONTROL_HI_NR_62.md) - Holds high byte of Copper control flags.|
| $63 | [COPPER_DATA_16B_NR_63](COPPER_DATA_16B_NR_63.md) - Used to upload code to the Copper.|
| $64 | [VIDEO_LINE_OFFSET_NR_64](VIDEO_LINE_OFFSET_NR_64.md) - Offset numbering of raster lines in copper/interrupt/active register.|
| $68 | [ULA_CONTROL_NR_68](ULA_CONTROL_NR_68.md) - Disable ULA, controls ULA mixing/blending, enable ULA+.|
| $69 | [DISPLAY_CONTROL_NR_69](DISPLAY_CONTROL_NR_69.md) - Layer2, ULA shadow, Timex $FF port.|
| $6A | [LORES_CONTROL_NR_6A](LORES_CONTROL_NR_6A.md) - LoRes Radastan mode.|
| $6B | [TILEMAP_CONTROL_NR_6B](TILEMAP_CONTROL_NR_6B.md) - Controls Tilemap mode.|
| $6C | [TILEMAP_DEFAULT_ATTR_NR_6C](TILEMAP_DEFAULT_ATTR_NR_6C.md) - Default tile attribute for 8-bit only maps.|
| $6E | [TILEMAP_BASE_ADR_NR_6E](TILEMAP_BASE_ADR_NR_6E.md) - Base address of the 40x32 or 80x32 tile map (similar to text-mode of other computers).|
| $6F | [TILEMAP_GFX_ADR_NR_6F](TILEMAP_GFX_ADR_NR_6F.md) - Base address of the tiles' graphics.|
| $70 | [LAYER2_CONTROL_NR_70](LAYER2_CONTROL_NR_70.md) - Layer 2 resolution, palette offset.|
| $71 | [LAYER2_XOFFSET_MSB_NR_71](LAYER2_XOFFSET_MSB_NR_71.md) - Sets the pixel offset used for drawing Layer 2 graphics on the screen.|
| $75 | [SPRITE_ATTR0_INC_NR_75](SPRITE_ATTR0_INC_NR_75.md) - Same as Sprite port-mirror Attribute 0 Register ($35) (write first byte of sprite-attributes), plus increments Sprite port-mirror Index Register ($34).|
| $76 | [SPRITE_ATTR1_INC_NR_76](SPRITE_ATTR1_INC_NR_76.md) - Same as Sprite port-mirror Attribute 1 Register ($36) (write second byte of sprite-attributes), plus increments Sprite port-mirror Index Register ($34).|
| $77 | [SPRITE_ATTR2_INC_NR_77](SPRITE_ATTR2_INC_NR_77.md) - Same as Sprite port-mirror Attribute 2 Register ($37) (write third byte of sprite-attributes), plus increments Sprite port-mirror Index Register ($34).|
| $78 | [SPRITE_ATTR3_INC_NR_78](SPRITE_ATTR3_INC_NR_78.md) - Same as Sprite port-mirror Attribute 3 Register ($38) (write fourth byte of sprite-attributes), plus increments Sprite port-mirror Index Register ($34).|
| $79 | [SPRITE_ATTR4_INC_NR_79](SPRITE_ATTR4_INC_NR_79.md) - Same as Sprite port-mirror Attribute 4 Register ($39) (write fifth byte of sprite-attributes), plus increments Sprite port-mirror Index Register ($34).|
| $7F | [USER_STORAGE_0_NR_7F](USER_STORAGE_0_NR_7F.md) - 8-bit storage for user.|
| $80 | [EXPANSION_BUS_ENABLE_REGISTER_NR_80](EXPANSION_BUS_ENABLE_REGISTER_NR_80.md) - Expansion bus enable/config.|
| $81 | [EXPANSION_BUS_CONTROL_NR_81](EXPANSION_BUS_CONTROL_NR_81.md) - Expansion bus controls.|
| $82 | [INTERNAL_PORT_DECODING_0_NR_82](INTERNAL_PORT_DECODING_0_NR_82.md) - Enabling internal ports decoding.|
| $83 | [INTERNAL_PORT_DECODING_1_NR_83](INTERNAL_PORT_DECODING_1_NR_83.md) - Enabling internal ports decoding.|
| $84 | [INTERNAL_PORT_DECODING_2_NR_84](INTERNAL_PORT_DECODING_2_NR_84.md) - Enabling internal ports decoding.|
| $85 | [INTERNAL_PORT_DECODING_3_NR_85](INTERNAL_PORT_DECODING_3_NR_85.md) - Enabling internal ports decoding.|
| $86 | [EXPANSION_BUS_DECODING_0_NR_86](EXPANSION_BUS_DECODING_0_NR_86.md) - When expansion bus is enabled: Internal ports decoding mask.|
| $87 | [EXPANSION_BUS_DECODING_1_NR_87](EXPANSION_BUS_DECODING_1_NR_87.md) - When expansion bus is enabled: Internal ports decoding mask.|
| $88 | [EXPANSION_BUS_DECODING_2_NR_88](EXPANSION_BUS_DECODING_2_NR_88.md) - When expansion bus is enabled: Internal ports decoding mask.|
| $89 | [EXPANSION_BUS_DECODING_3_NR_89](EXPANSION_BUS_DECODING_3_NR_89.md) - When expansion bus is enabled: Internal ports decoding mask.|
| $8A | [EXPANSION_BUS_PROPAGATE_NR_8A](EXPANSION_BUS_PROPAGATE_NR_8A.md) - Monitoring internal I/O or adding external keyboard.|
| $8C | [ALTERNATE_ROM_NR_8C](ALTERNATE_ROM_NR_8C.md) - Enable alternate ROM or lock 48k ROM.|
| $8E | [ZX_MEM_MAPPING_NR_8E](ZX_MEM_MAPPING_NR_8E.md) - Control classic 128K Spectrum memory mapping.|
| $8F | [MEMORY_MAPPING_MODE_REGISTER_NR_8F](MEMORY_MAPPING_MODE_REGISTER_NR_8F.md) - Select memory mapping mode.|
| $90 | [PI_GPIO_OUT_ENABLE_0_NR_90](PI_GPIO_OUT_ENABLE_0_NR_90.md) - Enables GPIO pins output.|
| $98 | [PI_GPIO_0_NR_98](PI_GPIO_0_NR_98.md) - GPIO pins mapped to Next Register.|
| $A0 | [PI_PERIPHERALS_ENABLE_NR_A0](PI_PERIPHERALS_ENABLE_NR_A0.md) - Enable Pi peripherals: UART, Pi hats, I2C, SPI.|
| $A2 | [PI_I2S_AUDIO_CONTROL_NR_A2](PI_I2S_AUDIO_CONTROL_NR_A2.md) - Pi I2S controls.|
| $A3 | [PI_I2S_CLOCK_DIVIDE_REGISTER_NR_A3](PI_I2S_CLOCK_DIVIDE_REGISTER_NR_A3.md) - Pi I2S clock divide in master mode.|
| $A8 | [ESP_WIFI_GPIO_OUTPUT_NR_A8](ESP_WIFI_GPIO_OUTPUT_NR_A8.md) - ESP WiFi GPIO Output.|
| $A9 | [ESP_WIFI_GPIO_NR_A9](ESP_WIFI_GPIO_NR_A9.md) - ESP WiFi GPIO Read/Write.|
| $B0 | [EXTENDED_KEYS_0_NR_B0](EXTENDED_KEYS_0_NR_B0.md) - Read Next keyboard compound keys separately.|
| $B1 | [EXTENDED_KEYS_1_NR_B1](EXTENDED_KEYS_1_NR_B1.md) - Read Next keyboard compound keys separately.|
| $B2 | [DIVMMC_TRAP_ENABLE_1_REGISTER_NR_B2](DIVMMC_TRAP_ENABLE_1_REGISTER_NR_B2.md) - DivMMC trap configuration.|
| $B2 | [EXTENDED_MD_PAD_BUTTONS_NR_B2](EXTENDED_MD_PAD_BUTTONS_NR_B2.md) - Reading additional buttons on MD pads.|
| $B4 | [DIVMMC_TRAP_ENABLE_2_REGISTER_NR_B4](DIVMMC_TRAP_ENABLE_2_REGISTER_NR_B4.md) - DivMMC trap configuration.|
| $B8 | [DIVMMC_ENTRY_POINTS_0_NR_B8](DIVMMC_ENTRY_POINTS_0_NR_B8.md) - DivMMC automap control.|
| $B9 | [DIVMMC_ENTRY_POINTS_VALID_0_NR_B9](DIVMMC_ENTRY_POINTS_VALID_0_NR_B9.md) - DivMMC entry point validity.|
| $BA | [DIVMMC_ENTRY_POINTS_TIMING_0_NR_BA](DIVMMC_ENTRY_POINTS_TIMING_0_NR_BA.md) - Adjust delay of divmmc mapping.|
| $BB | [DIVMMC_ENTRY_POINTS_1_NR_BB](DIVMMC_ENTRY_POINTS_1_NR_BB.md) - DivMMC automap control.|
| $C0 | [INTERRUPT_CONTROL_NR_C0](INTERRUPT_CONTROL_NR_C0.md) - Interrupt control configuration.|
| $C2 | [NMI_RETURN_ADDRESS_LSB_REGISTER_NR_C2](NMI_RETURN_ADDRESS_LSB_REGISTER_NR_C2.md) - LSB of NMI return address.|
| $C3 | [NMI_RETURN_ADDRESS_MSB_REGISTER_NR_C3](NMI_RETURN_ADDRESS_MSB_REGISTER_NR_C3.md) - MSB of NMI return address.|
| $C4 | [INTERRUPT_ENABLE_0_REGISTER_NR_C4](INTERRUPT_ENABLE_0_REGISTER_NR_C4.md) - Interrupt type enable control.|
| $C5 | [INTERRUPT_ENABLE_1_REGISTER_NR_C5](INTERRUPT_ENABLE_1_REGISTER_NR_C5.md) - ctc interrupt enable control.|
| $C6 | [INTERRUPT_ENABLE_2_REGISTER_NR_C6](INTERRUPT_ENABLE_2_REGISTER_NR_C6.md) - UART interrupt enable control.|
| $C8 | [INTERRUPT_STATUS_0_REGISTER_NR_C8](INTERRUPT_STATUS_0_REGISTER_NR_C8.md) - Has interrupt occurred?.|
| $C9 | [INTERRUPT_STATUS_1_REGISTER_NR_C9](INTERRUPT_STATUS_1_REGISTER_NR_C9.md) - Has ctc interrupt occurred?.|
| $CA | [INTERRUPT_STATUS_2_REGISTER_NR_CA](INTERRUPT_STATUS_2_REGISTER_NR_CA.md) - Has UART interrupt happened?.|
| $CC | [DMA_INTERRUPT_ENABLE_0_NR_CC](DMA_INTERRUPT_ENABLE_0_NR_CC.md) - Interrupts that can override DMA.|
| $CD | [DMA_INTERRUPT_ENABLE_1_NR_CD](DMA_INTERRUPT_ENABLE_1_NR_CD.md) - CTC Interrupts that can override DMA.|
| $CE | [DMA_INTERRUPT_ENABLE_2_NR_CE](DMA_INTERRUPT_ENABLE_2_NR_CE.md) - UART Interrupts that can override DMA.|
| $D8 | [I_O_TRAPS_REGISTER_NR_D8](I_O_TRAPS_REGISTER_NR_D8.md) - experimental.|
| $D9 | [I_O_TRAP_WRITE_REGISTER_NR_D9](I_O_TRAP_WRITE_REGISTER_NR_D9.md) - experimental.|
| $DA | [I_O_TRAP_CAUSE_REGISTER_NR_DA](I_O_TRAP_CAUSE_REGISTER_NR_DA.md) - experimental.|
| $F0 | [XDEV_COMMAND_REGISTER_NR_F0](XDEV_COMMAND_REGISTER_NR_F0.md) - Issue 4 only.|
| $F8 | [XADC_REGISTER_NR_F8](XADC_REGISTER_NR_F8.md) - Issue 4 only.|
| $F9 | [XADC_D0_REGISTER_NR_F9](XADC_D0_REGISTER_NR_F9.md) - Issue 4 only.|
| $FA | [XADC_D1_REGISTER_NR_FA](XADC_D1_REGISTER_NR_FA.md) - Issue 4 only.|
| $FF | [DEBUG_LED_CONTROL_NR_FF](DEBUG_LED_CONTROL_NR_FF.md) - Turns debug LEDs on and off on TBBlue implementations that have them.|
|-----|-------------------------------------------------------------------|

## Links

[Index](index.md)