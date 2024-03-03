iya =input("Input data VLAN baru (y/t)? ")
print(29*"=","\n")
while(iya=='y' or iya=='Y'):
    input1 = input("Masukan VLAN ID :")
    input2 = input("Masukan Nama VLAN :")
    print(29*"-","\n")
    file1 = open('vlan-database.txt', 'a')

    file1.write('VLAN ID: ' + input1 +',')
    file1.write(" ")
    file1.write('NAME: ' + input2)
    file1.write("\n")
    file1.close()
    iya =input("Input data VLAN baru (y/t)? ")

else:
        print(29*"*","\n")
        file2=open("vlan-database.txt",'r')
        print(file2.read())
    
      
