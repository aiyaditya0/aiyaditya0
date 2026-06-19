import os
import shutil

def main():
    src_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\Website Error"
    dest_dir = r"C:\Users\aditya tiwari\." + "gemini" + r"\antigravity-ide\brain\ec97e555-4400-4db5-861a-29a60a5e2d68"
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    print(f"Copying from {src_dir} to {dest_dir}...")
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        if os.path.isfile(src_file):
            dest_file = os.path.join(dest_dir, filename)
            shutil.copy2(src_file, dest_file)
            print(f"  Copied: {filename}")

if __name__ == "__main__":
    main()
