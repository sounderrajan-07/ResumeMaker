from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__, template_folder='templates')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_resume():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    skills = request.form['skills']
    experience = request.form['experience']
    education = request.form['education']

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Resume", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Name: {name}", ln=True)
    pdf.cell(0, 10, f"Email: {email}", ln=True)
    pdf.cell(0, 10, f"Phone: {phone}", ln=True)
    pdf.ln(10)

    pdf.multi_cell(0, 10, f"Skills:\n{skills}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Experience:\n{experience}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Education:\n{education}")

    # Save file
    output_path = os.path.join("resume.pdf")
    pdf.output(output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
