# KryptoCore Vault

[Standalone Windows builds and requirements](PORTABLE.md)

[Unreleased design preview](DESIGN.md)

A local password manager for Windows. Vault stores logins in an encrypted
`.kcv` file on your device and uses the open-source
[KryptoCore library](https://github.com/kryptocorelabs/kryptocore).

[Desktop downloads](https://github.com/kryptocorelabs/vault/releases) · [Usage and recovery](USAGE.md) · [Firefox](FIREFOX.md)

<img src="vault-desktop.png" alt="Vault desktop showing synthetic logins in a dark tile layout, with the selected password hidden" width="500">

*Development build with synthetic logins. The screenshot shows a newer local
build than the linked download.*

## Standalone development build

The current local design build is `KryptoCore-Vault-Portable.exe`, containing
Python, Qt, the Rust backend and the Firefox native host. It starts without
running Setup.cmd. This is an unreleased local build; the older public preview
below still uses its documented Python setup. See [standalone build checks](PORTABLE.md)
and the [design preview](DESIGN.md) for scope and release limits.

## Try the desktop preview

1. Download and extract the Windows x64 desktop ZIP.
2. With Python 3.13 x64 installed, run `Setup.cmd` once.
3. Open `Start-Vault.cmd` and create a test vault.

Use synthetic data for this development preview. See the
[usage notes](USAGE.md) for how to make and test copies of a vault.

## Release status

**Public preview:** 0.1.0-preview.3 for Windows x64.

**Release candidate:** Vault 0.1.0-rc.2 and Firefox 0.1.15 passed local
tests for pairing, autofill, locking, and switching vaults. The Windows
candidate is awaiting signing. The public releases page has no signed XPI
for 0.1.15 yet.

This repository hosts Vault downloads and release notes. The application
source is maintained separately.
Use the [security policy](SECURITY.md) to report a suspected vulnerability
privately.

## Offline recovery companion

[Rescue](https://github.com/kryptocorelabs/rescue) is a separate offline preview
for authenticating KCV1/KCV2 files and exporting records to a new plaintext
JSON file. It requires the existing Vault password or a configured KCV2 recovery
key. It does not reset the original password or repair damaged ciphertext.
Use a working copy, retain backups, and protect the unencrypted export.
