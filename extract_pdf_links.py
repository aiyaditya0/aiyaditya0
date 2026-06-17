import os
import re

def extract_links_from_pdf():
    folder_path = 'IMPORTANT ASSET'
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    
    url_pattern = re.compile(r'https?://[^\s()<>"]+')
    
    print("Mapping PDF files to folder links (Max 10 per file)...")
    print("=" * 60)
    
    for pdf_file in pdf_files:
        file_path = os.path.join(folder_path, pdf_file)
        print(f"\n[File] {pdf_file}")
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()
            
            matches = url_pattern.findall(content)
            unique_urls = sorted(list(set(matches)))
            
            cleaned_urls = []
            for url in unique_urls:
                url = re.split(r'[\)\>\\]', url)[0]
                cleaned_urls.append(url)
                
            cleaned_urls = sorted(list(set(cleaned_urls)))
            
            drive_folders = []
            mega_folders = []
            
            for url in cleaned_urls:
                if 'drive.google.com/drive/folders' in url or 'drive.google.com/folderview' in url:
                    drive_folders.append(url)
                elif 'mega.nz/folder/' in url or 'mega.nz/#F!' in url or 'mega.nz/file/' in url:
                    mega_folders.append(url)
            
            if drive_folders:
                print(f"  Google Drive Folders (Total: {len(drive_folders)}):")
                for url in drive_folders[:10]:
                    print(f"    - {url}")
                if len(drive_folders) > 10:
                    print(f"    - ... and {len(drive_folders) - 10} more folders")
            if mega_folders:
                print(f"  Mega Folders/Files (Total: {len(mega_folders)}):")
                for url in mega_folders[:10]:
                    print(f"    - {url}")
                if len(mega_folders) > 10:
                    print(f"    - ... and {len(mega_folders) - 10} more")
            
            if not drive_folders and not mega_folders:
                print("  No drive/mega folder links found.")
        except Exception as e:
            print(f"  Error reading file: {e}")

if __name__ == '__main__':
    extract_links_from_pdf()
