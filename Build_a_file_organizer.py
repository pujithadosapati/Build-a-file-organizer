from pathlib import Path
import shutil
# Create test folder
folder = Path("/content/Test_Files")
folder.mkdir(exist_ok=True)
# Create sample files
sample_files = [
    "photo.jpg",
    "notes.pdf",
    "song.mp3",
    "video.mp4",
    "program.py"
]
for name in sample_files:
    (folder / name).write_text("Sample file")

print("Sample files created successfully!")

# Organize files
file_types = {
    ".jpg": "Images",
    ".pdf": "Documents",
    ".mp3": "Audio",
    ".mp4": "Videos",
    ".py": "Python_Files"
}

for file in list(folder.iterdir()):
    if file.is_file():
        category = file_types.get(file.suffix.lower(), "Others")
        destination = folder / category
        destination.mkdir(exist_ok=True)

        new_file = destination / file.name
        count = 1

        while new_file.exists():
            new_file = destination / f"{file.stem}_{count}{file.suffix}"
            count += 1

        shutil.move(str(file), str(new_file))
        print(file.name, "->", category)

print("File organization completed successfully!")
