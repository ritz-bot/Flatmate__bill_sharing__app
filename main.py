from flat import Bill, Flatmate
from pdfgenerator import PdfReport

amount = float(input("Hey User, Enter the Bill amount: "))
period= input("Duration of satay in house: ")
bill= Bill(amount, period)
name_1= input("what is first flatmate name?")
days_in_house1=int(input(f"How many days did the {name_1} stayed in the house?"))
name_2= input("what is second flatmate name?")
days_in_house2=int(input(f"How many days did the {name_2} stayed in the house?"))

flatmate1= Flatmate(name_1, days_in_house1)
flatmate2= Flatmate(name_2, days_in_house2)


print(f"{name_1} $",flatmate1.pays(bill, flatmate2))#bill is an instance of object class
print(f"{name_2}pays $", flatmate2.pays(bill,flatmate1))

pdf_report = PdfReport(filename=f"{bill.period}.pdf")
pdf_report.generate(flatmate1,flatmate2,bill=bill)
#classes should be open for extention but closed for notification

file_sharer=FileSharer()

