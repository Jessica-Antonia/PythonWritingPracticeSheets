#letters for 2nd grade penmanship practice

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Create a PDF document
file_path = "/home/jessica/MyRepo/PythonWritingPracticeSheets/Gerrit_2nd_Grade_Writing_Practice.pdf"
doc = SimpleDocTemplate(file_path, pagesize=letter)
styles = getSampleStyleSheet()
elements = []

# Add a title
title = Paragraph("Gerrit's 2nd Grade Writing Practice", styles['Title'])
elements.append(title)
elements.append(Spacer(1, 12))

# Instructions paragraph
instructions = Paragraph(
    "Instructions: Practice writing lowercase and uppercase letters neatly and small enough to fit between the lines. "
    "Take your time and focus on forming each letter correctly. Try to write slowly and with care.",
    styles['Normal']
)
elements.append(instructions)
elements.append(Spacer(1, 12))

# Table with lines to trace and write letters
table_data = [["Letter", "Write The Upper Case", "Write the lower case", "Write your favorite"]]

# Add several letters to practice
for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    table_data.append([
        letter.upper() + " / " + letter,
    ])

table = Table(table_data, colWidths=[60, 140, 140, 140])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
elements.append(table)

# Add an encouragement note at the bottom
elements.append(Spacer(1, 24))
encouragement = Paragraph(
    "Great job practicing! Remember, every time you try, your writing muscles get stronger. Keep it up!",
    styles['Normal']
)
elements.append(encouragement)

# Build the PDF
doc.build(elements)
