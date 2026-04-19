# DDLC Ren'Py 8 Port

This is a Doki Doki Literature Club fan work that is not affiliated with Team Salvato. It is designed to be played only after the official game has been completed. You can download Doki Doki Literature Club for free at: [http://ddlc.moe](http://ddlc.moe).

This project focuses on porting *Doki Doki Literature Club!* to the modern Ren'Py 8 engine (Python 3). It fixes runtime crashes caused by the Python 2 to Python 3 cross-generational migration and resolves macOS Gatekeeper App Translocation read-only restriction errors. 

> [!IMPORTANT]  
> **Adherence to Team Salvato IP Guidelines**: To protect the original copyright, this repository **only contains the modified scripts**. It does NOT contain any original `.rpa` audio/image archives or unmodified game campaign scripts.

## 🚀 Why Port to Ren'Py 8? (Benefits)

Upgrading the core engine from Ren'Py 6 (Python 2) to Ren'Py 8 (Python 3) unlocks a massive leap in modernization, providing improvements far beyond basic compatibility:

- **Native Apple Silicon & macOS Game Mode Support**: For macOS users, the engine now natively supports Apple Silicon architecture (M1/M2/M3/M4 chips) and smoothly triggers macOS "Game Mode". This runs noticeably faster, generates significantly less heat, and is drastically more power-efficient than running the original 32-bit x86 client through Rosetta translation.
- **Superior 64-bit Performance**: Bypasses the strict 4GB RAM limits of older 32-bit environments. Coupled with Python 3's engine architecture, runtime memory management and garbage collection are much more stable and performant.
- **Advanced Accessibility & Gamepad Support**: Inherits modern Ren'Py's rendering and pipeline upgrades, bringing much better out-of-the-box support for controllers/gamepads, and system-level accessibility tools (like self-voicing features).
- **Future-Proofing**: Python 2.7 reached end-of-life years ago. Migrating the core logic to Python 3 ensures the game stays alive, secure, and compatible with modern hardware and future OS updates.

## 🌟 Features & Modifications

1. **Python 3 Compatibility Layer (`game/01-py3-compat.rpy`)**
   - Implemented a compatibility shim wrapping `renpy.file` and `open` to fix `bytes` vs `str` read/write bugs that emerged during the Python 3 transition, successfully restoring the game's meta-game file creation sequences (e.g., `hxppy thxughts.png`).
   - Recursively scrubs `Surface` types from `renpy.game.log.log` out of the rollback and save system, fixing a persistent crash that occurred when trying to serialize non-pickleable attributes.
2. **macOS Gatekeeper App Translocation Defense (`game/splash.rpy`, `game/script.rpy`)**
   - Automatically detects if the game is being forced to run under a read-only environment due to App Translocation.
   - Triggers an explicit warning screen giving clear instructions for the user to disable isolation instead of quietly failing later in the gameplay.
3. **Optimized Build Rules (`game/build.rpy`)**
   - Revamped `build.rpy` instructions to prevent packaging leftover `firstrun` flags, cache logs, or `traceback.txt` files that would cause a broken state for new users, while properly packaging archives and filtering source files.
4. **Effects & Credits Modifications (`game/effects.rpy`, `game/zz_credits.rpy`, `game/zz_debug.rpy`)**
   - Adapted built-in legacy functions for effects matching Ren'Py 8 constraints.
   - Includes developer utilities and structural modifications to the end credits sequence.

## ✅ Resolved Issues

- **Credits Text Stutter**: Fixed the end credits text rendering issue by replacing the legacy image-dissolve path with a Ren'Py 8-compatible music-synced text wipe.

## 💾 Installation Guide

Because this repository strictly functions as a Mod/Patch to abide by IP restrictions, you cannot launch it directly as a standalone game. You must pair it with the official DDLC files:

1. Download the original *Doki Doki Literature Club!* game from [ddlc.moe](http://ddlc.moe).
2. Copy all the `.rpa` files (`audio.rpa`, `images.rpa`, `fonts.rpa`, `scripts.rpa`) from the original game's `game/` folder.
3. Paste them into the `game/` folder of this cloned repository.
4. Launch the game or build the distribution using the latest [Ren'Py 8.5+ SDK](https://www.renpy.org/).

### 🍎 For macOS Players

If you build the app on macOS and are met with the warning: *"The game cannot be run because you are trying to run it from a read-only location..."*

Please use one of the following methods to remove Gatekeeper isolation:

- **Method A (Recommended)**: Drag and move the `DDLC` application directly into your `/Applications` folder, then launch it from there.
- **Method B (Terminal)**: Open Terminal and run the following command to remove the quarantine attributes:
  ```bash
  xattr -cr /path/to/your/DDLC.app
  ```

---
*Love, Monika*
