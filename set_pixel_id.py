import os

def update_pixel_id():
    pixel_id = input("Enter your Meta Pixel ID: ").strip()
    if not pixel_id.isdigit():
        print("Error: Meta Pixel ID should contain only digits.")
        return

    placeholder = "YOUR_PIXEL_ID"
    changed_files = 0

    # Walk through workspace files
    for root, dirs, files in os.walk("."):
        # Skip hidden directories like .git
        if any(part.startswith('.') for part in root.split(os.sep)):
            continue
        
        for file in files:
            if file.endswith(('.html', '.js')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if placeholder in content:
                        new_content = content.replace(placeholder, pixel_id)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"✓ Updated: {file_path}")
                        changed_files += 1
                except Exception as e:
                    print(f"✗ Error reading {file_path}: {e}")

    print(f"\nCompleted! Updated {changed_files} files with Pixel ID: {pixel_id}")

if __name__ == "__main__":
    update_pixel_id()
