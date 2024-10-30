import os
import csv
from mutagen.mp3 import MP3

directory_audio_files = "W:\\bible\\vi\\"
# directory_audio_files = os.getcwd()  #     if executed inside the folder with the files
csv_file = "info_audio_files_vi.csv"

def list_folders_files_and_size(directory):
    folders_info = {}
    for name in os.listdir(directory):
        folder_path = os.path.join(directory, name)
        if os.path.isdir(folder_path):
            subfolders = [sub for sub in os.walk(folder_path)][1:]
            file_count = 0
            total_size = 0
            file_len_s = 0
            for root, dirs, files in os.walk(folder_path):
                file_count += len(files)
                for file in files:
                    file_path = os.path.join(root, file)
                    total_size += os.path.getsize(file_path)
                    audio = MP3(file_path)
                    file_len_s += audio.info.length
            folders_info[name] = {
                "files": file_count,
                "size": total_size,
                "size_bytes": total_size, 
                "length_seconds": file_len_s
            }
    return folders_info

def size_format(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0

folders_info = list_folders_files_and_size(directory_audio_files)

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Folder", "Files", "Size", "Size (Bytes)", "Length (Seconds)"])
    for folder, info in folders_info.items():
        size_str = size_format(info["size"])
        writer.writerow([folder, info['files'], size_str, info['size_bytes'], info["length_seconds"]])

print(f"Results exported to {csv_file}")
