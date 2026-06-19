import os

def main():
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    filepath = os.path.join(root_dir, "video-editing.html")
    
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found!")
        return
        
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    # Replace the two variations of the ignored folder paths
    targets = [
        "500%20gb%20editing%20Pack/500%20GB%20editing%20Pack/",
        "500 gb editing Pack/500 GB editing Pack/"
    ]
    
    replacement = "video-editing-assets/"
    
    modified_content = content
    for target in targets:
        count = modified_content.count(target)
        if count > 0:
            modified_content = modified_content.replace(target, replacement)
            print(f"Replaced {count} instances of '{target}'")
            
    if modified_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(modified_content)
        print("Successfully updated video-editing.html!")
    else:
        print("No matches found or no replacements were necessary.")

if __name__ == "__main__":
    main()
