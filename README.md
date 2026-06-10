```text
╔════════════════════════════╗
║  ██████╗  ██████╗ ██╗  ██╗ ║
║  ██╔══██╗██╔═══██╗╚██╗██╔╝ ║
║  ██████╔╝██║   ██║ ╚███╔╝  ║
║  ██╔══██╗██║   ██║ ██╔██╗  ║
║  ██║  ██║╚██████╔╝██╔╝ ██╗ ║
║  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ║
║                            ║
║  XOR Header Key Analyzer   ║
╚════════════════════════════╝
Author: Jheff AT | Version: 1.0.0 Copyright (c) 2026 | Contact: jheff.at@gmail.com
```

# 🔓 ROX

**XOR Key Recovery Tool**

ROX is a Python command-line utility that recovers XOR encryption keys using known file signatures (magic headers).

---
## 🗄️ Signature Database

ROX uses a file named **`dict.bin`** that contains known file signatures (magic headers) used during the analysis process.

### 🔍 How It Works

* 📂 `dict.bin` stores potential file header signatures.
* 🔑 ROX compares these signatures against the encrypted file.
* 🧩 The tool attempts to derive XOR keys capable of producing valid headers.
* 🔄 Repeating patterns in the recovered data are analyzed to identify likely XOR keys.
* 📄 Matching headers can help determine the original file type even when the file extension is missing or unknown.

### 🎯 Purpose

This functionality is particularly useful when analyzing files that have been obfuscated using a **single-byte XOR cipher** and the original file format is unknown.

### 💡 Example Workflow

```text
Encrypted File
       │
       ▼
Compare Against Signatures
       │
       ▼
Generate XOR Key Candidates
       │
       ▼
Detect Repeating Patterns
       │
       ▼
Identify Likely Keys & File Types
```

---

## 📄 Supported Formats

* 🖼️ JPEG
* 🖼️ PNG
* 🎞️ GIF
* 📕 PDF
* 📦 ZIP
* ⚙️ EXE
* 🎵 MP3
* 🖼️ BMP
* 🔊 WAV
* + More...

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/rox.git
cd rox
```

---

## 💻 Usage

```bash
python rox.py secret.dat
```

Example:

```bash
python rox.py secret.dat
```

---

## 📊 Example Output

```text
 --------------------------------------------------------------------------------
 🔍Analyzing encrypted file secret.dat...
     ✅Candidate Key #1
         🔢HEX    : 23 47 30 64 65 69 75 6E 64 75 68 66 62 34 75 38 33 39 38 33 39 33 34 30 30 33 34 34 21 
         📦Base64 : b'I0cwZGVpdW5kdWhmYjR1ODM5ODM5MzQwMDM0NCE='
         🔤ASCII  : #G0deiunduhfb4u8398393400344! 
         📏Length : 29 Bytes
--------------------------------------------------------------------------------

[📄] Analysis complete.

```

---

## ⚠ Disclaimer

ROX is intended for:

* 🎓 Education
* 🔬 Research
* 🕵️ Digital Forensics
* 🛡️ Security Analysis

Use responsibly and only on data you are authorized to analyze.

---

## 👨‍💻 Author

**Jheff AT**

🐍 Python • 🐧 Linux • 🛡️ Cybersecurity • 🏗️ Infrastructure Engineering
