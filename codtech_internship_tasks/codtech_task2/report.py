from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import pandas as pd

def generate_pdf():
    # PDF create
    pdf = canvas.Canvas("Report.pdf", pagesize=A4)

    # Read CSV data
    data = pd.read_csv("data.csv")

    # Basic stats
    avg_score = data["Score"].mean()
    max_score = data["Score"].max()
    min_score = data["Score"].min()

    # Title
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(100, 800, "Student Score Report")

    # Content
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 770, f"Average Score: {avg_score:.2f}")
    pdf.drawString(100, 750, f"Highest Score: {max_score}")
    pdf.drawString(100, 730, f"Lowest Score: {min_score}")

    pdf.drawString(100, 700, "Detailed List:")

    # Listing all students with scores
    y_position = 670
    for index, row in data.iterrows():
        pdf.drawString(120, y_position, f"{row['Name']} — {row['Score']}")
        y_position -= 20

    # Save PDF
    pdf.save()
    print("PDF Generated Successfully!")

# Run function
generate_pdf()