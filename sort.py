import os
import sys
import shutil
import zipfile


# Define the file extensions for each category
image_extensions = ('JPEG', 'PNG', 'JPG', 'TIFF')
video_extensions = ('AVI', 'MP4', 'MOV', 'MKV')
document_extensions = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
music_extensions = ('MP3', 'OGG', 'WAV', 'AMR', 'M4A')
archive_extensions = ('ZIP', 'GZ', 'TAR', 'RAR')
grafic_extensions = ('AI', 'PSD', 'MAX')
internet_extensions = ('SVG', 'HTM')

# List to keep track of file extensions found in the target folder
known_extensions = set()

# List to keep track of unknown file extensions found in the target folder
unknown_extensions = set()

from unidecode import unidecode

def normalize(s):
    # Transliterate Cyrillic characters into Latin using unidecode
    normalized = unidecode(s)

    # Replace all characters except Latin letters and numbers with '_'
    normalized = ''.join(c if c.isalnum() and c.isascii() else '_' for c in normalized)

    return normalized

def process_image(file_path):
    destination = os.path.join(os.path.dirname(file_path), 'images', os.path.basename(file_path))
    
    if not os.path.exists(os.path.dirname(destination)):
        os.makedirs(os.path.dirname(destination))
    
    try:
        shutil.move(file_path, destination)
    except Exception as e:
        print(f"An error occurred while moving: {e}")


def process_grafic(file_path):
    destination = os.path.join(os.path.dirname(file_path), 'grafic', os.path.basename(file_path))
    
    if not os.path.exists(os.path.dirname(destination)):
        os.makedirs(os.path.dirname(destination))
    
    try:
        shutil.move(file_path, destination)
    except Exception as e:
        print(f"An error occurred while moving: {e}")


def process_internet(file_path):
    destination = os.path.join(os.path.dirname(file_path), 'internet', os.path.basename(file_path))
    
    if not os.path.exists(os.path.dirname(destination)):
        os.makedirs(os.path.dirname(destination))
    
    try:
        shutil.move(file_path, destination)
    except Exception as e:
        print(f"An error occurred while moving: {e}")


def process_video(file_path):
    destination = os.path.join(os.path.dirname(file_path), 'videos', os.path.basename(file_path))
    
    if not os.path.exists(os.path.dirname(destination)):
        os.makedirs(os.path.dirname(destination))
    
    try:
        shutil.move(file_path, destination)
    except Exception as e:
        print(f"An error occurred while moving: {e}")



def process_document(file_path):
    destination = os.path.join(os.path.dirname(file_path), 'documents', os.path.basename(file_path))
    
    if not os.path.exists(os.path.dirname(destination)):
        os.makedirs(os.path.dirname(destination))
    
    try:
        shutil.move(file_path, destination)
    except Exception as e:
        print(f"An error occurred while moving: {e}")




def process_music(file_path):
    destination = os.path.join(os.path.dirname(file_path), 'music', os.path.basename(file_path))
    
    if not os.path.exists(os.path.dirname(destination)):
        os.makedirs(os.path.dirname(destination))
    
    try:
        shutil.move(file_path, destination)
    except Exception as e:
        print(f"An error occurred while moving: {e}")


def process_archive(file_path, password=None):
    destination_folder = os.path.join(os.path.dirname(file_path), 'archives')

    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Extract the archive's name without extension
            archive_name = os.path.splitext(os.path.basename(file_path))[0]

            # Create a subfolder with the same name as the archive (without extension)
            subfolder_path = os.path.join(destination_folder, archive_name)
            os.makedirs(subfolder_path, exist_ok=True)

            for zip_info in zip_ref.infolist():
                # Check if the file is encrypted and a password is provided
                if password and zip_info.flag_bits & 0x01:
                    # If the file is encrypted but no password is provided, skip extraction
                    continue

                # Extract each file into the subfolder
                zip_ref.extract(zip_info, subfolder_path, pwd=password)
    except zipfile.BadZipFile:
        # If the file is not a valid ZIP archive, do not process it further
        # You can also add custom handling or logging for non-ZIP files if needed
        return

    os.remove(file_path)


    
def process_unknown(file_path):
    # Do nothing for files with unknown extensions
    # # Print a message for files with unknown extensions
    # print(f"Unknown extension: {file_path}")
    pass

def sort_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            _, file_extension = os.path.splitext(file_name)
            file_extension = file_extension[1:].upper()  # Remove the dot and convert to uppercase

            # Add the extension to known_extensions set
            known_extensions.add(file_extension)

            if file_extension in image_extensions:
                process_image(file_path)
            elif file_extension in grafic_extensions:
                process_grafic(file_path)
            elif file_extension in internet_extensions:
                process_internet(file_path)
            elif file_extension in video_extensions:
                process_video(file_path)
            elif file_extension in document_extensions:
                process_document(file_path)
            elif file_extension in music_extensions:
                process_music(file_path)
            elif file_extension in archive_extensions:
                process_archive(file_path)
            else:
                unknown_extensions.add(file_extension)
                process_unknown(file_path)

    # Remove empty folders after sorting
    for root, dirs, _ in os.walk(folder_path, topdown=False):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

def main():
    if len(sys.argv) != 2:
        print("Usage: python sort.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]

   # Create destination folders if they don't exist
    for folder in ('images', 'videos', 'documents', 'music', 'archives', 'grafic', 'internet'):
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
    sort_folder(folder_path)

    # Print the results
    print("List of files in each category:")
    print("Images:", os.listdir(os.path.join(folder_path, 'images')))
    print("Grafic:", os.listdir(os.path.join(folder_path, 'grafic')))
    print("Internet:", os.listdir(os.path.join(folder_path, 'internet')))
    print("Videos:", os.listdir(os.path.join(folder_path, 'videos')))
    print("Documents:", os.listdir(os.path.join(folder_path, 'documents')))
    print("Music:", os.listdir(os.path.join(folder_path, 'music')))
    print("Archives:", os.listdir(os.path.join(folder_path, 'archives')))
    print("\nList of all extensions known to the script:", sorted(known_extensions))
    print("List of all extensions unknown to the script:", sorted(unknown_extensions))

if __name__ == "__main__":
    main()