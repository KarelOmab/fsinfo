from pathlib import Path
from filesysteminfo import FileSystemInfo
from fileinfo import FileInfo
import shutil
import os

class DirectoryInfo(FileSystemInfo):
    def __init__(self, path):
        super().__init__(path)
        self._path = Path(path).resolve()

    @property
    def exists(self):
        return self._path.exists()
    
    @property
    def length(self):
        total_size = 0
        for root, dirs, files in os.walk(self._path):
            for name in files:
                filepath = os.path.join(root, name)
                # Skip if it is a symbolic link
                if not os.path.islink(filepath):
                    total_size += os.path.getsize(filepath)
        return total_size

    def create(self):
        try:
            self._path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise Exception(e)

    def delete(self, recursive=False):
        try:
            if recursive:
                shutil.rmtree(self._path)
            else:
                self._path.rmdir()  # Only removes the directory if empty
        except Exception as e:
            raise Exception(e)

    def get_files(self, pattern='*'):
        try:
            return [FileInfo(child) for child in self._path.glob(pattern) if child.is_file()]
        except Exception as e:
            raise Exception(e)

    def get_directories(self, pattern='*'):
        try:
            return [DirectoryInfo(child) for child in self._path.glob(pattern) if child.is_dir()]
        except Exception as e:
            raise Exception(e)

    def move_to(self, dest):
        try:
            destination = Path(dest).resolve()
            shutil.move(self._path, destination)
            self._path = destination
        except Exception as e:
            raise Exception(e)


