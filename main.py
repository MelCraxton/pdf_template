from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=8)

df = pd.read_csv('topics.csv')


for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Arial', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)

    for i in range(20, 298, 10):
        pdf.line(10, i, 200, i)

    # Footer - Add breaklines (278mm)
    pdf.ln(265)
    # Set the footer for first page
    pdf.set_font(family='Arial', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R')



    for i in range(row['Pages']-1):
        pdf.add_page()
        # Footer - Add breaklines (278mm)
        pdf.ln(277)
        # Set the footer for the rest of the pages
        pdf.set_font(family='Arial', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='R')

        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)



pdf.output('output.pdf')