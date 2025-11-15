# NextBuild Keywords Watcher

A file monitoring utility that automatically syncs `keywords.json` changes to your NextBuild Studio installation.

## Overview

The Keywords Watcher monitors your local `keywords.json` file for changes and automatically copies updated versions to your NextBuild Studio extension directory. This ensures your development changes are immediately available in the NextBuild Studio IDE.

## Features

- **Automatic Sync**: Detects file changes and syncs immediately
- **Backup Creation**: Creates backup of target file before overwriting
- **Configurable Paths**: Customizable source and target paths
- **Status Feedback**: Clear console output showing sync operations
- **Cross-Platform**: Works on Linux, Windows, and macOS
- **Error Handling**: Graceful handling of file access issues

## Quick Start

### Using the Launcher Script (Recommended)

```bash
cd /path/to/nextbuild-viewers-linux/scripts
./run_keywords_watcher.sh
```

This will:
- Monitor `../data/keywords.json`
- Sync to `/home/usb/Applications/NextBuildStudio/app/resources/app/extensions/em00k.nextbuild-viewers/data/keywords.json`
- Check for changes every 2 seconds

### Manual Usage

```bash
cd /path/to/nextbuild-viewers-linux/scripts
python3 keywords_watcher.py --source ../data/keywords.json --target /path/to/target/keywords.json
```

## Command Line Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--source` | `-s` | `../data/keywords.json` | Source keywords.json file to monitor |
| `--target` | `-t` | NextBuild Studio path | Target keywords.json file location |
| `--interval` | `-i` | `2.0` | Check interval in seconds |

## Examples

### Basic Usage
```bash
# Use default paths
./run_keywords_watcher.sh
```

### Custom Paths
```bash
# Monitor specific source file
python3 keywords_watcher.py --source /my/project/keywords.json --target /my/studio/extensions/data/keywords.json
```

### Faster Checking
```bash
# Check every 0.5 seconds for faster response
python3 keywords_watcher.py --interval 0.5
```

### Windows Usage
```bash
# Use Windows paths
python3 keywords_watcher.py --target "C:\Users\username\AppData\Local\Programs\NextBuildStudio\resources\app\extensions\em00k.nextbuild-viewers\data\keywords.json"
```

## How It Works

1. **Initial Sync**: Performs initial sync if target file doesn't exist or is older
2. **File Monitoring**: Checks source file modification time every 2 seconds
3. **Change Detection**: Compares modification times to detect changes
4. **Safe Copy**: Creates backup of target before overwriting
5. **Status Reporting**: Shows timestamp and sync status in console

## Output Examples

```
Keywords Watcher initialized:
  Source: /home/user/nextbuild/data/keywords.json
  Target: /home/user/NextBuildStudio/extensions/data/keywords.json
  Check interval: 2.0 seconds
--------------------------------------------------
Target file doesn't exist - performing initial sync...
[14:23:15] ✓ Synced keywords.json
    Source: /home/user/nextbuild/data/keywords.json
    Target: /home/user/NextBuildStudio/extensions/data/keywords.json
[14:25:42] ✓ Synced keywords.json
[14:28:17] ✓ Synced keywords.json
```

## Integration with Keywords Editor

The watcher works perfectly with the Keywords Editor:

1. **Edit keywords** using the GUI editor
2. **Save changes** - watcher detects the file modification
3. **Automatic sync** to NextBuild Studio
4. **Test immediately** in the IDE

### Workflow Example

```bash
# Terminal 1: Start the watcher
./run_keywords_watcher.sh

# Terminal 2: Edit keywords
./run_keywords_editor.sh

# Make changes in editor, save, and see them sync automatically
```

## Configuration

### Default Paths

The launcher script uses these defaults:
- **Source**: `../data/keywords.json` (relative to scripts directory)
- **Target**: `/home/usb/Applications/NextBuildStudio/app/resources/app/extensions/em00k.nextbuild-viewers/data/keywords.json`

### Custom Installation Paths

If NextBuild Studio is installed in a different location:

```bash
# Find your NextBuild Studio installation
find /home -name "em00k.nextbuild-viewers" 2>/dev/null

# Use custom target path
python3 keywords_watcher.py --target "/path/to/your/studio/extensions/em00k.nextbuild-viewers/data/keywords.json"
```

## Troubleshooting

### Common Issues

1. **Permission Denied**
   ```
   Error syncing file: [Errno 13] Permission denied
   ```
   **Solution**: Ensure write permissions on target directory or run with appropriate permissions.

2. **Source File Not Found**
   ```
   Error: Source file not found
   ```
   **Solution**: Check the source path or run from the correct directory.

3. **Target Directory Not Found**
   ```
   Error syncing file: [Errno 2] No such file or directory
   ```
   **Solution**: Create target directory or check the target path.

### Performance Considerations

- **Check Interval**: Default 2 seconds balances responsiveness with system load
- **Large Files**: Works efficiently with the ~2.5MB keywords.json file
- **Network Drives**: May have slower response times on network-mounted drives

### Stopping the Watcher

Press `Ctrl+C` to stop the watcher gracefully:

```
^C
Keywords Watcher stopped by user
```

## Technical Details

### Dependencies
- Python 3.6+
- Standard library modules: `os`, `time`, `shutil`, `argparse`, `pathlib`

### File Monitoring Method
Uses file modification time comparison rather than file watching libraries for maximum compatibility across platforms.

### Backup Strategy
- Creates `.backup` file before overwriting target
- Preserves file permissions and metadata using `shutil.copy2()`

## Advanced Usage

### Integration with Build Scripts

Add to your development workflow:

```bash
#!/bin/bash
# build_and_watch.sh

# Build your project
npm run build

# Start keywords watcher in background
./scripts/run_keywords_watcher.sh &

# Save PID for cleanup
echo $! > .watcher_pid

# Your development workflow here
# ...

# Cleanup
kill $(cat .watcher_pid)
rm .watcher_pid
```

### Multiple Targets

Monitor and sync to multiple locations:

```bash
#!/bin/bash
# watch_multiple.sh

# Start multiple watchers
python3 keywords_watcher.py --target "/path/to/studio1/keywords.json" &
PID1=$!

python3 keywords_watcher.py --target "/path/to/studio2/keywords.json" &
PID2=$!

# Wait for Ctrl+C
trap "kill $PID1 $PID2; exit" INT
wait
```

## Support

For issues or questions:
1. Check file paths and permissions
2. Verify NextBuild Studio installation location
3. Test with manual copy first: `cp data/keywords.json /path/to/target/`
4. Review console output for specific error messages

## License

Part of the NextBuild project. See main project LICENSE for details.







