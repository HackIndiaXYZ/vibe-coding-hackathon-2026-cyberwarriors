"""
Generate PDF Summary of CyberShield AI Project
Simple explanation of frontend, backend, database, and algorithms
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def create_summary_pdf():
    # Create PDF document
    doc = SimpleDocTemplate("CyberShield_AI_Summary.pdf", pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.darkblue,
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.darkblue,
        spaceAfter=12,
        spaceBefore=20
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        leading=14
    )
    
    # Title
    story.append(Paragraph("CyberShield AI - Project Summary", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Introduction
    intro_text = """
    <b>CyberShield AI</b> is an intelligent cybersecurity system that protects users from online scams, 
    phishing attacks, and fraudulent messages. It uses machine learning to automatically detect and 
    warn users about potential threats in real-time.
    """
    story.append(Paragraph(intro_text, normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Section 1: Frontend
    story.append(Paragraph("1. FRONTEND (User Interface)", heading_style))
    
    frontend_text = """
    <b>What is Frontend?</b><br/>
    The frontend is what users see and interact with. It's the visual part of the application that 
    runs in your web browser.
    
    <b>Technologies Used:</b><br/>
    • <b>HTML</b> - Structure of web pages<br/>
    • <b>CSS</b> - Styling and design<br/>
    • <b>JavaScript</b> - Interactive functionality<br/>
    • <b>Chrome Extension</b> - Browser extension for WhatsApp Web and Gmail
    
    <b>Components:</b><br/>
    • <b>content.js</b> - Monitors messages on WhatsApp Web and Gmail<br/>
    • <b>background.js</b> - Runs in background, communicates with backend API<br/>
    • <b>popup.html</b> - Extension popup interface for settings<br/>
    • <b>manifest.json</b> - Extension configuration file
    
    <b>What it does:</b><br/>
    • Automatically scans messages on WhatsApp Web and Gmail<br/>
    • Shows warning badges on suspicious messages<br/>
    • Displays alerts when scams are detected<br/>
    • Provides user settings and statistics
    """
    story.append(Paragraph(frontend_text, normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Section 2: Backend
    story.append(Paragraph("2. BACKEND (Server)", heading_style))
    
    backend_text = """
    <b>What is Backend?</b><br/>
    The backend is the server-side logic that processes data and makes decisions. 
    It runs on your local computer and handles the heavy computational work.
    
    <b>Technologies Used:</b><br/>
    • <b>Python</b> - Programming language<br/>
    • <b>Flask</b> - Web framework for API<br/>
    • <b>scikit-learn</b> - Machine learning library<br/>
    • <b>pickle</b> - For saving/loading trained models
    
    <b>Components:</b><br/>
    • <b>app.py</b> - Main Flask API server<br/>
    • <b>train_fortinet_model.py</b> - Model training script<br/>
    • <b>model.pkl</b> - Trained machine learning model<br/>
    • <b>vectorizer.pkl</b> - Text vectorization tool
    
    <b>What it does:</b><br/>
    • Receives messages from the frontend extension<br/>
    • Uses machine learning to analyze text for scam patterns<br/>
    • Returns risk assessment (safe/suspicious/scam)<br/>
    • Provides API endpoints for detection
    """
    story.append(Paragraph(backend_text, normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Section 3: Database
    story.append(Paragraph("3. DATABASE (Data Storage)", heading_style))
    
    database_text = """
    <b>What is Database?</b><br/>
    The database stores the trained machine learning models and vectorization tools 
    that the backend uses to detect scams.
    
    <b>Storage Method:</b><br/>
    • <b>Pickle Files (.pkl)</b> - Python serialization format<br/>
    • <b>model.pkl</b> - Stores the trained Random Forest classifier<br/>
    • <b>vectorizer.pkl</b> - Stores the TF-IDF vectorizer<br/>
    • <b>job_scam_training_dataset.csv</b> - Training data examples
    
    <b>What it stores:</b><br/>
    • Trained machine learning model parameters<br/>
    • Text vectorization mappings<br/>
    • Training dataset with scam examples<br/>
    • Pattern recognition rules
    
    <b>Note:</b> This is a local file-based storage, not a traditional database. 
    All data stays on your computer for privacy.
    """
    story.append(Paragraph(database_text, normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Section 4: Algorithms
    story.append(Paragraph("4. ALGORITHMS (Machine Learning)", heading_style))
    
    algorithms_text = """
    <b>What are Algorithms?</b><br/>
    Algorithms are mathematical formulas and rules that the computer uses to 
    analyze data and make predictions about whether a message is a scam.
    
    <b>Primary Algorithm:</b><br/>
    • <b>Random Forest Classifier</b> - Machine learning algorithm that uses 
      multiple decision trees to make predictions. It's trained on thousands 
      of scam examples to learn patterns.
    
    <b>Text Processing:</b><br/>
    • <b>TF-IDF (Term Frequency-Inverse Document Frequency)</b> - Converts 
      text into numerical values by analyzing word importance. Common scam 
      words get higher weights.
    
    <b>Fallback Detection:</b><br/>
    • <b>Keyword Pattern Matching</b> - When backend is offline, uses predefined 
      scam keywords and patterns to detect threats. Supports multiple languages 
      (English, Hindi, Tamil, Telugu, Bengali, etc.)
    
    <b>How it works:</b><br/>
    1. User receives a message<br/>
    2. Text is converted to numbers using TF-IDF<br/>
    3. Random Forest analyzes the numbers<br/>
    4. Algorithm calculates scam probability (0-100%)<br/>
    5. Returns risk level: Safe (0-50%), Suspicious (50-75%), Scam (75-100%)
    
    <b>Training:</b><br/>
    • Model is trained on dataset of real scam messages<br/>
    • Uses supervised learning with labeled examples<br/>
    • Achieves 95%+ accuracy on known scam patterns
    """
    story.append(Paragraph(algorithms_text, normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Summary Table
    story.append(Paragraph("QUICK REFERENCE TABLE", heading_style))
    
    table_data = [
        ['Component', 'Technology', 'Purpose'],
        ['Frontend', 'HTML/CSS/JS', 'User interface in browser'],
        ['Extension', 'Chrome Extension', 'Monitors WhatsApp & Gmail'],
        ['Backend', 'Python/Flask', 'API server for ML processing'],
        ['Database', 'Pickle Files', 'Stores trained models'],
        ['Algorithm', 'Random Forest', 'ML classification'],
        ['Text Processing', 'TF-IDF', 'Text to numbers conversion'],
        ['Fallback', 'Keyword Matching', 'Offline detection']
    ]
    
    table = Table(table_data, colWidths=[2*inch, 2*inch, 2.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 0.3*inch))
    
    # Architecture Flow
    story.append(Paragraph("SYSTEM ARCHITECTURE FLOW", heading_style))
    
    flow_text = """
    <b>How the System Works:</b><br/><br/>
    1. User opens WhatsApp Web or Gmail<br/>
    2. Chrome Extension (Frontend) loads automatically<br/>
    3. Content Script monitors new messages<br/>
    4. Message text is sent to Backend API (localhost:5000)<br/>
    5. Backend loads ML model from Pickle files (Database)<br/>
    6. TF-IDF converts text to numbers<br/>
    7. Random Forest algorithm analyzes the numbers<br/>
    8. Backend returns risk assessment to Frontend<br/>
    9. Frontend shows warning badge/alert if scam detected<br/>
    10. User is protected from clicking malicious links
    """
    story.append(Paragraph(flow_text, normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Conclusion
    story.append(Paragraph("CONCLUSION", heading_style))
    
    conclusion_text = """
    CyberShield AI combines modern web technologies with machine learning to create 
    an intelligent scam detection system. The frontend provides a seamless user 
    experience, the backend handles complex ML processing, the database stores 
    trained models, and the algorithms make intelligent predictions about scam 
    messages. All processing happens locally on your computer for maximum privacy 
    and security.
    
    <b>Key Benefits:</b><br/>
    • Real-time scam detection<br/>
    • Multi-language support<br/>
    • Works offline with fallback detection<br/>
    • Privacy-focused (no data leaves your computer)<br/>
    • High accuracy (95%+ on known patterns)
    """
    story.append(Paragraph(conclusion_text, normal_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Footer
    footer_text = """
    <font size="8">Generated for CyberShield AI Project | Version 3.2 | © 2026 Soundar M & Team</font>
    """
    story.append(Paragraph(footer_text, ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, alignment=TA_CENTER)))
    
    # Build PDF
    doc.build(story)
    print("✅ PDF Summary generated successfully: CyberShield_AI_Summary.pdf")

if __name__ == "__main__":
    create_summary_pdf()
