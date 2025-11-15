<style>
  .highlight {
    background-color: #222;
    color: #ffd700;
    padding: 4px 8px;
    border-radius: 4px;
  }
  .section {
    background-color: #1a1a1a;
    border-left: 4px solid #007acc;
    padding: 10px;
    margin-bottom: 12px;
  }
  .note {
    background: #2c2c2c;
    padding: 10px;
    border-left: 4px solid #66bb6a;
    margin-top: 10px;
  }
</style>

# 🎉 <span style="color:#4ec9b0;">Welcome To</span>
<img src="./Docs/NB-1024x169.png" alt="NextBuildStudio" width="40%"> 

### <span class="highlight">v2025.11.06 </span> &nbsp;&nbsp;🔗 [zxnext.uk/nextbuild](https://zxnext.uk/nextbuild)

---

Welcome to **NextBuild Studio (NBS)** — your one-stop shop for building and creating exciting new **ZX Spectrum Next** games and applications.

Built on the powerful [**Boriel ZX Basic Compiler**](https://github.com/boriel-basic/zxbasic) by [boriel](https://zxbasic.readthedocs.io/en/docs/), NBS adds robust hardware support with custom libraries to unleash the full potential of the Next:

- 🕹️ Edit Sprites with `.spr`, `.til`, `.fnt` support  
- 🎵 Sampled sound, PT3 music, SFX playback  
- 🎨 Full 256-colour support, DMA & Copper effects  
- 💻 Integrated development with hover-help and inline docs  
- ⚡ One-click compile & run with CSpect  
- 🧠 Real-time syntax checks and auto-snippets

This document is a small taste, with the more complete help system available by pressing `F1`

---

## 🚀 Getting Started

In NBS, you'll edit `.bas` files and build with the **Compile** button (bottom bar) or by pressing `F6`.

Try now:
- Click on [**holymoley.bas**](./NextBuild_Examples/HoleyMoley/holeymoley.bas)  
- Then click **Compile** or press `F6 → Build Source`  
- The app will build and auto-launch in CSpect!

You’ll see the **Explorer** open the folder on the left. Use the inline docs and hover-help to explore each keyword — press **F1** for more info!

---

## 🛠️ Built-in Tools

- 🧱 **Sprite Editor** (`.spr`, `.til`, `.fnt`, `.nxm`)
- 🗺️ **Map Editor** (`.nxm`)
- 🖼️ **Image Importer** (sprites, panels, convert images)
- 🧩 **Block Editor** (composite sprite editing)
- 🔍 **Image Viewer** (`.nxi`, `.sl2`)
- 📘 **Inline Help** and ZX Basic Docs (F1)
- ✅ **Syntax Checker**, **Snippets**, and **Templates**
- 🔊 **PT3 Player** (Windows only) - Right click a ```.pt3``` file in the explorer to play, ```esq``` to quit
- 🎹 **AYFX editor** ``Ctrl+Shift+P``, type ``"AYFX"``
- 🚦More commands available in the **Command Palette** ```ctrl+shift+p``` and type ```NextBuild```

---

## 🧪 How It Works

- Every keyword supports **hover help**  
- Inline help shows when you press `F1` on a word  
- `F1` on nothing opens the full help system  
- Snippets expand when triggered by hover-help  

---

## 📂 Quick Access

### 💻 Example Projects
- [📝 Hello World](./NextBuild_Examples/HelloWorld/HelloWorld.bas)
- [🕹️ Sprite Demo](./NextBuild_Examples/Sprites/SpriteDemo.bas)
- [🕹️ Comprehensive Sprites](./NextBuild_Examples/Sprites/ScaleRotataSprite.bas)
- [🎯 Template](./NextBuild_Examples/Template.bas)
- [📖 Start Here](./Docs/Introduction.md)

### ⚙️ Tasks & Commands
- [▶ Run Emulator](command:workbench.action.tasks.runTask?%5B%22Start%20Cspect%22%5D)
- [🛠️ Build File](command:workbench.action.tasks.build)
- [⚙ Open Settings](command:workbench.action.openSettings)

### 📚 Help & Documentation
- [🔤 Keyword Help](command:nextbuild-viewers.showKeywordHelp)
- [🧠 Z80 Tips](./docs/Z80Tips.md)
- [📦 Compiler Settings](./docs/CompilerSettings.md)

---

<div class="note">
💡 <strong>Tip:</strong> You can click on any <code>.bas</code> file above to load it directly into the editor!
</div>

---

## 🙏 Credits

NextBuild Studio has been developed over many years by **David Saphier**, and wouldn't be possible without support and contributions from:

- **boriel https://ko-fi.com/boriel**  
- **D Xalior Rimron-Soutter https://zx.xalior.com/**  
- **Mike “Flash” Ware https://www.rustypixels.uk/**  
- **Mike Dailly https://lemmings.info/**  
- **Peter Helcmanovsky https://ped7g.itch.io/**
- **Remy Sharp https://remysharp.com/**  
- **Jari Komppa https://solhsa.com/**
- **DuefectuCorp http://duefectucorp.com/**
- **Leslie Greenhalgh**
- **Richard Faulkner**

```Sorry to anyone I have missed, there have been so many people that have helped over the years, I thank you all.```

---

## 📝 Notices

- **NextBuild-Studio** and its components are © 2025 **David Saphier**, unless otherwise noted.  
- **Boriel Basic** is © José Rodríguez  
- **CSpect** is © Mike Dailly

---
