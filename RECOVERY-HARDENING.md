# Vault recovery protection by version

| Public download | Recovery behavior |
| --- | --- |
| [Windows 0.1.0-preview.4](https://github.com/kryptocorelabs/vault/releases/tag/v0.1.0-preview.4) | Emergency reset rotates the seed for KCV2–KCV4 and retains the matching emergency sheet. |
| Windows previews through 0.1.0-preview.3 | Treat resets as legacy behavior without verified seed rotation. |
| Firefox 0.1.16 | Browser companion only. Recovery is a desktop operation. |

An earlier snapshot remains readable with its matching password or emergency
sheet. See the [canonical format and key lifecycle](https://github.com/kryptocorelabs/vault-source/blob/main/apps/vault/FORMAT-LIFECYCLE.md)
for migration and snapshot rules.

The [historical review](https://github.com/kryptocorelabs/vault-source/blob/main/apps/vault/RECOVERY-HARDENING.md)
documents the defect and regression tests.
