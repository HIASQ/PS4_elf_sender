# PS4 ELF Payload Sender v0.1

A lightweight, interactive Python CLI tool designed to send `.elf` payload files to a jailbroken PlayStation 4 console over the local network. 

This script improves upon basic socket senders by adding a dynamic user experience and configuration persistence.

## 🚀 Features

- **Persistent Configuration:** Automatically saves the last used IP address and Port to a `config.txt` file, saving you from re-typing them every time.
- **Smart ELF Scanner:** Automatically scans its own directory for any `.elf` files and displays them in a numbered menu for quick selection.
- **Network Stability:** Implements optimized chunk sizes (`8192 bytes`) and a minor delay (`time.sleep`) to prevent payload crashes or the notorious `WinError 10054` (connection reset by peer) error.
- **Pure Python:** No external dependencies required. Built completely using standard Python libraries (`socket`, `os`, `time`).

## 📋 Requirements

- Python 3.x installed on your PC.
- A jailbroken PS4 connected to the same local network (LAN/Wi-Fi).
- A Payload Receiver (like `BinLoader` or `GoldHEN`'s built-in loader) running on your PS4.

## 🔧 How to Use

1. Clone or download this repository.
2. Place your `.elf` payload files (e.g., `goldhen.elf`, `ftp.elf`) inside the **same folder** as the script.
3. Run the script using your terminal:
   ```bash
   python payload_sender.py
   ```
4. Enter your PS4's **IP Address** and the **Port** (usually `9090` or `9021`). For future runs, you can just press **Enter** to use the saved defaults.
5. Select the payload you want to send by typing its corresponding number from the list.
6. Press **Enter** to transmit the file to your console.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
