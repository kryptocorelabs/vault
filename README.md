# KryptoCore Vault

**An open-source password manager for people who want to keep their logins on their own device.**

After setup, save and open your logins offline in an encrypted `.kcv` file.
No account or cloud service is required.

**Windows x64 preview.** Try it with sample data. Setup requires Python 3.13 x64.

[Download the Windows preview](https://github.com/kryptocorelabs/vault/releases/tag/v0.1.0-preview.4) · [Browse the source](https://github.com/kryptocorelabs/vault-source) · [Give feedback](https://github.com/kryptocorelabs/vault/issues)

## Try the desktop preview

1. Download and extract the [Windows x64 desktop ZIP](https://github.com/kryptocorelabs/vault/releases/tag/v0.1.0-preview.4).
2. Install Python 3.13 x64, then run `Setup.cmd` once.
3. Open `Start-Vault.cmd`, create a test vault and save a fictional login.

[Usage and backups](USAGE.md) · [Security in 30 seconds](SECURITY-IN-BRIEF.md) · [Check a download](VERIFY-DOWNLOADS.md)

<img src="vault-desktop.png" alt="Vault desktop showing synthetic logins in a dark tile layout, with the selected password hidden" width="500">

*Development screenshot with synthetic logins.*

The maintainers test Vault locally and through CI. An independent security
audit is pending. Use the [security policy](SECURITY.md) to report suspected
vulnerabilities privately.

## Source and community

Vault uses the [KryptoCore encryption library](https://github.com/kryptocorelabs/kryptocore).
Vault and its Firefox companion are open source under MIT. Dependencies retain
their own licenses. Read the [project charter](https://github.com/kryptocorelabs/kryptocore/blob/main/PROJECT_CHARTER.md).

**Windows 0.1.0-preview.4** rotates the encryption seed when recovering a
KCV2–KCV4 vault. Earlier copies retain their original access. See the
[recovery version guide](RECOVERY-HARDENING.md) and [threat model](THREAT_MODEL.md).

The development source now includes [native Linux/macOS desktop builds](PLATFORMS.md)
with the same local vault format. Firefox pairing remains Windows-only. Native
CI artifacts are evaluation builds; existing download releases remain unchanged.

## Vault formats and backups

New vaults use KCV4. Keep an encrypted backup and check the
[format compatibility guide](MIGRATION.md) before moving a vault to a different build.

The [migration guide](MIGRATION.md) covers copying an encrypted legacy vault,
creating a new vault with fresh key material, and verifying backups.

Vault offers [password changes and SHA-256 fingerprints](ACCESS-AND-INTEGRITY.md).
Optional re-keying creates a new key and emergency sheet for the current file;
old copies retain their old access. A fingerprint is not a signature or malware scan.

## Release status

**Public preview:** 0.1.0-preview.4 for Windows x64. The ZIP has a publisher
signature and a GitHub build attestation. [Check the download](VERIFY-DOWNLOADS.md)

**Firefox add-on:** [Mozilla-signed 0.1.16](FIREFOX.md) is available for
persistent installation. Preview.4 requires a separate one-use desktop approval
before filling credentials. Windows Authenticode signing is pending.

## Offline recovery companion

[Rescue preview.4](https://github.com/kryptocorelabs/rescue/releases/tag/v0.1.0-preview.4)
authenticates KCV1–KCV4 files offline and exports records to a new plaintext
JSON file. It requires the matching Vault password or a configured recovery key
for KCV2–KCV4. It leaves the input intact.
Use a working copy, retain backups, and protect the unencrypted export.
See the [recovery guide](RESCUE-FIRST.md).
