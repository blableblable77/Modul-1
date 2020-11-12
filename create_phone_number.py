def create_phone_number (x):
    list1=x[:3] # list1-list3 berfungsi untuk memisahkan variabel
    list2=x[3:6]
    list3=x[6:]
    str1=list(map(str,list1)) # berfungsi mengubah list menjadi str
    str2=list(map(str,list2))
    str3=list(map(str,list3))
    return ('"('+''.join(str1)+') ' + ''.join(str2)+'-'+''.join(str3)+'"') 

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))