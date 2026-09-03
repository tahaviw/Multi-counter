#!/usr/bin/env python3
"""
Multi-Timer Utility Application
A compact, dark-mode desktop application with four independent countdown timers.
Each timer displays a horizontal progress bar that loops seamlessly.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QFrame, QProgressBar
)
from PyQt6.QtCore import Qt, QTimer as QtCoreTimer
from PyQt6.QtGui import QColor


class TimerWidget(QWidget):
    """Individual timer widget with a progress bar and label."""

    # Tick interval in milliseconds for smooth updates
    TICK_MS = 100  # 10 updates per second for smooth animation

    def __init__(self, duration_seconds, color_hex, color_name, index=None):
        super().__init__()
        self.duration = duration_seconds
        self.color_hex = color_hex
        self.color_name = color_name
        self.index = index

        # Use millisecond-precise elapsed tracking
        self.elapsed_ms = 0
        self.is_running = False

        # Layout
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)

        # Progress bar - range is total milliseconds for accurate fill
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, duration_seconds * 1000)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedHeight(16)
        self.progress_bar.setFixedWidth(180)

        # Timer label
        self.label = QLabel(self._format_label(duration_seconds))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setMinimumWidth(60)

        layout.addWidget(self.progress_bar)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Set fixed height for each timer row
        self.setFixedHeight(40)

        # Initialize PyQt timer (fires every TICK_MS)
        self.timer = QtCoreTimer()
        self.timer.setTimerType(Qt.TimerType.PreciseTimer)
        self.timer.timeout.connect(self._update)

    def _format_label(self, total_seconds):
        """Format duration label (e.g., '15s', '1m', '5m', '15m')."""
        if total_seconds < 60:
            return f"{total_seconds}s"
        minutes = total_seconds // 60
        return f"{minutes}m"

    def start(self):
        """Start the timer."""
        self.is_running = True
        # Do NOT reset elapsed_ms so resume from current position works
        self.timer.start(self.TICK_MS)

    def stop(self):
        """Stop (pause) the timer at current position.
        Retains current elapsed_ms and progress bar value."""
        self.is_running = False
        self.timer.stop()
        # Do NOT reset elapsed_ms or progress bar value

    def reset(self):
        """Fully reset timer to 0."""
        self.is_running = False
        self.timer.stop()
        self.elapsed_ms = 0
        self.progress_bar.setValue(0)

    def _update(self):
        """Update progress and handle looping.
        Uses millisecond-precision timing to ensure accurate countdown."""
        if not self.is_running:
            return

        # Increment by exactly TICK_MS milliseconds
        self.elapsed_ms += self.TICK_MS

        # Loop seamlessly when reaching the full duration
        if self.elapsed_ms >= self.duration * 1000:
            self.elapsed_ms = 0

        # Update progress bar (range is in ms, so value is also in ms)
        self.progress_bar.setValue(self.elapsed_ms)

    def set_color(self):
        """Apply timer-specific color to the progress bar."""
        c = QColor(self.color_hex)

        self.progress_bar.setStyleSheet(f"""
            QProgressBar {{
                border: 1px solid #3a3a55;
                border-radius: 4px;
                background-color: #2d2d44;
                height: 16px;
            }}
            QProgressBar::chunk {{
                background: qlineargradient(spread:pad x1:0 y1:0, x2:1 y2:0,
                    stop:0 rgba({c.red()}, {c.green()}, {c.blue()}, 255),
                    stop:1 rgba({c.red()}, {c.green()}, {c.blue()}, 180));
                border-radius: 3px;
            }}
        """)


class MainWindow(QWidget):
    """Main application window."""

    def __init__(self):
        super().__init__()

        # Window title
        self.setWindowTitle("Multi-Timer Utility")

        # Fixed size - compact widget
        self.setFixedSize(450, 280)

        # Remove title bar maximize button (keep minimize/close)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)

        # Main vertical layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(8)

        # Timer configurations: (duration_seconds, color_hex, color_name)
        # Durations: 15s, 1m (60s), 5m (300s), 15m (900s)
        timer_configs = [
            (15,  "#00d4ff", "cyan"),     # 15 seconds
            (60,  "#50c878", "emerald"),  # 1 minute
            (300, "#ffa500", "amber"),    # 5 minutes
            (900, "#9b59b6", "purple"),   # 15 minutes
        ]

        # Create and add timer widgets
        self.timers = []
        for i, (duration, color_hex, color_name) in enumerate(timer_configs, 1):
            timer = TimerWidget(duration, color_hex, color_name, i)
            timer.set_color()
            main_layout.addWidget(timer)
            self.timers.append(timer)

        # Add stretch to push buttons down
        main_layout.addStretch()

        # Control buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)

        self.start_button = QPushButton("Start")
        self.start_button.setFixedSize(90, 30)
        self.start_button.clicked.connect(self.start_all)

        self.stop_button = QPushButton("Stop")
        self.stop_button.setFixedSize(90, 30)
        self.stop_button.clicked.connect(self.stop_all)

        self.reset_button = QPushButton("Reset")
        self.reset_button.setFixedSize(90, 30)
        self.reset_button.clicked.connect(self.reset_all)

        button_layout.addStretch()
        button_layout.addWidget(self.reset_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.start_button)
        button_layout.addStretch()

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Track running state
        self.is_running = False

        # Apply dark mode styling
        self.apply_dark_mode()

        # Update button states
        self._update_button_states()

    def apply_dark_mode(self):
        """Apply dark theme styling to the entire application."""
        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a2e;
                font-family: 'Segoe UI', Arial, sans-serif;
                color: #e0e0e0;
            }
            QPushButton {
                background-color: #3a3a55;
                color: #e0e0e0;
                border: 1px solid #4a4a66;
                padding: 6px 12px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4a4a66;
            }
            QPushButton:pressed {
                background-color: #5a5a77;
            }
            QPushButton:disabled {
                background-color: #2a2a40;
                color: #6a6a6a;
            }
            QLabel {
                color: #e0e0e0;
                font-size: 13px;
                font-weight: bold;
            }
            QProgressBar {
                border: 1px solid #3a3a55;
                border-radius: 4px;
                background-color: #2d2d44;
            }
        """)

    def start_all(self):
        """Start or resume all timers simultaneously."""
        for timer in self.timers:
            timer.start()
        self.is_running = True
        self._update_button_states()

    def stop_all(self):
        """Stop (pause) all timers at their current positions.
        Progress and elapsed time are preserved."""
        for timer in self.timers:
            timer.stop()
        self.is_running = False
        self._update_button_states()

    def reset_all(self):
        """Reset all timers back to 0."""
        for timer in self.timers:
            timer.reset()
        self.is_running = False
        self._update_button_states()

    def _update_button_states(self):
        """Enable/disable buttons based on running state."""
        self.start_button.setEnabled(not self.is_running)
        self.stop_button.setEnabled(self.is_running)


def main():
    """Application entry point."""
    app = QApplication(sys.argv)

    # Enable high DPI scaling (try several possible attribute names)
    try:
        app.setAttribute(Qt.AA_EnableHighDpiScaling)
    except AttributeError:
        pass

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()