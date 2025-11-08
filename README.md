# 💠 Modern Terminal Assistant

A **voice-enabled smart terminal** built with Python that runs inside **WSL**, **PowerShell**, or **Git Bash**.  
It allows you to open applications, execute commands, perform web searches, and even control Spotify —  
while logging every action and providing **spoken feedback** through text-to-speech.

---

## 🚀 Features

- 🧠 **Smart Command Handling**
  - Supports intuitive commands like:
    - `open vscode`
    - `open chrome`
    - `open spotify:`
    - `search neuralink`
    - `run ls -l`
  - Any unknown command is executed as a shell command.

- 🗣️ **Voice Feedback**
  - Uses `pyttsx3` for speech synthesis.
  - Works with **eSpeak-ng** in WSL or native TTS on Windows.

- 🧾 **Event Logging**
  - Automatically logs every action and command in `~/assistant_log.txt`.

- 🎵 **Spotify Mode**
  - Type `open spotify:` to enter dedicated Spotify control mode.
  - Commands supported in Spotify Mode:
    - `play <song name>`
    - `pause`
    - `next`
    - `search <query>`
    - `exit spotify`


---

## ⚙️ Installation (For WSL / Git Bash)

### 1️⃣ Navigate to your project folder

```bash
cd /mnt/c/Users/<yourname>/Project/terminal

python3 -m venv venv
source venv/bin/activate
pip install pyttsx3 rich

sudo apt update
sudo apt install espeak-ng -y

sudo apt install dos2unix -y
dos2unix /mnt/c/Users/<yourname>/Project/terminal/ai-terminal.sh
dos2unix /mnt/c/Users/<yourname>/Project/terminal/venv/Scripts/activate

chmod +x ai-terminal.sh
./ai-terminal.sh
```
```
💠 WSL AI Terminal Assistant
> open vscode
[2025-11-08 10:25:36] Opened app: vscode


```

### For Windows / PowerShell Users

If you want to run it directly on Windows, use this PowerShell command:
```
cd C:\Users\<yourname>\Project\terminal
.\venv\Scripts\activate
python .\ai_terminal.py
```
You can also create a batch file (run_assistant.bat) with:

```
@echo off
cd C:\Users\<yourname>\Project\terminal
call venv\Scripts\activate
python ai_terminal.py
pause
```

### 🧠 Future Enhancements

🎙️ Voice Command Recognition (speech input)

🪟 Cross-platform GUI Dashboard for viewing logs and running commands

🧩 Plugin System for adding integrations (e.g., file search, web automation)

🤖 OpenAI Chat Integration for natural conversation

🌐 Local Web Dashboard to visualize logs and analytics



