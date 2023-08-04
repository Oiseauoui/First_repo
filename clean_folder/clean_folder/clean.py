import os

def clean_folder(folder_path):
    # Your previous code for parsing the folder goes here
    # ...

if __name__ == "__main__":
    # If you want to add a command-line interface for testing
    # when calling clean.py directly, you can do that here.
    # This part won't affect the console script behavior.
    import argparse

    parser = argparse.ArgumentParser(description="Clean folder script")
    parser.add_argument("folder_path", help="Path to the folder to clean")
    args = parser.parse_args()

    clean_folder(args.folder_path)
