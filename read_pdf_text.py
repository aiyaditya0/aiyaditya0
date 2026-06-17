import os

def check_libraries():
    try:
        import pypdf
        print("pypdf is installed.")
        return True
    except ImportError:
        print("pypdf is NOT installed. Attempting to install...")
        import subprocess
        try:
            subprocess.run(["pip", "install", "pypdf"], check=True)
            import pypdf
            print("pypdf installed successfully.")
            return True
        except Exception as e:
            print(f"Failed to install pypdf: {e}")
            return False

def extract_details():
    if not check_libraries():
        print("Cannot extract text without pypdf library.")
        return
        
    import pypdf
    folder_path = 'IMPORTANT ASSET'
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    
    out_file = 'extracted_pdf_details.txt'
    with open(out_file, 'w', encoding='utf-8') as out:
        out.write("EXTRACTED TEXT AND LINKS FROM ALL ORIGINAL PDF FILES\n")
        out.write("=" * 80 + "\n")
        
        for pdf_file in pdf_files:
            file_path = os.path.join(folder_path, pdf_file)
            out.write(f"\n\n=== FILE: {pdf_file} ===\n")
            out.write("-" * 50 + "\n")
            try:
                reader = pypdf.PdfReader(file_path)
                for page_num, page in enumerate(reader.pages):
                    text = page.extract_text()
                    out.write(f"\n--- Page {page_num + 1} ---\n")
                    out.write(text + "\n")
                    
                    # Extract links from annotations if any
                    if "/Annots" in page:
                        annots = page["/Annots"]
                        for annot in annots:
                            obj = annot.get_object()
                            if obj.get("/Subtype") == "/Link":
                                action = obj.get("/A")
                                if action and action.get("/URI"):
                                    uri = action["/URI"]
                                    out.write(f"[Link Annotation]: {uri}\n")
            except Exception as e:
                out.write(f"Error reading file {pdf_file}: {e}\n")
                
    print(f"Extraction completed. Details written to '{out_file}'.")

if __name__ == '__main__':
    extract_details()
