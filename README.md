# Multi-Timer Utility

A compact, dark-mode Windows desktop application with four independent countdown timers.

## Features

- **4 Independent Timers**: 5s (Cyan), 10s (Emerald), 30s (Amber), 60s (Purple)
- **Smooth Animation**: 50ms update interval for fluid progress bars
- **Dark Mode UI**: Modern dark theme with custom colored progress bars
- **Fixed Compact Size**: 450x280 pixels, non-resizable widget form factor
- **Independent Looping**: Each timer loops seamlessly when reaching 100%

## Requirements

- Python 3.8+
- PyQt6

## Installation

### 1. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install PyQt6

```bash
pip install PyQt6
```

## Running the Application

```bash
python timer_app.py
```

## Usage

1. Click **Start** to begin all four timers simultaneously
2. Each progress bar fills independently and loops seamlessly
3. Click **Stop** to halt all timers at their current positions
4. Click **Start** again to restart from zero

## File Structure

```
Multi-counter/
├── timer_app.py      # Main application file
└── README.md         # This file
```

## Technical Details

- **Framework**: PyQt6 for modern UI rendering
- **Timer Implementation**: QTimer with 50ms update interval
- **Threading**: Uses PyQt's signal/slot mechanism (no separate threads)
- **Styling**: Custom QSS stylesheet for dark mode appearance

## License

MIT License