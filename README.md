# KryptoCore Vault

A local password manager for Windows. Vault stores logins in an encrypted
`.kcv` file on your device and uses the open-source
[KryptoCore library](https://github.com/kryptocorelabs/kryptocore).

[Download the desktop preview](https://github.com/kryptocorelabs/vault/releases/tag/v0.1.0-preview.3) · [All releases](https://github.com/kryptocorelabs/vault/releases) · [Usage and recovery](USAGE.md)

<img src="vault-desktop.png" alt="Vault desktop showing synthetic logins in a dark tile layout, with the selected password hidden" width="500">

*Development build with synthetic logins. The screenshot shows a newer local
build than the linked download.*

## Try the desktop preview

1. Download and extract the Windows x64 desktop ZIP.
2. With Python 3.13 x64 installed, run `Setup.cmd` once.
3. Open `Start-Vault.cmd` and create a test vault.

Use synthetic data for this development preview. See the
[usage notes](USAGE.md) for how to make and test copies of a vault.

## Project status

This repository hosts Vault downloads and release notes. The application
source is maintained separately. Firefox integration is in development.
Use the [security policy](SECURITY.md) to report a suspected vulnerability
privately.
