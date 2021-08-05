# Checksum
A Python script designed to aid in verifying checksums of files.

# Arguments
* -f
File to verify.

* -a
Hashing algorithm to use. (Currently supports MD5, SHA1, SHA256, and SHA512).

* -c
Hash to verify selected file against.

* -e
Skips verification, and just displays the checksum of the chosen file.

# Examples

`python3 checksum.py -a sha256 -f checksum.py -c 185870b78ecc497ee97f2d4714682597c1e81cb77128a4f66eade59b3809c393`

**OUTPUT: Match!**

`python3 checksum.py -a sha256 -f checksum.py -c 347efe3c8b72b70b5a32a78b8fe7efe2bdd5df7a4a855cd4631546d9452f25b8`

**OUTPUT: [!] Not a match.**

`python3 checksum.py -a sha256 -f checksum.py -e`

**OUTPUT: Checksum: 185870b78ecc497ee97f2d4714682597c1e81cb77128a4f66eade59b3809c393**
