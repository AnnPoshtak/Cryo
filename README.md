<div align="center">❄️ Cryo

Absolute Zero for Your Processes

<p>
<img src="https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/platform-Linux-black?style=for-the-badge&logo=linux">
<img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
</p><p><strong>Cryo is a CLI tool that instantly "pauses" processes to free up CPU resources.</strong><br>
No need to close apps or lose your work — just put them into a temporary "coma" and bring them back whenever you want.</p><p>
</p></div><hr>🚀 Why Cryo?

Tired of your CPU overheating while dozens of browser tabs or apps are running? Cryo pauses them instantly without closing anything.

Many alternatives are either too complex or risky. Cryo strikes the perfect balance between speed, safety, and simplicity.

Features

⚡ Lightning Fast: Built on Python using the powerful psutil library.

🛡️ Smart Protection: Prevents freezing critical system processes or non-existent PIDs.

🕸️ Deep Freeze: Suspends the main application and all its child processes — perfect for heavy browsers and IDEs.


> ⚠️ Disclaimer: Cryo works at the OS signal level (SIGSTOP/SIGCONT). Most apps resume perfectly, but some (especially network-heavy) may crash or restart upon unfreezing.




---

🛠 Installation

Python 3.10+ is required. We recommend using pipx to keep your system clean.

1. System Prep (Python + pipx)

Choose your distro:

```shell
#Arch Linux / Manjaro

sudo pacman -Syu python python-pipx

#Ubuntu / Debian

sudo apt update && sudo apt install python3 pipx

#Fedora

sudo dnf update && sudo dnf install python3 pipx
```

2. Install Cryo

```shell
# Clone the code
git clone https://github.com/AnnPoshtak/Cryo

# Enter the directory
cd Cryo

# Install in editable mode
pipx install -e .

# Optional: ensure PATH is set
pipx ensurepath
```

🔥 Final Step: Restart your terminal or log out/in so cryo command is recognized.


---

💻 Usage

Take control of your CPU — just freeze and unfreeze.

🥶 Freeze

Suspends the application and all its sub-processes instantly.
```shell
cryo freeze firefox
```

🥵 Unfreeze

Brings the application back exactly where you left off.
```shell
cryo unfreeze firefox
```

---

<div align="center">💬 Cryo is just getting started! Your feedback helps make it better for everyone.
If Cryo saved your laptop today, a ⭐ would help others discover it too!

<strong>Made with ❤️ and Python</strong>

</div>