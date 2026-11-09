# Vault recovery protection by version

Public Windows Vault downloads through 0.1.0-preview.3 predate the verified release of recovery re-keying. Current [Vault source](https://github.com/kryptocorelabs/vault-source/blob/main/apps/vault/FORMAT-LIFECYCLE.md) rotates the seed during emergency reset for KCV2–KCV4. An earlier snapshot remains readable with its matching password or emergency sheet.

The [historical review](https://github.com/kryptocorelabs/vault-source/blob/main/apps/vault/RECOVERY-HARDENING.md) documents the defect and regression tests. The Firefox extension does not perform recovery.
