# fsinfo

**fsinfo** is a Python library providing a high-level abstraction for working with filesystem paths, files, and directories in a cross-platform way. It simplifies file system operations like querying file attributes, manipulating directories, and handling files across Linux, macOS, and Windows.

## Features

### FileSystemInfo
This base class offers common attributes and methods for dealing with filesystem entities.

- **creation_time**: Get the time of creation of the file/directory.
- **exists**: Check if the file/directory exists.
- **full_name**: Get the fully qualified name of the file/directory.
- **last_access_time**: Get the last access time of the file/directory.
- **last_write_time**: Get the last modification time of the file/directory.
- **name**: Get the name of the file/directory.
- **delete**: Delete the file/directory.

### FileInfo
The `FileInfo` class extends `FileSystemInfo` with file-specific functionality.

- **directory**: Get the parent directory of the file.
- **directory_name**: Get the full path of the file's parent directory.
- **length**: Get the size of the file in bytes.
- **is_read_only**: Check if the file is read-only.
- **extension**: Get the file extension.
- **create_text**: Open the file for writing text.
- **open_text**: Open the file for reading text.
- **copy_to**: Copy the file to a specified destination.
- **move_to**: Move the file to a specified destination.

### DirectoryInfo
The `DirectoryInfo` class extends `FileSystemInfo` with directory-specific functionality.

- **length**: Get the total size of all the files within the directory.
- **create**: Create the directory.
- **get_files**: Get a list of all the files in the directory matching a specified pattern.
- **get_directories**: Get a list of all the subdirectories in the directory matching a specified pattern.
- **move_to**: Move the directory to a specified destination.

## Installation

Install `fsinfo` using pip:

```
pip install fsinfo
```

## Usage

### Working with Files

```
from YourPackageName.fileinfo import FileInfo 

file = FileInfo('/path/to/your/file.txt')
print(file.creation_time)
file.copy_to('/path/to/destination/file.txt', overwrite=True)
```

### Working with Directories

```
from YourPackageName.directoryinfo import DirectoryInfo 

directory = DirectoryInfo('/path/to/your/directory')
print(directory.length)  # Total size of files in the directory

for  file_info  in  directory.get_files():
  print(file_info.name)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.