import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class BeautifulPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_margins(20, 20, 20)
        self.set_auto_page_break(True, margin=20)
        
    def header(self):
        # Draw dark background on every page
        self.set_fill_color(5, 5, 5) # #050505
        self.rect(0, 0, self.w, self.h, 'F')
        
        # Subtle header line & site name (only if not first page)
        if self.page_no() > 1:
            self.set_text_color(165, 140, 123) # var(--text-muted)
            self.set_font('helvetica', 'I', 8)
            # Use XPos and YPos for positioning
            self.cell(0, 10, 'FutureWithAi - AI Company OS Blueprint Prompt', new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.cell(0, 10, f'Page {self.page_no()}', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='R')
            self.set_draw_color(35, 35, 35) # #232323
            self.set_line_width(0.5)
            self.line(20, 22, self.w - 20, 22)
            self.ln(5)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font('helvetica', 'I', 8)
            self.set_text_color(165, 140, 123)
            self.cell(0, 10, 'futurewithai.anshumanenterprises.online', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

def sanitize_text(text):
    # Map common unicode chars to ascii counterparts
    text = text.replace('↓', ' -> ')
    text = text.replace('→', ' -> ')
    text = text.replace('•', '-')
    text = text.replace('…', '...')
    text = text.replace('“', '"').replace('”', '"')
    text = text.replace('‘', "'").replace('’', "'")
    # Encode to latin-1 and ignore other unsupported chars
    return text.encode('latin-1', 'ignore').decode('latin-1')

def create_blueprint_pdf():
    pdf = BeautifulPDF()
    pdf.add_page()
    
    # 1. Large Brand Logo
    logo_path = 'primary-logo.webp'
    if os.path.exists(logo_path):
        # Center the logo (w = 120, page width is 210, so x = (210 - 120)/2 = 45)
        pdf.image(logo_path, x=45, y=30, w=120)
        pdf.ln(50) # space after logo
    else:
        pdf.ln(20)
        pdf.set_font('helvetica', 'B', 32)
        pdf.set_text_color(255, 138, 0) # Orange
        pdf.cell(0, 20, 'FutureWithAi', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.ln(20)
        
    # Title
    pdf.set_font('helvetica', 'B', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 15, 'AI Company OS Blueprint', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    
    # Subtitle / Info
    pdf.set_font('helvetica', '', 12)
    pdf.set_text_color(221, 193, 174) # var(--text-secondary)
    pdf.multi_cell(0, 7, 'Use this blueprint to build a full-stack SaaS AI Agent system where specialized AI departments work together under a CEO agent to automate your business.', align='C')
    pdf.ln(10)
    
    # Button-like Link to Emergent App
    btn_w = 140
    btn_h = 12
    btn_x = (pdf.w - btn_w) / 2
    
    pdf.set_x(btn_x)
    url = "https://app.emergent.sh/landing/"
    pdf.set_fill_color(255, 138, 0) # Orange button
    pdf.set_text_color(5, 5, 5) # Dark text
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(btn_w, btn_h, "Click here to open Emergent App & build yours", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C', fill=True, link=url)
    pdf.ln(15)
    
    # Divider line
    pdf.set_draw_color(255, 138, 0)
    pdf.set_line_width(1)
    pdf.line(40, pdf.get_y(), pdf.w - 40, pdf.get_y())
    pdf.ln(10)
    
    # Read the text file content
    txt_path = 'PROMPT FOR EMERGENT .txt'
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    pdf.set_font('helvetica', '', 10)
    pdf.set_text_color(243, 223, 209) # var(--text-primary)
    
    for idx, line in enumerate(lines):
        line_str = line.strip()
        line_str = sanitize_text(line_str)
        
        # Skip original prompt header / copy text instruction since it's now a formal PDF
        if "PROMPT FOR EMERGENT" in line_str or "Copy Everything" in line_str:
            continue
            
        # Divider lines in text file
        if line_str.startswith('___'):
            pdf.ln(5)
            pdf.set_draw_color(35, 35, 35)
            pdf.set_line_width(0.5)
            pdf.line(20, pdf.get_y(), pdf.w - 20, pdf.get_y())
            pdf.ln(5)
            continue
            
        if not line_str:
            pdf.ln(3)
            continue
            
        # Check if line is a Heading (e.g., all uppercase like CORE CONCEPT)
        is_heading = False
        headings = [
            "CORE CONCEPT", "AI EMPLOYEES", "FRONTEND", "DASHBOARD", 
            "AGENT CARDS", "CEO PAGE", "TASK SYSTEM", "APPROVAL SYSTEM",
            "MARKETING WORKSPACE", "SALES WORKSPACE", "RESEARCH WORKSPACE",
            "DEVELOPER WORKSPACE", "OPERATIONS WORKSPACE", "FINANCE WORKSPACE",
            "HR WORKSPACE", "LIVE ACTIVITY FEED", "DATABASE", "AUTHENTICATION",
            "API LAYER", "AI ORCHESTRATION", "KNOWLEDGE BASE", "AUTOMATION ENGINE",
            "NOTIFICATIONS", "ADMIN PANEL", "FUTURE READY", "FINAL GOAL"
        ]
        
        for h in headings:
            if line_str.startswith(h):
                is_heading = True
                break
                
        if is_heading:
            pdf.ln(8)
            pdf.set_font('helvetica', 'B', 14)
            pdf.set_text_color(255, 138, 0) # Orange heading
            pdf.cell(0, 8, line_str, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.set_font('helvetica', '', 10)
            pdf.set_text_color(243, 223, 209)
            pdf.ln(2)
        elif line_str.startswith('* ') or line_str.startswith('- '):
            # Bullet point indent
            pdf.set_font('helvetica', '', 10)
            pdf.set_text_color(221, 193, 174) # var(--text-secondary)
            pdf.set_x(25)
            pdf.multi_cell(0, 6, "- " + line_str[2:])
            # Reset x position after multi_cell to the left margin
            pdf.set_x(20)
        elif line_str.endswith(':'):
            # Sub-heading
            pdf.ln(2)
            pdf.set_font('helvetica', 'B', 11)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 6, line_str, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.set_font('helvetica', '', 10)
            pdf.set_text_color(243, 223, 209)
        else:
            pdf.set_font('helvetica', '', 10)
            pdf.set_text_color(243, 223, 209)
            # Ensure x is at left margin before calling multi_cell
            pdf.set_x(20)
            pdf.multi_cell(0, 6, line_str)
            # Reset x to margin
            pdf.set_x(20)
            
    # Output PDF
    pdf.output('PROMPT FOR EMERGENT.pdf')
    print("PDF generated successfully.")

if __name__ == '__main__':
    create_blueprint_pdf()
