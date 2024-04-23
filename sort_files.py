import argparse
import os
import shutil
import threading

def copy_file(src, dst):
    try:
        shutil.copy2(src, dst)
    except Exception as e:
        print(f"Error copying file {src} to {dst}: {e}")

def process_folder(folder, output):
    for root, _, files in os.walk(folder):
        for file in files:
            ext = os.path.splitext(file)[1][1:]
            ext_folder = os.path.join(output, ext)
            if not os.path.exists(ext_folder):
                try:
                    os.makedirs(ext_folder)
                except Exception as e:
                    print(f"Error creating directory {ext_folder}: {e}")
                    continue
            src_file = os.path.join(root, file)
            dst_file = os.path.join(ext_folder, file)
            threading.Thread(target=copy_file, args=(src_file, dst_file)).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort files in a folder by extension using multiple threads.")
    parser.add_argument("--source", "-s", help="Source folder", required=True)
    parser.add_argument("--output", "-o", help="Output folder", default="dist")
    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    process_folder(args.source, args.output)

    print(f"You can delete {args.source}")