import webbrowser

from fpdf import FPDF


class PdfReport:
    #fpdf can used to generate a pdf
    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1, flatmate2, bill):

        flatmate1_pay=str(flatmate1.pays(bill=bill,flatmate2=flatmate2))
        flatmate2_pay = str(flatmate2.pays1(bill=bill,flatmate1=flatmate1))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()



        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        #insert period label and value
        pdf.set_font(family="Times",size=14,style='B')
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0, ln=1)

        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)#enough for windows, but for mac and windows, we need to do changes
