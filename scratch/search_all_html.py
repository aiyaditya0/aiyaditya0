import os

directory = "c:/Users/aditya tiwari/Downloads/FUTUREWITHAI WEB"
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                if "your cart" in content.lower():
                    print(f"Found in: {file}")
            except Exception as e:
                pass
