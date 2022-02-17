from os import PathLike
from pathlib import Path
from typing import Union
from zipfile import ZIP_DEFLATED
from zipfile import ZipFile


def zip_dir(zip_name: str, source_dir: Union[str, PathLike]):
    src_path = Path(source_dir).expanduser().resolve(strict=True)
    with ZipFile(zip_name, "w", ZIP_DEFLATED) as zf:
        for file in src_path.rglob("*"):
            zf.write(file, file.relative_to(src_path))
