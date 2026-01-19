# Universal Multi-Format File Hasher

This utility is a high-performance Python tool designed to generate cryptographic fingerprints for any file. By leveraging the local system's OpenSSL library, it calculates every available hash format, providing a comprehensive overview of a file's data integrity.

The application is built to be cross-platform, utilizing a native file selection interface that integrates seamlessly with Windows, macOS, Linux, and Android environments.

---

## Core Features

* Native Interface Integration: The tool uses the system's built-in file explorer to allow for intuitive file selection.
* Extensive Algorithm Support: It dynamically identifies and applies all hashing methods supported by your specific operating system, including SHA-256, SHA-512, MD5, and BLAKE2.
* Memory Management: By implementing a buffered chunk-reading approach, the tool can process files of any size—even those exceeding several gigabytes—without consuming significant system memory.
* Automated Filtering: The logic automatically bypasses variable-length algorithms that require specific length parameters, ensuring the process completes without interruption.

---

## Technical Specifications

The script is designed for reliability and transparency. Below is a breakdown of how the internal components handle your data:

| Component | Purpose |
| :--- | :--- |
| hashlib.algorithms_available | Queries the OS for all supported cryptographic methods. |
| Binary Mode ('rb') | Processes the raw bitstream to ensure accuracy across all file types. |
| Chunked Processing | Reads data in 4KB segments to maintain a low hardware footprint. |
| Error Handling | Gracefully manages deprecated or restricted algorithms. |

---

## Requirements and Setup

### For the Python Script
If you prefer running the source code, you will need:
* Python 3.6 or higher.
* Tkinter (Usually included with Python. Linux users may need to install 'python3-tk').
* Android users can run the script via the Pydroid 3 application.

### For the Executable
No Python installation is required if you are using the standalone release.

---

## Usage Instructions

1. Launch the application (either the script or the executable).
2. A file selection window will appear. Navigate to and select the file you wish to hash.
3. The results will be displayed in the terminal window, listing the algorithm name followed by the generated hex digest.

---

## Releases

For users who do not wish to install a Python environment, a standalone executable (.exe) is available in the project's distribution folder. 

* Windows: Locate 'UniversalHasher.exe' in the Releases section.
* Note: As this is a standalone tool, some security software may flag it as unrecognized. This is a common occurrence with self-contained Python applications and can be resolved by allowing the file to run through your security prompt.

---

## Safety and Security

While this tool provides legacy formats such as MD5 and SHA-1 for backwards compatibility, these formats are no longer recommended for verifying security-sensitive data. For modern security standards, please prioritize the SHA-2 or SHA-3 families.

---

## License
This project is released under an open-source license. You are encouraged to modify and distribute it as needed for your own workflows.
