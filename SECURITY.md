# Vault security

Vault is a development preview for synthetic test data. See the
[usage notes](USAGE.md) for encryption limits and recovery instructions.

Testing to date has been carried out by the KryptoCoreLabs maintainers, locally
and through automated CI. No independent security audit has been completed.
We welcome community testing, code reviews and scrutiny of our security
assumptions. Please use synthetic data and report suspected vulnerabilities
privately through the project's security-reporting channel.

## Password reset, snapshots and memory

Resetting a password does not revoke old vault copies. Anyone with an old file
and its matching password or emergency sheet can still read that snapshot.
If credentials were exposed, change them at the corresponding services too.

The unreleased recovery hardening rotates the random 32-byte payload seed,
rewraps it in both slots and re-encrypts the authenticated payload. The existing
emergency sheet remains valid. A seed recovered from a pre-reset copy cannot
decrypt the updated file or its later edits. Earlier builds only rewrote the
password slot and retained the seed; their resets did not provide that boundary.
Use the hardening change described in [the review](RECOVERY-HARDENING.md);
the version label alone does not establish that a build includes it.

Ordinary saves retain the seed. A copy and its matching credentials therefore
remain sensitive even after editing the active vault. The current emergency
sheet can also unlock later files until it is renewed. If it may be exposed,
renew it from the unlocked vault and protect the replacement separately.

An older, authentic file can replace a newer one and still open successfully.
There is no trusted monotonic counter or external freshness record. AEAD detects
modification, not rollback of an entire valid file. Dated, separately stored
backups and checking expected entries help recovery but do not prevent rollback.

Rust uses zeroizing owners for session passwords, seeds, derived keys, decrypted
buffers and login fields where implemented. Python strings, JSON serialization
and Qt widgets can create additional managed copies. Clearing a field or locking
Vault does not guarantee erasure of all copies, swap or crash dumps. Do not rely
on memory secrecy against a compromised process, user account or operating system.
See the [Vault threat model](THREAT_MODEL.md) for trust boundaries.

## Report a vulnerability

Use **Security → Report a vulnerability** on the
[Vault repository](https://github.com/kryptocorelabs/vault/security)
when GitHub private reporting is available. If the option is unavailable,
open an issue asking the maintainers for a private contact. Keep technical
details for the private conversation.

Include the Vault and add-on versions, operating system, browser version
if relevant, possible impact, and steps to reproduce with synthetic data.
Leave real vault files, passwords, and emergency sheets out of the report.
For an ordinary support request about an opening error, share the error
message and versions and remove any private details.

## How reports are handled

Maintainers aim to acknowledge reports privately, reproduce issues, and
assess affected versions. We coordinate disclosure with the reporter and
document affected versions, fixes, and available mitigations when a public
advisory is appropriate.
