## nextlib.bas
## nextlib.bas

- Sub Routines : 58
- Functions    : 8

sub BankPoke(bank as ubyte, offset as uinteger, value as ubyte)
sub BankPokeUint(bank as ubyte, offset as uinteger, value as uinteger)
sub RunAT(speed as ubyte)
Sub CopyToBanks(startb as ubyte, destb as ubyte, nrbanks as ubyte)
sub BankToRam(start_bank as ubyte, dest_mem as uinteger, dest_len as uinteger)
sub ClearBanks(startb as ubyte, number_of_banks as ubyte=1)
Sub MMU8new(byval slot as ubyte, byval memorybank as ubyte)
Sub MMU8(byval nn as ubyte, byval na as ubyte)
Sub MMU16(byval memorybank as ubyte)

Sub ScrollLayer(byval x as ubyte,byval y as ubyte)
SUB PlotL2(byVal X as ubyte, byval Y as ubyte, byval T as ubyte)
SUB PlotL2Shadow(byVal X as ubyte, byval Y as ubyte, byval T as ubyte)
sub FPlotL2(y as uinteger,x as uinteger, c as ubyte)
SUB CIRCLEL2(byval x as ubyte, byval y as ubyte, byval radius as ubyte, byval col as ubyte)

Sub NextRegA(reg as ubyte,value as ubyte)
sub swapbank(byVal bank as ubyte)
SUB zx7Unpack(source as uinteger, dest AS uinteger)

Sub InitSprites(byVal Total as ubyte, spraddress as uinteger, bank as uinteger=0)
Sub InitSprites2(byVal Total as ubyte, spraddress as uinteger,bank as ubyte, sprite as ubyte=0)
sub ShowSprites(flag as ubyte)
sub RemoveSprite(spriteid AS UBYTE, visible as ubyte)
sub UpdateSprite(ByVal x AS uinteger,ByVal y AS UBYTE,ByVal spriteid AS UBYTE,ByVal pattern AS UBYTE,ByVal mflip as ubyte=0,ByVal anchor as ubyte=0)

sub LoadBMP(byval fname as STRING)
sub FreeBank(bank as ubyte)

Sub LoadSDBank(byval filen as String,ByVal address as uinteger,ByVal length as uinteger,ByVal offset as ulong, bank as ubyte)
Sub LoadSD(byval filen as String,ByVal address as uinteger,ByVal length as uinteger,ByVal offset as ulong)
Sub SaveSD(byval filen as String,ByVal address as uinteger,ByVal length as uinteger)

SUB DoTileBank16(byVal X as ubyte, byval Y as ubyte, byval T as ubyte, byval B as ubyte)
SUB DoTile8(byVal X as ubyte, byval Y as ubyte, byval T as ubyte)
SUB DoTileBank8(byVal X as ubyte, byval Y as ubyte, byval T as ubyte, byval b as ubyte)
SUB DoTileBank8Test(byVal X as ubyte, byval Y as ubyte, byval T as ubyte, byval b as ubyte, byval c as ubyte)
sub FDoTile16(tile as ubyte, x as ubyte ,y as ubyte, bank as ubyte)
sub FDoTile8(tile as ubyte, x as ubyte ,y as ubyte, bank as ubyte)

Sub L2Text(byval x as ubyte,byval y as ubyte ,m$ as string, fntbnk as ubyte, colormask as ubyte)
Sub FL2Text(byval x as ubyte,byval y as ubyte ,byval m$ as string, fntbnk as ubyte)

sub ShowLayer2(enable as ubyte)
sub FPlotLineV(y as ubyte ,x as uinteger ,h as ubyte, c as ubyte)
sub FPlotLineW(y as ubyte ,x as uinteger ,w as uinteger, c as ubyte)
sub DrawImage(xpos as uinteger, ypos as ubyte, img_data as uinteger, frame as ubyte = 0 )

sub InitPalette(pallete_sel as ubyte, bank as ubyte=0, start as uinteger=0, colcount as ubyte=0,offset as ubyte=0)
SUB PalUpload(ByVal address as uinteger, byval colours as ubyte,byval offset as ubyte, bank as ubyte=0)
sub SelectPalette(p as ubyte)

Sub ClipLayer2( byval x1 as ubyte, byval x2 as ubyte, byval y1 as ubyte, byval y2 as ubyte )
Sub ClipULA( byval x1 as ubyte, byval x2 as ubyte, byval y1 as ubyte, byval y2 as ubyte )
Sub ClipTile( byval x1 as ubyte, byval x2 as ubyte, byval y1 as ubyte, byval y2 as ubyte )
Sub ClipSprite( byval x1 as ubyte, byval x2 as ubyte, byval y1 as ubyte, byval y2 as ubyte )

sub TileMap(byval address as uinteger, byval blkoff as ubyte, byval numberoftiles as uinteger,byval x as ubyte,byval y as ubyte, byval width as ubyte, byval mapwidth as uinteger)

sub FlipBuffer()
sub EnableShadow()
sub DisableShadow()

sub WaitRetrace(byval repeats as uinteger)
sub WaitRetrace2(byval repeats as ubyte)

sub WaitKey()

sub Console(db_string as string)

sub CopyBank(startb as ubyte, destb as ubyte, nrbanks as ubyte)
sub CopyFromBank(cfb_sourceb as ubyte, cfb_dest_address as UINTEGER, cfb_lenght as UINTEGER)
sub dbMemory(db_address as uinteger, db_len as uinteger)
sub Debug(BYVAL x as UBYTE,byval y as ubyte, s as string)

function NStr(ins as ubyte) as string
function BinToString(num as ubyte) as String
function BankPeek(bank as ubyte, offset as uinteger) as ubyte
function BankPeekUint(bank as ubyte, offset as uinteger) as uinteger

Function GetMMU(byval slot as ubyte) as ubyte
function check_interrupts() as ubyte
Function GetReg(byval slot as ubyte) as ubyte
Function ReserveBank() as ubyte
