"""Check the published Firefox artifact against the recorded release and test evidence.

This does not independently verify Mozilla's trust chain; the disposable-Firefox
verification report records that separate test.
"""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.request
import zipfile
import io

parser=argparse.ArgumentParser();parser.add_argument('--download',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'FIREFOX_RELEASE_MANIFEST.json').read_text(encoding='utf-8'))
report=json.loads((root/'FIREFOX_SIGNATURE_VERIFICATION.json').read_text(encoding='utf-8'))
assert manifest['artifact']==f"KryptoCore-Vault-Firefox-{manifest['version']}.xpi"
assert manifest['tag']=='firefox-v'+manifest['version']
assert manifest['extension_id']==report['addon_id']=='vault@kryptocorelabs'
assert manifest['version']==report['version'] and manifest['sha256']==report['sha256']
assert manifest['mozilla_signed'] and report['signature_required'] and report['restart_persistence_verified']
assert report['payload_matches_submission'] and report['manifest_semantically_identical']
assert {item['case'] for item in report['negative_checks'] if item['rejected']}=={'unsigned','tampered'}
assert {item['phase'] for item in report['states']}=={'install','restart'}
for item in report['states']:
    addon=item['addon']
    assert item['signaturesRequired'] and addon['signedState']==item['signedConstant']
    assert addon['isActive'] and not addon['temporarilyInstalled'] and not addon['appDisabled']
assert (root/'FIREFOX_SHA256SUMS.txt').read_text(encoding='ascii').strip()==manifest['sha256']+'  '+manifest['artifact']
url='https://github.com/kryptocorelabs/vault/releases/download/'+manifest['tag']+'/'+manifest['artifact']
assert url in (root/'FIREFOX.md').read_text(encoding='utf-8')
if args.download:
    request=urllib.request.Request(url,headers={'User-Agent':'KryptoCore-Firefox-release-check'})
    with urllib.request.urlopen(request,timeout=60) as response:
        data=response.read(16*1024*1024+1)
    assert len(data)==manifest['bytes'] and len(data)<=16*1024*1024
    assert hashlib.sha256(data).hexdigest()==manifest['sha256']
    with zipfile.ZipFile(io.BytesIO(data)) as package:
        addon=json.loads(package.read('manifest.json'))
        assert addon['version']==manifest['version']
        assert addon['browser_specific_settings']['gecko']['id']==manifest['extension_id']
        assert not addon.get('host_permissions') and addon['optional_host_permissions']==['https://*/*']
        for name in ('META-INF/cose.sig','META-INF/mozilla.rsa','popup.css','vault_firefox_channel.wasm'):
            assert package.read(name)
    print('Published XPI size, hash, manifest and expected contents match the recorded artifact.')
print('Firefox release metadata, recorded verification evidence and checksum agree.')
