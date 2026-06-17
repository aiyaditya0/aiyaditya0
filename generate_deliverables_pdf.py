import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class BeautifulPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_margins(15, 20, 15)
        self.set_auto_page_break(True, margin=20)
        
    def header(self):
        # Draw dark background on every page
        self.set_fill_color(5, 5, 5) # #050505
        self.rect(0, 0, self.w, self.h, 'F')
        
        # Subtle header line & site name (only if not first page)
        if self.page_no() > 1:
            self.set_text_color(165, 140, 123) # var(--text-muted)
            self.set_font('helvetica', 'I', 8)
            self.cell(0, 10, 'FutureWithAi - Master Deliverables & Links Catalog', new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.cell(0, 10, f'Page {self.page_no()}', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='R')
            self.set_draw_color(35, 35, 35) # #232323
            self.set_line_width(0.5)
            self.line(15, 22, self.w - 15, 22)
            self.ln(5)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font('helvetica', 'I', 8)
            self.set_text_color(165, 140, 123)
            self.cell(0, 10, 'futurewithai.anshumanenterprises.online', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

def sanitize_text(text):
    text = text.replace('→', ' -> ')
    text = text.replace('•', '-')
    text = text.replace('…', '...')
    text = text.replace('“', '"').replace('”', '"')
    text = text.replace('₹', 'Rs ')
    text = text.replace('‘', "'").replace('’', "'")
    return text.encode('latin-1', 'ignore').decode('latin-1')

def generate_catalog_pdf():
    pdf = BeautifulPDF()
    pdf.add_page()
    
    # 1. Logo
    logo_path = 'primary-logo.png'
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=45, y=30, w=120)
        pdf.ln(50)
    else:
        pdf.ln(20)
        pdf.set_font('helvetica', 'B', 32)
        pdf.set_text_color(255, 138, 0)
        pdf.cell(0, 20, 'FutureWithAi', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.ln(20)
        
    # Title
    pdf.set_font('helvetica', 'B', 22)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 15, 'Master Deliverables & Download Links', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    
    # Subtitle
    pdf.set_font('helvetica', '', 11)
    pdf.set_text_color(221, 193, 174)
    pdf.multi_cell(0, 6, 'This document lists all 31 product variations across our store categories with their corresponding direct Google Drive, GitHub, and Mega links verified from the original source PDFs.', align='C')
    pdf.ln(10)
    
    # Divider line
    pdf.set_draw_color(255, 138, 0)
    pdf.set_line_width(1)
    pdf.line(40, pdf.get_y(), pdf.w - 40, pdf.get_y())
    pdf.ln(10)

    # Categories Data
    categories = [
        {
            "name": "1. Viral Reels Bundle (mega-reels.html)",
            "primary_desc": "Contains multiple folder packages. Links mapped from 10000 + REEL-BUNDLE-2026.pdf.",
            "items": [
                ("Starter Pack", "Rs 9", "1,000+ Reels (30K Reels Folder)", "https://drive.google.com/drive/folders/1qBpqgApYwv86vNhsqKhJume2NNo_Qg9V"),
                ("Creator Pack", "Rs 29", "5,000+ Reels (Glowing Motion Graphics)", "https://drive.google.com/drive/folders/1paWoOOCqEX_er85dJPhzWKRMPcU6S_C8"),
                ("Silver Pack", "Rs 49", "15,000+ Reels (Cricket Reels Folder)", "https://drive.google.com/drive/folders/14wmvnGhTFT40hdfjDdm_aQwjji7xbhtY"),
                ("Gold Pack", "Rs 79", "50,000+ Reels (AI Anime Reels)", "https://drive.google.com/drive/folders/1vefoBhE-bHMiJ0guIB49GeJDsADlguYB"),
                ("Ultimate Pack (Bestseller)", "Rs 99", "100,000+ Reels (30K Reels Folder)", "https://drive.google.com/drive/folders/1qBpqgApYwv86vNhsqKhJume2NNo_Qg9V"),
                ("Mega Reseller Bundle", "Rs 199", "All Reels + Graphics + PLR (Mega)", "https://mega.nz/folder/BBpxDYQQ#OLyaL1a0vDXxG__ddzyxoQ")
            ]
        },
        {
            "name": "2. n8n Automation Workflows (n8n-pack.html & n8n-workflow-automation.html)",
            "primary_desc": "Standard templates use GitHub; Enterprise use Google Drive/GitHub.",
            "items": [
                ("Starter Workflows (Standard)", "Rs 19", "100+ JSONs (GitHub Link)", "https://github.com/anshumanenterprises1119/futurewithai"),
                ("Pro Workflows (Standard)", "Rs 49", "500+ JSONs (GitHub Link)", "https://github.com/anshumanenterprises1119/futurewithai"),
                ("Developer Pack (Standard)", "Rs 99", "2,000+ JSONs (GitHub Link)", "https://github.com/anshumanenterprises1119/futurewithai"),
                ("Advanced AI Agents (Enterprise)", "Rs 199", "5,000+ Schemas (Drive Folder)", "https://drive.google.com/drive/folders/1HK8GYyfqNK6z64BvEzjBMJuH8xM0-LeD"),
                ("Enterprise Pack (Enterprise)", "Rs 349", "14,000+ Schemas (Drive Folder)", "https://drive.google.com/drive/folders/1HK8GYyfqNK6z64BvEzjBMJuH8xM0-LeD"),
                ("Ultimate Agency Suite (Enterprise)", "Rs 449", "14,000+ JSONs + PLR (GitHub)", "https://github.com/Zie619/n8n-workflows")
            ]
        },
        {
            "name": "3. Video Editing Toolkit (video-editing.html)",
            "primary_desc": "Premium editing folders. Mapped from 500 GB VIDOE EDITING PACK.pdf.",
            "items": [
                ("Mini Editing Kit", "Rs 9", "10 GB Assets (Video Editing Drive)", "https://drive.google.com/drive/folders/1-XwOjUh5J-KbdgsMunjzyEp0v0eOHiDd?usp=drive_link"),
                ("Creator Editing Kit", "Rs 29", "50 GB Assets (Video Editing Drive)", "https://drive.google.com/drive/folders/1-XwOjUh5J-KbdgsMunjzyEp0v0eOHiDd?usp=drive_link"),
                ("Pro Editing Kit", "Rs 49", "150 GB Assets (Video Editing Drive)", "https://drive.google.com/drive/folders/1-XwOjUh5J-KbdgsMunjzyEp0v0eOHiDd?usp=drive_link"),
                ("VFX & LUTs Pack", "Rs 99", "250 GB FX Presets (Video Editing Drive)", "https://drive.google.com/drive/folders/1-XwOjUh5J-KbdgsMunjzyEp0v0eOHiDd?usp=drive_link"),
                ("Studio Pack", "Rs 199", "500 GB+ Premium Assets (2026 Bundle)", "https://drive.google.com/drive/folders/10QKbUY7qRyKM3m1ig6EsVQ3KNSJdDZ8Y?usp=drive_link"),
                ("Director Suite", "Rs 299", "500 GB+ Assets + Bonus Graphics Link", "https://drive.google.com/drive/folders/1hORXYzDSl0lQnOHbBChKIF6s4wSTC0mP?usp=drive_link")
            ]
        },
        {
            "name": "4. Web Apps Source Code (web-apps.html)",
            "primary_desc": "Contains multiple tested SaaS application zips. Mapped from 1500+ Web Apps PDF.",
            "items": [
                ("Basic SaaS Bundle", "Rs 9", "5 Web App Source Codes (30 zips link)", "https://drive.google.com/file/d/1Yxav8ddkv83hraWX0-syO3P7zGdpN9kV/view?usp=drivesdk"),
                ("Bronze SaaS Bundle", "Rs 29", "25 Web App Source Codes (PHP Part 1)", "https://drive.google.com/file/d/1kNLxo7Fo6qhFo_wimJjYLaLQMDptMSjY/view?usp=drivesdk"),
                ("Silver SaaS Bundle", "Rs 49", "100 Web App Source Codes (PHP Part 2)", "https://drive.google.com/file/d/1oAYVlPR2SBlvzdhV2x4m0zQrmRTRHjXX/view?usp=drivesdk"),
                ("Gold SaaS Bundle", "Rs 99", "500 Web App Source Codes (PHP Part 3)", "https://drive.google.com/file/d/1cV1rTcI0XQWe6Y4C3lQjymwnxfduNa3B/view?usp=drivesdk"),
                ("Premium Bundle (Bestseller)", "Rs 199", "1500+ Web Apps (Software 115 products)", "https://drive.google.com/file/d/1yNQyxLnLbWppNyzdzQhuYXh6f-Vpjf4n/view?usp=drivesdk"),
                ("SaaS Suite", "Rs 299", "1500+ Web Apps + Mega Themes & Plugins", "https://mega.nz/folder/It4RVKAQ#DIh5_Axo7CiYabcL5IB3Eg/folder/h1JxxYjD")
            ]
        },
        {
            "name": "5. Digital Marketing Resource Bundle (digital-marketing-bundle.html)",
            "primary_desc": "Deepak Sahu (Digital Marketer) Master Folder holding Canva, Prompts & courses.",
            "items": [
                ("Social Media Kit", "Rs 9", "1,000+ Canva & Ads (Primary DM Folder)", "https://drive.google.com/drive/folders/1XyNfF4cxEJTkOJHxAjPLILeAqdAutgdX?usp=drive_link"),
                ("ChatGPT Prompts Kit", "Rs 29", "10,000+ Prompts (Primary DM Folder)", "https://drive.google.com/drive/folders/1XyNfF4cxEJTkOJHxAjPLILeAqdAutgdX?usp=drive_link"),
                ("Ebooks & PLR Pack", "Rs 49", "5,000+ Books & Guides (Primary DM Folder)", "https://drive.google.com/drive/folders/1XyNfF4cxEJTkOJHxAjPLILeAqdAutgdX?usp=drive_link"),
                ("Graphic Design Kit", "Rs 99", "100 GB Design Assets (Primary DM Folder)", "https://drive.google.com/drive/folders/1XyNfF4cxEJTkOJHxAjPLIFeAqdAutgdX?usp=drive_link"),
                ("Pro Marketing Kit", "Rs 199", "250+ Marketing Assets (Primary DM Folder)", "https://drive.google.com/drive/folders/1XyNfF4cxEJTkOJHxAjPLIFeAqdAutgdX?usp=drive_link"),
                ("Agency Marketing Suite", "Rs 299", "500+ Marketing Assets (Primary DM Folder)", "https://drive.google.com/drive/folders/1XyNfF4cxEJTkOJHxAjPLIFeAqdAutgdX?usp=drive_link"),
                ("Ultimate DM Bundle", "Rs 499", "700+ Marketing Assets (Primary DM Folder)", "https://drive.google.com/drive/folders/1XyNfF4cxEJTkOJHxAjPLIFeAqdAutgdX?usp=drive_link")
            ]
        }
    ]

    for cat in categories:
        pdf.ln(5)
        # Category Heading
        pdf.set_font('helvetica', 'B', 12)
        pdf.set_text_color(255, 138, 0) # Orange
        pdf.cell(0, 8, sanitize_text(cat["name"]), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        # Display main description for category
        pdf.set_font('helvetica', 'I', 8.5)
        pdf.set_text_color(165, 140, 123) # Muted
        pdf.cell(0, 5, sanitize_text(cat["primary_desc"]), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

        # Draw Table Head
        pdf.set_font('helvetica', 'B', 9)
        pdf.set_text_color(255, 255, 255)
        pdf.set_fill_color(20, 20, 20)
        
        pdf.cell(45, 7, "Tier Name", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, fill=True)
        pdf.cell(15, 7, "Price", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, fill=True, align='C')
        pdf.cell(65, 7, "Deliverables", border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, fill=True)
        pdf.cell(55, 7, "Click to Download Link", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True, align='C')
        
        # Draw Table Rows
        pdf.set_font('helvetica', '', 8.5)
        pdf.set_text_color(243, 223, 209)
        
        for name, price, qty, link_url in cat["items"]:
            # Row printing
            pdf.cell(45, 6, sanitize_text(name), border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
            pdf.cell(15, 6, sanitize_text(price), border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
            pdf.cell(65, 6, sanitize_text(qty), border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
            
            # Clickable cell in table
            pdf.set_text_color(255, 138, 0) # Orange link text
            pdf.cell(55, 6, "Download Files", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C', link=link_url)
            pdf.set_text_color(243, 223, 209) # Restore color
            
        pdf.ln(5)

    # Output PDF
    out_name = 'FutureWithAI_Products_Links.pdf'
    pdf.output(out_name)
    print(f"PDF generated successfully as '{out_name}'.")

if __name__ == '__main__':
    generate_catalog_pdf()
