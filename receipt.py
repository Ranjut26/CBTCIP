from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def create_receipt(transaction):
    """
    Generates a PDF receipt for a transaction.
    
    :param transaction: A dictionary containing transaction details.
                        Required keys: 'date', 'customer_id', 'customer_name', 'items', 'total'
    """
    # Create a canvas
    file_name = f"receipt_{transaction['date'].replace('/', '-')}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Define margins
    margin = 0.75 * inch
    usable_width = width - 2 * margin

    # Draw header
    draw_header(c, transaction, margin, height - margin, usable_width)

    # Draw items table
    draw_items_table(c, transaction, margin, height - margin - 1.5 * inch, usable_width)

    # Draw footer
    draw_footer(c, transaction, margin, margin, usable_width)

    # Save the PDF
    c.showPage()
    c.save()
    print(f"Receipt generated successfully: {file_name}")

def draw_header(c, transaction, x, y, width):
    """Draws the receipt header."""
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.blue)
    c.drawCentredString(x + width / 2, y, "Star Stationeries")

    # Subtitle
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 14)
    y -= 0.4 * inch
    c.drawCentredString(x + width / 2, y, "Payment Receipt")

    # Transaction date, customer ID, and customer name
    c.setFont("Helvetica-Bold", 12)
    y -= 0.5 * inch
    c.drawString(x, y, "Date:")
    c.setFont("Helvetica", 12)
    c.drawString(x + 50, y, transaction['date'])
    
    c.setFont("Helvetica-Bold", 12)
    y -= 0.25 * inch
    c.drawString(x, y, "Customer ID:")
    c.setFont("Helvetica", 12)
    c.drawString(x + 80, y, str(transaction['customer_id']))
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y - 0.25 * inch, "Customer:")
    c.setFont("Helvetica", 12)  # Bold font for customer name
    c.drawString(x + 70, y - 0.25 * inch, transaction['customer_name'])

def draw_items_table(c, transaction, x, y, width):
    """Draws the table of purchased items."""
    table_header_height = 0.3 * inch
    row_height = 0.25 * inch

    # Table header
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.red)
    c.drawString(x, y - 0.25 * inch, "Item")
    c.drawString(x + 3 * inch, y - 0.25 * inch, "Quantity")
    c.drawString(x + 4.5 * inch, y - 0.25 * inch, "Price (INR)")
    c.drawString(x + 6 * inch, y - 0.25 * inch, "Total (INR)")

    # Reset color to black for the table rows
    c.setFillColor(colors.black)

    # Draw a line below header
    c.setLineWidth(1)
    c.line(x, y - 0.35 * inch, x + width, y - 0.35 * inch)
    y -= table_header_height

    # Table rows
    c.setFont("Helvetica", 10)
    for item in transaction['items']:
        c.drawString(x, y - row_height, item['name'])
        c.drawString(x + 3 * inch, y - row_height, str(item['quantity']))
        c.drawString(x + 4.5 * inch, y - row_height , f"₹{item['price']:.2f}".replace(u'\u2022', ''))  # Ensure no extraneous characters
        c.drawString(x + 6 * inch, y - row_height , f"₹{item['total']:.2f}".replace(u'\u2022', ''))  # Ensure no extraneous characters
        y -= row_height * 1

    # Line before total amount
    y -= 0.1 * inch
    c.setLineWidth(1)
    c.setStrokeColor(colors.black)
    c.line(x, y, x + width, y)

    # Total amount
    c.setFont("Helvetica-Bold", 12)
    y -= 0.25 * inch
    c.drawString(x, y, f"Total: ₹{transaction['total']:.2f}".replace(u'\u2022', ''))

def draw_footer(c, transaction, x, y, width):
    """Draws the receipt footer."""
    # Thank you message
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.gray)
    c.drawCentredString(x + width / 2, y, "Thank you for choosing us! Happy shopping :)")

# Sample transaction
transaction = {
    'date': '2024/06/08',
    'customer_id': 'SS1256',
    'customer_name': 'Tara Arjun',
    'items': [
        {'name': 'Colouring Books', 'quantity': 3, 'price': 200.0, 'total': 600.0},
        {'name': 'Canvas Board', 'quantity': 1, 'price': 500.0, 'total': 500.0},
        {'name': 'Acrylic Paints', 'quantity': 2, 'price': 350.0, 'total': 700.0},
        {'name': 'Sketches', 'quantity': 4, 'price': 150.0, 'total': 600.0},
        {'name': 'Painting Brushes', 'quantity': 5, 'price': 100.0, 'total': 500.0},
        {'name': 'Palettes', 'quantity': 2, 'price': 50.0, 'total': 100.0},
        {'name': 'Stand for Pens Holding', 'quantity': 1, 'price': 150.0, 'total': 150.0},
        {'name': 'Water Holder', 'quantity': 1, 'price': 75.0, 'total': 75.0},
        {'name': 'Paper Clips', 'quantity': 10, 'price': 20.0, 'total': 200.0},
        {'name': 'Pencils', 'quantity': 12, 'price': 15.0, 'total': 180.0},
        {'name': 'Eraser', 'quantity': 5, 'price': 5.0, 'total': 25.0},
        {'name': 'Sharpener', 'quantity': 3, 'price': 10.0, 'total': 30.0},
    ],
    'total': 3660.0
}

create_receipt(transaction)