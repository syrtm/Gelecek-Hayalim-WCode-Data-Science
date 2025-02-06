note = 50

if note >= 50:
    print("Geçtiniz")

if note == 50:
    print("Sınırdan geçtiniz.")

else:
    print("Kaldınız")

students = ["Merve","Şeyda","Şüheda","Ece"]


for student in students:
    if student == "Suheda":
        break
    print (student)
else:
    print("1.for loopu bitti.")
print("********")

for student in students:
    if student == "Suheda":
        continue
    print (student)
else:
    print("2.for loopu bitti.")


i=0
while i < 5:
    print(i)
    i += 1

student_name = "Selay"