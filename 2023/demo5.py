amout=1757
val=[500,50,5,1,8]
notes={500:0,50:0,5:0}
remaining_amount=amout

for i in val:
    notes[i]=remaining_amount//i
    remaining_amount=remaining_amount%i
print(notes)

print(1757//500)
print(1757%500)