# Vault for Firefox

Vault 0.1.0-rc.2 and add-on 0.1.15 are the tested release-candidate pair
for Firefox 140 or later on Windows. The add-on fills sign-in fields on
request for the matching HTTPS origin. The website assistant is opt-in.

Mozilla signs the XPI used for persistent installation. The 0.1.15 submission
ZIP is used for signing and temporary testing. Check
[Vault releases](https://github.com/kryptocorelabs/vault/releases) for
published downloads.

## Pair the release candidate

1. Open and unlock your test vault in the Windows app.
2. Select **Firefox → Verbindungscode erstellen** in Vault.
3. Paste the one-time code in the add-on and select **Firefox verbinden**.
4. Open a matching HTTPS sign-in page and choose **Login ausfüllen**.
   Check the fields before submitting the form yourself.

Existing Firefox v5 pairings carry over when you update Vault or the add-on.
Locking Vault blocks new requests until you unlock it again.
