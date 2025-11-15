# Memory 

## Table of contents 

Allowed commands are:

`"-address address"`: Prints out internal information of the debugger for a 64k address. Can be helpful if you encounter e.g. 'Unverified breakpoints' problems.

`"-dasm address count"`: Disassembles a memory area. count=number of lines.
"-eval expr": Evaluates an expression. The expression might contain mathematical expressions and also labels. It will also return the label if the value correspondents to a label.

`"-exec|e cmd args"`: cmd and args are directly passed to the remote (ZEsarUX, CSpect, ...). E.g. `"-exec get-registers"`.

`"-help|h"`: This command. Do "-e help" to get all possible remote (ZEsarUX, CSpect, ...) commands.

`"-label|-l XXX"`: Returns the matching labels (XXX) with their values. Allows wildcard "*".
`"-md address size [dec|hex] [word] [little|big]": Memory dump at 'address' with 'size' bytes. Output is in 'hex' (default) or 'dec'imal. Per default data will be grouped in bytes.
  But if chosen, words are output. Last argument is the endianness which is little endian by default.
`"-mdelta address size string"`: This does a 'delta' search on the address range. The memory is searched for byte sequences that contain the same deltas as the given string. E.g. if you would search for "MIK" not only "MIK" would be found but also "mik" or "njl". The whole memory is dumped but all values are adjusted by an offset to match the searched string. If several sequences are found the memory might be dumped several times.The idea is to find strings also if they are not coded as ASCII sequence but with some other, unknown coding scheme.

`"-memmodel"`: Prints slot and bank info of the currently used memory model.
`"-ml address filepath"`: Loads a binary file into memory. The filepath is relative to the TMP directory.
`"-ms address size filename"`: Saves a memory dump to a file. The file is saved to the temp directory.
`"-msetb address value [repeat]"`:
	address: The address to fill. Can also be a label or expression.
	value: The byte value to set.
	repeat: (Optional) How often the value is repeated.

Examples:
	`"-msetb 8000h 0Fh"` : Puts a 15 into memory location 0x8000.
	`"-msetb 8000h 0 100h"` : fills memory locations 0x8000 to 0x80FF with zeroes.
	`"-msetb fill_colors_ptr+4 FEh"`: If fill_colors_ptr is e.g. 0xCF02 the value FEh is put into location 0xCF06.

`"-msetw address value [repeat [endianness]]:"`
- address: The address to fill. Can also be a label or expression.
- value: The word value to set.
- repeat: (Optional) How often the value is repeated.
- endianness: (Optional) 'little' (default) or 'big'.

Examples:
	"-msetw 8000h AF34h" : Puts 34h into location 0x8000 and AFh into location 0x8001.
	"-msetw 8000h AF34h 1 big" : Puts AFh into location 0x8000 and 34h into location 0x8001.
	"-msetw 8000h 1234h 100h" : fills memory locations 0x8000 to 0x81FF with the word value 1234h.

`"-mv address size [address_n size_n]*"`: Memory view at 'address' with 'size' bytes. Will open a new view to display the memory contents.

`"-mvd address size [address_n size_n]*"`: Opens a memory view that can be used for comparison. I.e. you start at some time than later you update the view and then you can make a diff and search e.g. for all values that have been decremented by 1.
`"-mvw address size [address_n size_n]* [big]"`: Memory view at 'address' with 'size' words. Like -mv but display unit is word instead of byte. Normally the display is little endian. This can be changed by adding "big" as last argument.
`"-patterns [index[+count|-endindex] [...]"`: Shows the tbblue sprite patterns beginning at 'index' until 'endindex' or a number of 'count' indices.

	The values can be omitted. 'index' defaults to 0 and 'count' to 1.
	Without any parameter it will show all sprite patterns.
	You can concat several ranges.
	Example: "-patterns 10-15 20+3 33" will show sprite patterns at index 10, 11, 12, 13, 14, 15, 20, 21, 22, 33.

`-rmv`: Shows the memory register view. I.e. a dynamic view with the memory contents the registers point to.
`"-sprites [slot[+count|-endslot] [...]"`: Shows the tbblue sprite registers beginning at 'slot' until 'endslot' or a number of 'count' slots. The values can be omitted. 'slot' defaults to 0 and 'count' to 1. You can concat several ranges.
	Example: "-sprite 10-15 20+3 33" will show sprite slots 10, 11, 12, 13, 14, 15, 20, 21, 22, 33.
	Without any parameter it will show all visible sprites automatically.
`"-state save|restore|list|clear|clearall [statename]"`: Saves/restores the current state. I.e. the complete RAM + the registers.
`"-wpadd address [size] [type]"`: Adds a watchpoint. See below.
`"-wprm address [size] [type]"`: Removes a watchpoint.
	- address: The 64k address to watch.
	- size: The size of the area to watch. Can be omitted. Defaults to 1.
	- type:
	    - "r": Read watchpoint
	    - "w": Write watchpoint
	    - "rw": Read/write watchpoint. Default.
	Note: This is a leightweight version of the WPMEM watchpoints you can add to your sources.
	      Watchpoints added through "-wpadd" are independent. They are NOT controlled (enabled/disabled) through the
		  vscode's BREAKPOINTS pane.
		  Furthermore they work on 64k addresses (whereas WPMEM works on long addresses).
		  I.e. a watchpoint added through "-wpadd" will break in any bank.

Some examples:
`"-exec h 0 100"`: Does a hexdump of 100 bytes at address 0.
`"-e write-memory 8000h 9fh"`: Writes 9fh to memory address 8000h.
`"-e gr"`: Shows all registers.
`"-eval 2+3*5"`: Results to "17".
`"-msetb mylabel 3"`: Sets the data at memory location 'mylabel' to 3.
`"-mv 0 10"`: Shows the memory at address 0 to address 9.
`"-sprites"`: Shows all visible sprites.
`"-state save 1"`: Stores the current state as 'into' 1.
`"-state restore 1"`: Restores the state 'from' 1.

Notes:
For all commands (if it makes sense or not) you can add "-view" as first parameter. This will redirect the output to a new view instead of the console.
E.g. use "-help -view" to put the help text in an own view.
