# Chương 8
#Câu 1
kingdoms = ['Bacteria', 'Protozoa', 'Chromista',
'Plantaee', 'Fungi','Animaliaa']
print("kingdoms: ", kingdoms)
#1a
print("kingdoms[0] : ", kingdoms[0])
#1b
print("kingdoms[5] : ", kingdoms[5])
#1c
print("kingdoms[:3]: ", kingdoms[:3])
#1d
print("kingdoms[2:5]: ", kingdoms[2:5])
#1e 
print("kingdoms[4:]: ", kingdoms[4:])
#1f
print("kingdoms[1:0]: ", kingdoms[1:0])
# Câu 2
#2a
print("kingdoms[-6]: ", kingdoms[-6])
#2b
print("kingdoms[-1]: ", kingdoms[-1])
#2c
print("kingdoms[-6:-3]: ", kingdoms[-6:-3])
#2d
print("kingdoms[-4:-1]: ", kingdoms[-4:-1])
#2e
print("kingdoms[-2:]: ", kingdoms[-2:])
#2f
print("kingdoms[-1:-2]: ", kingdoms[-1:-2])
print("--------/////--------")
# Câu 3 
#3 Create list of appointments:
appointments = ['9:20', '10:30', '14:00', '15:00', 
'15:30']
print(appointments)
#3a Add them 16:20 to the end of the list
appointments.append('16:30')
print(appointments)
#3b Use the + operator to add '16:30' 
appointments += ['16:30']
print(appointments)
#3c The approach in (a) modifies the list. 
#3c The one in (b) creates a new list.
print("--------/////--------")