<div align="center">❄️ Cryo

Absolute Zero for Your Processes

<p>
<img src="https://img.shields.io/badge/rust-2021%2B-orange?style=for-the-badge&logo=rust">
<img src="https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-black?style=for-the-badge&logo=linux">
<img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
</p>

<p><strong>Cryo is a blazing-fast CLI tool written in Rust that instantly "pauses" processes to free up CPU resources.</strong><br>
No need to close apps or lose your work — just put them into a temporary "coma" and bring them back whenever you want.</p>
</div>

<hr>

🚀 Why Cryo?

Tired of your CPU overheating while dozens of browser tabs or apps are running? Cryo pauses them instantly without closing anything.

Many alternatives are either too complex or risky. Written from scratch in **Rust**, Cryo strikes the perfect balance between extreme speed, memory safety, and simplicity.

### Features

* ⚡ **Blazing Fast:** Powered by Rust and the optimized `sysinfo` crate for near-zero overhead.
* 🛡️ **Smart Protection:** Built-in safeguards prevent freezing critical system processes or your own terminal session.
* 🕸️ **Deep Freeze:** Recursively suspends the main application and all its child processes — perfect for heavy modern browsers and IDEs.

> ⚠️ **Disclaimer:** Cryo works at the OS signal level (`SIGSTOP`/`SIGCONT` on Unix, thread suspension on Windows). Most apps resume perfectly, but some (especially network-heavy ones) may time out, crash, or restart upon unfreezing.

---

🛠 Installation

To compile Cryo, you need the Rust toolchain installed on your system. If you don't have it yet, get it via [rustup.rs](https://rustup.rs/).

### 1. Clone the repository
```shell
git clone [https://github.com/AnnPoshtak/Cryo](https://github.com/AnnPoshtak/Cryo)
cd Cryo
```
### 2. Build and install
You can compile the optimized release binary and move it directly to your Cargo binaries path so it's accessible from anywhere:
```shell
cargo install --path .
```
### 🔥 Final Step: Make sure ~/.cargo/bin is in your system's PATH. If it is, you can now use the cryo command anywhere!

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

🖥️ Show

Shows all processes with their PID

```shell
cryo show
```

🔌 Status

Shows the status of the selected process

```shell
cryo status firefox
```
---

<div align="center">💬 Cryo is just getting started! Your feedback helps make it better for everyone.
If Cryo saved your laptop today, a ⭐ would help others discover it too!

<strong>Made with ❤️ and Rust</strong>

</div>