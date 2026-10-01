from pathlib import Path
import json, hashlib, zipfile
base=Path(__file__).resolve().parent
manifest=json.loads((base/'site-parts.json').read_text())
archive=base/'site.zip'
with archive.open('wb') as out:
    for item in manifest['parts']:
        data=(base/item['file']).read_bytes()
        assert len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256'],item['file']
        out.write(data)
assert hashlib.sha256(archive.read_bytes()).hexdigest()==manifest['zip_sha256']
dest=base/'public';dest.mkdir(exist_ok=True)
with zipfile.ZipFile(archive) as z:
    assert all((dest/n).resolve().is_relative_to(dest.resolve()) for n in z.namelist())
    z.extractall(dest)
assert (dest/'index.html').is_file()
print('Verified and unpacked complete learning website.')
