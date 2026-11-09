# KryptoCore Vault

**An open-source password manager for people who want to keep their logins on their own device.**

After setup, save and open your logins offline in an encrypted `.kcv` file.
No account or cloud service is required.

**Windows x64 preview.** Try it with sample data. Setup requires Python 3.13 x64.

[Download the Windows preview](https://github.com/kryptocorelabs/vault/releases/tag/v0.1.0-preview.3) · [Browse the source](https://github.com/kryptocorelabs/vault-source) · [Give feedback](https://github.com/kryptocorelabs/vault/issues)

## Try the desktop preview

1. Download and extract the [Windows x64 desktop ZIP](https://github.com/kryptocorelabs/vault/releases/tag/v0.1.0-preview.3).
2. Install Python 3.13 x64 with the Windows Python Launcher, then run `Setup.cmd` once.
3. Open `Start-Vault.cmd`, create a test vault and save a fictional login.

[Usage and backups](USAGE.md) · [Security in 30 seconds](SECURITY-IN-BRIEF.md) · [Check a download](VERIFY-DOWNLOADS.md)

<img src="vault-desktop.png" alt="Vault desktop showing synthetic logins in a dark tile layout, with the selected password hidden" width="500">

*Development build with synthetic logins. The screenshot shows a newer local
build than the linked download.*

The maintainers test Vault locally and through CI. An independent security
audit is pending. Use the [security policy](SECURITY.md) to report suspected
vulnerabilities privately.

## Source and community

Vault uses the [KryptoCore encryption library](https://github.com/kryptocorelabs/kryptocore).
Vault and its Firefox companion are open source under MIT. Dependencies retain
their own licenses. Read the [project charter](https://github.com/kryptocorelabs/kryptocore/blob/main/PROJECT_CHARTER.md).

The unreleased [recovery hardening](RECOVERY-HARDENING.md) rotates the internal
data key when resetting a password. It does not revoke old vault copies. Existing
download assets have not been replaced; use the documented source/build identity
to establish whether a build includes this fix. See the [threat model](THREAT_MODEL.md).

The development source now includes [native Linux/macOS desktop builds](PLATFORMS.md)
with the same local vault format. Firefox pairing remains Windows-only. Native
CI artifacts are evaluation builds; existing download releases remain unchanged.

## Standalone development build

The [optional KCV3 epoch profile](EPOCHS.md) is an unreleased copy-based opt-in.
Use a KCV3-capable Rescue build for its files; published preview.3 is insufficient.

[JSON migration and Vault status](MIGRATION.md) are also available in development
source: deliberate export, new-vault creation with fresh key material, entry and
recovery facts, and local backup/file-age hints. Existing release assets are unchanged.

Development builds also offer [password changes and SHA-256 fingerprints](ACCESS-AND-INTEGRITY.md).
Optional re-keying creates a new key and emergency sheet for the current file;
old copies retain their old access. A fingerprint is not a signature or malware scan.

The current local design build is `KryptoCore-Vault-Portable.exe`, containing
Python, Qt, the Rust backend and the Firefox native host. It starts without
running Setup.cmd. This is an unreleased local build; the older public preview
below still uses its documented Python setup. See [standalone build checks](PORTABLE.md)
and the [design preview](DESIGN.md) for scope and release limits.

## Release status

**Public preview:** 0.1.0-preview.3 for Windows x64.

**Firefox add-on:** [Mozilla-signed 0.1.16](FIREFOX.md) is available for
persistent installation; signature enforcement and restart persistence passed
in Firefox 159.0.1. Windows Authenticode signing is still pending. Full current
desktop/browser workflow testing is a separate release check.

## Offline recovery companion

[Rescue](https://github.com/kryptocorelabs/rescue) is a separate offline preview
for authenticating KCV1/KCV2 files and exporting records to a new plaintext
JSON file. It requires the existing Vault password or a configured KCV2 recovery
key. It does not reset the original password or repair damaged ciphertext.
Use a working copy, retain backups, and protect the unencrypted export.
See the [recovery guide](RESCUE-FIRST.md).
