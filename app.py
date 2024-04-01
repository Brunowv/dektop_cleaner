import os
import shutil


img_exts = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
doc_exts = [".pdf", ".doc", ".docx", ".epub", ".odg"]
zip_exts = [".zip"]
video_exts = [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv"]


downloads_folder = os.path.expanduser("~/Downloads")
img_folder = os.path.expanduser("~/Imagenes")
doc_folder = os.path.expanduser("~/Documents")
zip_folder = os.path.expanduser("~/Zip")
video_folder = os.path.expanduser("~/Videos")


for folder in [img_folder, doc_folder, zip_folder, video_folder]:
    os.makedirs(folder, exist_ok=True)


for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    if os.path.isfile(file_path):

        _, ext = os.path.splitext(filename)

        if ext in img_exts:
            shutil.move(file_path, img_folder)
        elif ext in doc_exts:
            shutil.move(file_path, doc_folder)
        elif ext in zip_exts:
            shutil.move(file_path, zip_folder)
        elif ext in video_exts:
            shutil.move(file_path, video_folder)
