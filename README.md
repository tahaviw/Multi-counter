# Multi-Timer Utility

A compact, dark-mode desktop application with four independent countdown timers.

## Features

- **4 Independent Timers**: 15s (Cyan), 1m (Emerald), 5m (Amber), 15m (Purple)
- **Smooth Animation**: 100ms update interval for fluid progress bars
- **Dark Mode UI**: Modern dark theme with custom colored progress bars
- **Fixed Compact Size**: 450x280 pixels, non-resizable widget form factor
- **Independent Looping**: Each timer loops seamlessly when reaching 100%
- **Pause & Resume**: Stop preserves current progress; resume picks up where you left off
- **Reset Option**: Fully reset all timers to zero with one click

---

## Installation & Setup

### Step 1: Install Python

**On Windows:**
1. Go to [python.org/downloads](https://python.org/downloads)
2. Download Python 3.8 or newer (Python 3.12 recommended)
3. **IMPORTANT**: During installation, check the box **"Add Python to PATH"**
4. Click "Install Now"
5. Verify installation by opening Command Prompt and running:
   ```
   python --version
   ```

**On Linux (Arch, Ubuntu, etc.):**
```bash
sudo pacman -S python  # Arch
sudo apt install python3  # Debian/Ubuntu
python3 --version
```

**On macOS:**
```bash
brew install python3
python3 --version
```

### Step 2: Install PyQt6

Open your terminal (Command Prompt on Windows, Terminal on Linux/macOS):

```bash
pip install PyQt6
```

### Step 3: Verify Installation

```bash
python -c "from PyQt6.QtWidgets import QApplication; print('PyQt6 installed successfully!')"
```

---

## Running the Application

### Windows

#### Method 1: Command Prompt
```bash
cd Downloads\Multi-counter
python timer_app.py
```

#### Method 2: PowerShell
```powershell
cd $env:USERPROFILE\Downloads\Multi-counter
python timer_app.py
```

#### Method 3: Double-Click
1. Navigate to the `Multi-counter` folder
2. Right-click `timer_app.py`
3. Select "Edit with IDLE" then press F5 to run
4. Or: Right-click → "Open with" → "Choose another app" → select Python

### Linux

```bash
cd ~/Downloads/Multi-counter
python3 timer_app.py

# Or if you have a virtual environment:
source venv/bin/activate
python timer_app.py
```

### macOS

```bash
cd ~/Downloads/Multi-counter
python3 timer_app.py
```

---

## User Guide

### The Interface

```
+--------------------------------------------------+
|  Multi-Timer Utility                             |
|                                                  |
|  [=========>        ] 15s                        |
|  [====>            ] 1m                         |
|  [==>              ] 5m                         |
|  [>                ] 15m                        |
|                                                  |
|       [Reset]    [Stop]    [Start]               |
+--------------------------------------------------+
```

- **Progress Bars**: Show real-time countdown progress for each timer
- **Labels**: Display the total duration for each timer (15s, 1m, 5m, 15m)

### Controls

| Button | Action |
|--------|--------|
| **Start** | Starts all four timers simultaneously from their current positions |
| **Stop** | Pauses all timers instantly, preserving their current progress |
| **Reset** | Resets all timers back to 0% and stops them |

### How to Use

1. **Start All Timers**: Click the green **Start** button. All four timers begin counting down at once.

2. **Pause Mid-Countdown**: Click **Stop** to pause everything instantly. Your progress is saved exactly where it was.

3. **Resume**: Click **Start** again. All timers resume from their paused positions.

4. **Reset**: Click **Reset** to clear all timers and start fresh from 0%.

5. **Automatic Looping**: When a timer reaches 100%, it automatically resets to 0% and starts again immediately.

### Timer Details

| Timer | Duration | Color | Best For |
|-------|----------|-------|----------|
| Timer 1 | 15 seconds | Cyan/Blue | Quick breaks, short tasks |
| Timer 2 | 1 minute | Emerald Green | Short intervals, standing reminders |
| Timer 3 | 5 minutes | Amber/Orange | Pomodoro-style focus sessions |
| Timer 4 | 15 minutes | Purple/Magenta | Deep work blocks, extended tasks |

### Example Use Cases

**Pomodoro Technique:**
1. Click Start to begin your 5-minute focus session
2. Timer 3 (5m) tracks your work period
3. When it loops, take a 1-minute break (Timer 2)
4. Repeat for productivity cycles

**Meeting Timer:**
1. Set Timer 4 (15m) as your meeting duration
2. Click Start to begin
3. Watch the progress bar to gauge remaining time
4. Timer auto-loops for the next meeting

**Exercise Intervals:**
1. Timer 1 (15s) for quick exercise intervals
2. Timer 2 (1m) for rest periods
3. Toggle Start/Stop to pause between sets

---

## File Structure

```
Multi-counter/
├── timer_app.py      # Main application file
└── README.md         # This file
```

---

## Technical Details

- **Framework**: PyQt6 for modern, cross-platform UI rendering
- **Timer Implementation**: QTimer with 100ms PreciseTimer interval
- **Timing Accuracy**: Millisecond-precision tracking ensures accurate countdowns
- **Threading**: Uses PyQt's signal/slot mechanism (no separate threads needed)
- **Styling**: Custom QSS stylesheet for dark mode appearance
- **Platform Support**: Windows, Linux, macOS

---

## Troubleshooting

### "python is not recognized" (Windows)

1. Search "Environment Variables" in Start Menu
2. Click "Edit the system environment variables"
3. Click "Environment Variables"
4. Under "System variables", find "Path" and click "Edit"
5. Click "New" and add: `C:\Python312\` (adjust to your Python install path)
6. Restart your Command Prompt and try again

### "No module named 'PyQt6'" (Windows)

```powershell
pip install PyQt6
```

### Application doesn't open (Linux)

Make sure you have a display environment running:
```bash
# For headless servers, use Xvfb:
xvfb-run -a python3 timer_app.py
```

### tk window error (macOS)

If you see display errors on macOS, ensure X11 is installed or use Wayland:
```bash
# Install XQuartz if needed
brew install --cask xquartz
```

---

## License

MIT License