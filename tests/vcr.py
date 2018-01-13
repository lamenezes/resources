from pathlib import Path
from vcr import VCR


here = Path.cwd()

vcr = VCR(
    cassette_library_dir=str(here / 'resources/cassettes'),
    path_transformer=VCR.ensure_suffix('.yaml'),
    filter_headers=['authorization'],
    record_mode='once',
    match_on=['method', 'path', 'query'],
)
