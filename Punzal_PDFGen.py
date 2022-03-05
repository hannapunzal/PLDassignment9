#PDF Resume Creator
	#Create a python program that will create your personal resume in PDF format
	#All personal details are stored in a JSON file
	#Your program should read the JSON file and write the details in the PDF
	#The output file should be: LASTNAME_FIRSTNAME.pdf

#Note:
	#Search for available PDF library that you can use
	#Search how data is structured using JSON format
	#Search how to read JSON file
	#You will create the JSON file manually
	#Your code should be in github before Feb12

from tokenize import Name; from fpdf import FPDF; import json

Name = "Hannafaith B. Punzal"
Address = "Phase 1, Dela Costa 3,"
Address2 =" Brgy. Graceville, SJDM, Bulacan"
Contact = "9957382047"
Email = "hannapunzal123@gmail.com"


class PDF(FPDF):
    def header(self):


        self.set_font('Times', 'B', 30)



pdf = PDF('P', 'mm', "A4")

pdf.add_page()

pdf.image("pic.jpg", 15, 15, 50, 0)

pdf.set_font('Times', 'B', 30)
pdf.set_text_color(0, 30, 47)
w = pdf.get_string_width(Name) + 6
pdf.set_x((255 - w) / 2)
pdf.ln(7)
pdf.cell(0, 20, f"{Name}", align='R', ln=1)
pdf.set_font('Times', 'B', 15)
pdf.cell(0, 6, f"{Address}", align='R', ln=1)
pdf.cell(0, 6, f"{Address2}", align='R', ln=1)
pdf.cell(0, 6, f"{Contact}", align='R', ln=1)
pdf.cell(0, 6, f"{Email}", align='R', ln=1)
pdf.ln(10)

fh = open('Resume.json', 'r')
jh = fh.read()
info = json.loads(jh)

for information in info:
    pdf.ln(5)
    pdf.set_font('Times', 'BI', 18)
    pdf.set_text_color(0, 30, 47)
    pdf.cell(0, 10, f"{information['Header1']}", 'BI', ln=1)
    pdf.ln(8)
    pdf.set_font('Times', '', 12)
    pdf.set_text_color(0, 30, 47)
    pdf.cell(10, 5, f"{information['Obj']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Obj1']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Obj2']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Obj3']}", align='L', ln=1)
    pdf.ln(10)

    pdf.set_font('Times', 'BI', 18)
    pdf.set_text_color(0, 30, 47)
    pdf.cell(0, 10, f"{information['Header2']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', 'B', 14)
    pdf.set_text_color(0, 30, 47)
    pdf.cell(0, 5, "    Tertiary             :  ", align='L')
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 5, f"{information['Tertiary']}", align='R', ln=1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['Tertiary Address']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['Tertiary Year']}", align='R', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 5, "    Secondary        :  ", align='L')
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 5, f"{information['Secondary']}", align='R', ln=1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['Secondary Address']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['Secondary Address2']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['Secondary Year']}", align='R', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 5, "    Primary             :  ", align='L')
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 5, f"{information['Primary']}", align='R', ln=1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, f"{information['Primary Address']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['Primary Address2']}", align='R', ln=1)
    pdf.cell(0, 5, f"{information['Primary Year']}", align='R', ln=1)
    pdf.ln(5)

    pdf.set_font('Times', 'BI', 18)
    pdf.set_text_color(0, 30, 47)
    pdf.cell(0, 10, f"{information['Header3']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', '', 14)
    pdf.set_text_color(0, 30, 47)
    pdf.cell(0, 5, f"{information['Skill1']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill2']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill3']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill4']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill5']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill6']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill7']}", align='L', ln=1)
    pdf.ln(20)

    pdf.set_font('Times', 'BI', 18)
    pdf.set_text_color(0, 30, 47)
    pdf.cell(0, 10, f"{information['Header33']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', '', 14)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 5, f"{information['Skill11']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill22']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill33']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill44']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill55']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill66']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Skill77']}", align='L', ln=1)
    pdf.ln(5)

    pdf.set_font('Times', 'BI', 18)
    pdf.set_text_color(0, 30, 47)
    pdf.cell(0, 10, f"{information['Header4']}", 'BI', ln=1)
    pdf.ln(3)
    pdf.set_font('Times', '', 12)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 5, f"{information['Achievement1']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Achievement11']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Achievement111']}", align='L', ln=1)

    pdf.ln(5)

    pdf.cell(0, 5, f"{information['Achievement2']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Achievement22']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Achievement222']}", align='L', ln=1)
    pdf.ln(5)

    pdf.cell(0, 5, f"{information['Achievement3']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Achievement33']}", align='L', ln=1)
    pdf.ln(5)

    pdf.cell(0, 5, f"{information['Achievement4']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Achievement44']}", align='L', ln=1)
    pdf.ln(5)

    pdf.cell(0, 5, f"{information['Achievement5']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Achievement55']}", align='L', ln=1)
    pdf.ln(5)


    pdf.cell(0, 5, f"{information['Achievement6']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Achievement66']}", align='L', ln=1)
    pdf.ln(5)

    pdf.cell(0, 5, f"{information['Achievement7']}", align='L', ln=1)
    pdf.cell(0, 5, f"{information['Achievement77']}", align='L', ln=1)
    pdf.ln(5)




    pdf.output('PUNZAL_HANNAFAITH.pdf')