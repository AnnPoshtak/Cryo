<div align="center">

<h1>❄️ Cryo</h1>
<h3>Absolute Zero for Your Processes</h3>

<p>
<img src="https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/platform-Linux-black?style=for-the-badge&logo=linux">
<img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
</p>

<p><strong>Cryo is a CLI tool for instantly "freezing" processes.</strong><br>
Free up your CPU resources without losing session data or closing your apps.</p>

<p>
<a href="#why-cryo">Why Cryo?</a> • <a href="#installation">Installation</a> • <a href="#usage">Usage</a>
</p>

</div>

<hr>

<h2 id="why-cryo">🚀 Why Cryo?</h2>

<p>Many alternatives are either too complex or unsafe. <strong>Cryo</strong> strikes the perfect balance between speed and stability.</p>

<ul>
<li>⚡ <strong>Lightning Fast:</strong> Built on Python using the powerful <code>psutil</code> library.</li>
<li>🛡️ <strong>Smart Protection:</strong> Cryo will not allow you to freeze critical system processes or non-existent PIDs.</li>
<li>🕸️ <strong>Deep Freeze:</strong> Suspends not just the main application, but all its "children" (child processes) — perfect for heavy browsers and IDEs.</li>
</ul>

<blockquote>
⚠️ <strong>Disclaimer:</strong> Cryo works at the OS signal level (SIGSTOP/SIGCONT). While 99% of apps resume perfectly, some (especially those relying on real-time network connections) may crash or restart upon "unfreezing."
</blockquote>

<hr>

<h2 id="installation">🛠 Installation</h2>

<p>To get started, you need <strong>Python 3.10+</strong>. We strongly recommend using <code>pipx</code> to keep your system clean.</p>

<h3>1. System Prep (Python + pipx)</h3>

<p>Choose your fighter (distro):</p>

<h4>🐧 Arch Linux / Manjaro</h4>
<pre><code class="language-bash">sudo pacman -Syu python python-pipx</code></pre>

<h4>🟠 Ubuntu / Debian</h4>
<pre><code class="language-bash">sudo apt update && sudo apt install python3 pipx</code></pre>

<h4>🔵 Fedora</h4>
<pre><code class="language-bash">sudo dnf update && sudo dnf install python3 pipx</code></pre>

<h3>2. Install Cryo</h3>

<p>Clone the repo and install it as a global command:</p>

<pre><code class="language-bash"># 1. Clone the code
git clone https://github.com/AnnPoshtak/Cryo

# 2. Enter the directory
cd Cryo

# 3. Install in editable mode
pipx install -e .

# 4. Ensure path is set (optional, depending on your shell)</code></pre>

<p>🔥 <strong>Final Step:</strong> Restart your terminal (or log out/log in) so your system recognizes the new <code>cryo</code> command.</p>

<hr>

<h2 id="usage">💻 Usage</h2>

<p>Controlling time is easy. Just use <code>freeze</code> and <code>unfreeze</code>.</p>

<h3>🥶 Freeze</h3>

<p>Suspends the application and all its sub-processes, instantly dropping CPU usage to zero.</p>

<pre><code class="language-bash">cryo freeze firefox</code></pre>

<h3>🥵 Unfreeze</h3>

<p>Brings the application back to life exactly where you left off.</p>

<pre><code class="language-bash">cryo unfreeze firefox</code></pre>

<hr>

<div align="center">

<p>💬 I’d be super happy to get your feedback! This is just the beginning, and the project will continue to grow and improve. Your thoughts and suggestions are very welcome!</p>

<p><strong>Made with ❤️ and Python</strong></p>
<p>If you like this tool — give it a ⭐ on GitHub!</p>

</div>