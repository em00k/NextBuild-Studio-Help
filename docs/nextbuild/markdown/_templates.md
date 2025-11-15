# Templates
- [Templates](#templates)
  - [System Assets](#system-assets)
    - [Example](#example)
  - [Project Creator](#project-creator)
    - [Creating a proect](#creating-a-proect)

## System Assets

NextBuild now comes with a special operator that allows you to load `stock` data, such as fonts and palettes. The files are stored in the `Scripts/system_data`. The files in this folder will be available to all projects when loaded using the ``[]`` indicator. This identifier is replaced by ``nextbuild.py`` when the program is compiled into a NEX. 

### Example
```
LoadSDBank("[]atserix_font.fnt",0,0,0,34)
```
Will load the assets from ```ROOT/Scripts/System/``` 

So far the following files are available: 
- aterix_font.fnt ([``L2Text``](l2text.md) font)
- mouse.spr (16x16 mouse sprite)
- TESKO.PT3 (6Ch ``pt3`` music file)

## Project Creator

NextBuild Studio can create a new project structure from a set of preset templates. These templates will assist building the correct folder structure for ```modules```, which are used for multi binary applications **```The module system are not 100% complete```**

### Creating a proect 

Click the ```New Project``` Icon on the bottom of the window. The ```Create NextBuild Project``` will open. Fill in the details.

- ```Project Name``` - Name of your project & folder (avoid spaces!)

- ```Preject Template``` - Pick from a list, the structure is shown below

- Ensure the Base Sources direction is correct

- Click ```Create Project```

NBS will ask you if you want to open the project, when you click ``OK`` the project will open in the editor. As it will be build from a template - you should be able to ```Compile``` it right away!
