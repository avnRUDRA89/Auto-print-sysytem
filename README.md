# Auto PDF Monitor & Printer

This Python script automates PDF monitoring and printing on Windows. It watches a folder for new or modified PDF files, copies them to a backup folder, and prints them using the default printer or Adobe Reader.

## Features

- 📁 Real-time folder monitoring
- 📄 Auto-detect and process PDF files
- 🗂️ Backup by copying PDFs to a destination folder
- 🖨️ Automatic printing with retry logic
- 💻 Designed for Windows using `watchdog` and `pywin32`

## Requirements

- Python 3.6+
- Windows OS
- Adobe Reader (optional but recommended for controlled printing)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/auto-pdf-printer.git
   cd auto-pdf-printer
