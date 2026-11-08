# Vault for Firefox

**[Download Mozilla-signed Firefox add-on 0.1.16](https://github.com/kryptocorelabs/vault/releases/download/firefox-v0.1.16/KryptoCore-Vault-Firefox-0.1.16.xpi)**

Requires Firefox 140+ and the Windows Vault app with v5 browser pairing.
The add-on fills sign-in fields on request for the matching HTTPS origin.
Website assistance is opt-in. Chrome and Edge are not supported yet.

## Install once

1. Download `KryptoCore-Vault-Firefox-0.1.16.xpi` from the link above.
2. Remove any temporary development copy of this add-on.
3. In Firefox open `about:addons`, select the gear menu and choose
   **Install Add-on From File**. Select the downloaded XPI and confirm.
4. The installed extension stays available after Firefox restarts.

Use the signed XPI for normal installation. The unsigned ZIP and source ZIP
are developer/Mozilla submission artifacts. Do not change the signed XPI.
Future self-distributed versions currently need a manual signed-XPI update;
this release does not configure automatic updates.

## Connect to Vault

1. Open and unlock a test vault in the Windows app.
2. Select **Firefox → Verbindungscode erstellen** in Vault.
3. Paste the one-time code in the add-on and select **Verbinden**.
4. Open a matching HTTPS sign-in page and choose **Login ausfüllen**.
   Check the fields before submitting the form yourself.

Pairing is performed once. Existing compatible v5 pairings carry over when
you update the add-on. Locking Vault blocks new requests until it is unlocked.
Keep only one Vault instance open so it can own the local browser channel.

## Verified release scope

Firefox 159.0.1 accepted this XPI with signature enforcement enabled. The
extension was active, non-temporary and still active after restarting the same
disposable profile. Firefox rejected the unsigned submission ZIP and a tampered
copy. The application files match the submission; the manifest has identical
JSON content despite formatting changes. Signature metadata was added by Mozilla.

See [release manifest](FIREFOX_RELEASE_MANIFEST.json),
[verification report](FIREFOX_SIGNATURE_VERIFICATION.json) and
[checksum](FIREFOX_SHA256SUMS.txt). Mozilla signing does not replace an independent
security audit. Full pairing/autofill/locking tests of the exact current desktop
and signed add-on combination have not been rerun. The historical Vault RC.2 /
Firefox 0.1.15 pair has its separately documented test results. Windows desktop
code signing remains separate and pending.
