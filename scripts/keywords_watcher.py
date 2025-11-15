#!/usr/bin/env python3
"""
NextBuild Keywords Watcher
Monitors keywords.json for changes and syncs to target directory
"""

import os
import time
import shutil
import argparse
from pathlib import Path
from datetime import datetime

class KeywordsWatcher:
    def __init__(self, source_file, target_file, interval=2.0):
        self.source_file = Path(source_file).resolve()
        self.target_file = Path(target_file).resolve()
        self.interval = interval
        self.last_modified = 0
        self.running = False

        # Ensure target directory exists
        self.target_file.parent.mkdir(parents=True, exist_ok=True)

        print(f"Keywords Watcher initialized:")
        print(f"  Source: {self.source_file}")
        print(f"  Target: {self.target_file}")
        print(f"  Check interval: {self.interval} seconds")
        print("-" * 50)

    def get_file_modified_time(self, file_path):
        """Get file modification time"""
        try:
            return file_path.stat().st_mtime
        except OSError:
            return 0

    def copy_file(self):
        """Copy source file to target location"""
        try:
            # Create backup of target if it exists
            if self.target_file.exists():
                backup_file = self.target_file.with_suffix('.backup')
                shutil.copy2(self.target_file, backup_file)

            # Copy the file
            shutil.copy2(self.source_file, self.target_file)

            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] ✓ Synced keywords.json")
            print(f"    Source: {self.source_file}")
            print(f"    Target: {self.target_file}")

            return True
        except Exception as e:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] ✗ Error syncing file: {e}")
            return False

    def check_for_changes(self):
        """Check if source file has been modified"""
        if not self.source_file.exists():
            if self.running:
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"[{timestamp}] ⚠ Source file not found: {self.source_file}")
            return False

        current_modified = self.get_file_modified_time(self.source_file)

        if current_modified > self.last_modified:
            self.last_modified = current_modified
            return True

        return False

    def initial_sync(self):
        """Perform initial sync if target doesn't exist or is older"""
        if not self.target_file.exists():
            print("Target file doesn't exist - performing initial sync...")
            return self.copy_file()

        source_time = self.get_file_modified_time(self.source_file)
        target_time = self.get_file_modified_time(self.target_file)

        if source_time > target_time:
            print("Target file is older than source - performing initial sync...")
            return self.copy_file()

        print("Files are in sync ✓")
        return True

    def start(self):
        """Start the watcher"""
        print("Starting Keywords Watcher...")
        print("Press Ctrl+C to stop")
        print()

        # Get initial modification time
        self.last_modified = self.get_file_modified_time(self.source_file)

        # Perform initial sync
        self.initial_sync()

        self.running = True
        try:
            while self.running:
                if self.check_for_changes():
                    self.copy_file()

                time.sleep(self.interval)

        except KeyboardInterrupt:
            print()
            print("Keywords Watcher stopped by user")
        except Exception as e:
            print(f"Error in watcher: {e}")
        finally:
            self.running = False

    def stop(self):
        """Stop the watcher"""
        self.running = False

def main():
    parser = argparse.ArgumentParser(description="Monitor keywords.json and sync to target directory")
    parser.add_argument("--source", "-s", default="../data/keywords.json",
                       help="Source keywords.json file (default: ../data/keywords.json)")
    parser.add_argument("--target", "-t",
                       default="/home/usb/Applications/NextBuildStudio/app/resources/app/extensions/em00k.nextbuild-viewers/data/keywords.json",
                       help="Target keywords.json file")
    parser.add_argument("--interval", "-i", type=float, default=2.0,
                       help="Check interval in seconds (default: 2.0)")

    args = parser.parse_args()

    # Convert to absolute paths
    source_file = Path(args.source).resolve()
    target_file = Path(args.target).resolve()

    # Validate source file exists
    if not source_file.exists():
        print(f"Error: Source file does not exist: {source_file}")
        return 1

    # Create watcher and start
    watcher = KeywordsWatcher(source_file, target_file, args.interval)
    watcher.start()

    return 0

if __name__ == "__main__":
    exit(main())







