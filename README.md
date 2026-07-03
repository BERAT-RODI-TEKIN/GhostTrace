<div align="center">

```
   ______  __               __  ______                    
  / ____/ / /_  ____  _____/ /_/_  __/________ _________  
 / / __  / __ \/ __ \/ ___/ __// / / ___/ __ `/ ___/ _ \ 
/ /_/ / / / / / /_/ (__  ) /_ / / / /  / /_/ / /__/  __/ 
\____/ /_/ /_/\____/____/\__//_/ /_/   \__,_/\___/\___/  
```

**👻 GhostTrace — OSINT Username Hunter**

![Version](https://img.shields.io/badge/version-1.0-cyan?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Platforms](https://img.shields.io/badge/platforms-300%2B-purple?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/BERAT-RODI-TEKIN/GhostTrace?style=for-the-badge)

*Hunt any username across 300+ platforms in seconds.*

</div>

---

## 🔍 What is GhostTrace?

GhostTrace is an open-source OSINT tool that searches for a target username across **300+ platforms** simultaneously using multi-threading. Results are displayed in a clean neon terminal UI and saved to a text file.

> ⚠️ **For educational and ethical use only.** Only search usernames you own or have permission to search.

---

## ✨ Features

- 👻 **300+ platforms** — social media, gaming, coding, forums & more
- ⚡ **Multi-threaded** — blazing fast with configurable thread count
- 🎨 **Neon terminal UI** — cyan/green color-coded results
- 💾 **Auto-save** — results saved to `results/<username>.txt`
- 🔧 **Extensible** — easily add new platforms via `data/platforms.json`

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/BERAT-RODI-TEKIN/GhostTrace.git
cd GhostTrace

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
# Basic usage
python3 ghosttrace.py <username>

# With custom thread count
python3 ghosttrace.py <username> -t 50

# Without saving results
python3 ghosttrace.py <username> --no-save

# Interactive mode
python3 ghosttrace.py
```

### Examples

```bash
python3 ghosttrace.py johndoe
python3 ghosttrace.py johndoe -t 30
```

---

## 📁 Project Structure

```
GhostTrace/
├── ghosttrace.py          # Main entry point
├── modules/
│   ├── checker.py         # Platform checker (multi-threaded)
│   └── display.py         # Terminal UI & colors
├── data/
│   └── platforms.json     # Platform list (easily extendable)
├── results/               # Saved results (auto-created)
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🌐 Supported Platform Categories

| Category | Examples |
|----------|----------|
| 🌐 Social Media | Instagram, Twitter/X, TikTok, Snapchat |
| 💻 Dev & Code | GitHub, GitLab, HackerRank, LeetCode |
| 🎮 Gaming | Steam, Xbox, PSN, Roblox, Chess.com |
| 🎵 Music | Spotify, SoundCloud, Last.fm, Bandcamp |
| 📺 Video | YouTube, Twitch, Kick, Rumble |
| 🔒 Security | HackerOne, BugCrowd, RootMe, TryHackMe |
| ✍️ Writing | Medium, Substack, Wattpad, Dev.to |
| 🤝 Professional | LinkedIn, AngelList, Behance, Dribbble |
| + many more | 300+ platforms total |

---

## ➕ Adding New Platforms

Edit `data/platforms.json` and add an entry:

```json
{
  "name": "ExampleSite",
  "url": "https://example.com/users/{}",
  "check": "status_code",
  "expected": 200
}
```

**Check methods:**
- `status_code` — checks HTTP response code
- `not_found_text` — checks if text is absent from response

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

Made with 👻 by [Berat Rodi Tekin](https://github.com/BERAT-RODI-TEKIN)

*If you found this useful, leave a ⭐ on GitHub!*

</div>
