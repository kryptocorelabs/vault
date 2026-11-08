# Vault security

Vault is a development preview for synthetic test data. See the
[usage notes](USAGE.md) for encryption limits and recovery instructions.

Testing to date has been carried out by the KryptoCoreLabs maintainers, locally
and through automated CI. No independent security audit has been completed.
We welcome community testing, code reviews and scrutiny of our security
assumptions. Please use synthetic data and report suspected vulnerabilities
privately through the project's security-reporting channel.

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
