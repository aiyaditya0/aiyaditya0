import os
import re
import sys

def main():
    # Set console encoding to UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    html_files = ['checkout.html', 'loogo white.html', 'n8n-pack.html', 'payment-failure.html', 'payment-success.html', 'video-editing.html']
    
    for filename in html_files:
        filepath = os.path.join(root_dir, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Find all occurrences of literal \n (backslash followed by n)
        matches = [m.start() for m in re.finditer(r'\\n', content)]
        
        if matches:
            print(f"\nFile: {filename} - Found {len(matches)} literal '\\n' sequences:")
            for idx, pos in enumerate(matches):
                # Get surrounding context
                start = max(0, pos - 40)
                end = min(len(content), pos + 40)
                context = content[start:end].replace('\n', ' ').replace('\r', ' ')
                
                # Check if it looks like it's inside a <script> block
                before = content[:pos]
                last_script_open = before.rfind('<script')
                last_script_close = before.rfind('</script>')
                is_in_script = last_script_open > last_script_close
                
                status = "Script (Normal)" if is_in_script else "HTML (Potential Bug!)"
                print(f"  #{idx+1} [Status: {status}]: ...{context}...")

if __name__ == "__main__":
    main()
