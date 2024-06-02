# Backup Pruner

## Description

The Backup Pruner (more like a "Selector") script helps manage backup files in a specified directory by retaining only backups that are older than three months and deleting others. Additionally, it keeps one backup per week for files older than three months. The script is flexible and allows specifying the file extensions of the backup files to be managed.

## Usage

To use the script, you'll need to provide the directory containing the backup files and the list of file extensions to consider as command-line arguments.

### Example

```sh
python backup_selector.py /path/to/backups .tar.gz .zip .sql
```
