#!/usr/bin/env python3
import os
import shutil
import sys
import argparse
from datetime import datetime

def copy_files(source, destination):
    """
    Copy files from source to destination.
    
    Args:
        source (str): Source file path
        destination (str): Destination directory path
    """
    try:
        # Check if source exists
        if not os.path.exists(source):
            raise FileNotFoundError(f"Source path '{source}' does not exist")
            
        # Check if destination exists, create if not
        if not os.path.exists(destination):
            os.makedirs(destination, exist_ok=True)
        
        # Handle file copy
        if os.path.isfile(source):
            if os.path.isdir(destination):
                destination = os.path.join(destination, os.path.basename(source))
            shutil.copy2(source, destination)
            print(f"Successfully copied {source} to {destination}")
        
        # Handle directory copy (non-recursive)
        elif os.path.isdir(source):
            print(f"Skipping directory {source} (this script only copies individual files)")
    
    except Exception as e:
        print(f"Error copying {source} to {destination}: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Basic file copying tool for Red Hat Linux",
        epilog="Example: ./file_copy.py /home/user/file.txt /backup/"
    )
    
    parser.add_argument("source", help="Source file path")
    parser.add_argument("destination", help="Destination directory path")
    
    args = parser.parse_args()
    
    # Perform the copy operation
    copy_files(args.source, args.destination)

if __name__ == "__main__":
    main()