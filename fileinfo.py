from filesysteminfo import FileSystemInfo
from pathlib import Path
import shutil

class FileInfo(FileSystemInfo):
    def __init__(self, path):
        super().__init__(path)
        self._path = Path(path).resolve()

    @property
    def directory(self):
        return self._path.parent

    @property
    def directory_name(self):
        return str(self.directory)

    @property
    def length(self):
        return self._path.stat().st_size if self.exists else None

    @property
    def is_read_only(self):
        return (self._path.stat().st_mode & 0o222) == 0

    @is_read_only.setter
    def is_read_only(self, value):
        mode = self._path.stat().st_mode
        if value:
            self._path.chmod(mode & ~0o222)
        else:
            self._path.chmod(mode | 0o222)

    def create_text(self):
        try:
            return self._path.open(mode='w+', encoding='utf-8')
        except Exception as e:
            raise Exception(e)

    def open_text(self):
        try:
            return self._path.open(mode='r', encoding='utf-8')
        except Exception as e:
            raise Exception(e)

    def copy_to(self, dest, overwrite=False):
        try:
            destination = Path(dest).resolve()
            if destination.exists() and not overwrite:
                raise FileExistsError(f"File {dest} already exists and overwrite is False.")
            shutil.copy2(self._path, destination)
            return FileInfo(destination)
        except Exception as e:
            raise Exception(e)

    def move_to(self, dest):
        try:
            destination = Path(dest).resolve()
            shutil.move(self._path, destination)
            self._path = destination
        except Exception as e:
            raise Exception(e)

    def delete(self):
        try:
            self._path.unlink()
        except Exception as e:
            raise Exception(e)

