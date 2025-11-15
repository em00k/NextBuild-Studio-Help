# UpdateSprite(x,y,sprite id, sprite image, attribute 3, attribute 4)

## Syntax

```
UpdateSprite(x,y,sprite id, sprite image, attribute 3, attribute 4)
```

## Description

Updates a specified sprite according to its "sprite id". Sprites must first be upload to sprite ram. Once this has been done the UpdateSprite command can then be used to control the sprites.

- Sprites can be full screen over the border, x int - x position 0 - 319
- y as byte - y position 0 -255
- sprite id = 0 - 127 sprites id
- sprite image = image associate with the id
- Sprite attribute 3
- Sprite attribute 4

Sprite attributes 3 and 4 can control rotation, scaling, flipping, anchoring, and 4 bit mode. See [Sprites](Sprites.md) for more information.

**Examples**

Load and show sprite id 0 with image 0, not that x / y position 0,0 is in the top left hand corner and behind the border until we places sprite on top.

```
InitSprites(8,@Sprites) : ' init 8 sprites from address label Sprite:
' update sprite 0, using image 1 at x,y position 32,32, 
UpdateSprite(32,32,10,1,0,0) 
```


**Remarks**

## Links 

- [InitSprites()](InitSprites.md)
- [InitSprites2()](InitSprites2.md)