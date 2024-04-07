from pathlib import Path
from datetime import datetime, timezone

class FileSystemInfo:
    def __init__(self, path):
        self._path = Path(path).resolve()
        self.full_path = str(self._path)  # Represents the fully qualified path
        self.original_path = path  # The path originally specified by the user

    @property
    def attributes(self):
        # This method would be platform-specific; placeholder for now
        pass

    @property
    def creation_time(self):
        return datetime.fromtimestamp(self._path.stat().st_ctime)

    @property
    def creation_time_utc(self):
        return datetime.fromtimestamp(self._path.stat().st_ctime, tz=timezone.utc)

    @property
    def exists(self):
        return self._path.exists()

    @property
    def extension(self):
        return self._path.suffix

    @property
    def full_name(self):
        return self.full_path

    @property
    def last_access_time(self):
        return datetime.fromtimestamp(self._path.stat().st_atime)

    @property
    def last_access_time_utc(self):
        return datetime.fromtimestamp(self._path.stat().st_atime, tz=timezone.utc)

    @property
    def last_write_time(self):
        return datetime.fromtimestamp(self._path.stat().st_mtime)

    @property
    def last_write_time_utc(self):
        return datetime.fromtimestamp(self._path.stat().st_mtime, tz=timezone.utc)

    @property
    def link_target(self):
        return self._path.readlink() if self._path.is_symlink() else None

    @property
    def name(self):
        return self._path.name

    def delete(self):
        if self._path.is_file():
            self._path.unlink()
        elif self._path.is_dir():
            for child in self._path.iterdir():
                if child.is_file():
                    child.unlink()
                else:
                    FileSystemInfo(child).delete()
            self._path.rmdir()

    def refresh(self):
        # Refresh or reinitialize the path object to update its state
        self.__init__(self.original_path)
