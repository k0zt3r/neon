"""Package the approved first nine atlas rows for Codex CLI 0.167.0."""
from pathlib import Path
from PIL import Image
import json

root = Path(__file__).parent
dest = root / 'cli' / 'neon'
dest.mkdir(parents=True, exist_ok=True)
with Image.open(root / 'final' / 'spritesheet-extended.png') as atlas:
    atlas.crop((0, 0, 1536, 1872)).save(dest / 'spritesheet.png')
manifest = {
    'id': 'neon',
    'displayName': 'Неон',
    'description': 'Чёрный киберкот в бирюзовой куртке. Девять анимаций для Codex CLI.',
    'spritesheetPath': 'spritesheet.png',
    'frame': {'width': 192, 'height': 208, 'columns': 8, 'rows': 9},
    'animations': {},
}
(dest / 'pet.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print('Packaged cli/neon/pet.json and spritesheet.png (1536x1872).')
