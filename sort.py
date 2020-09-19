print('hellow')
print('Welcome to git')

#Bouble sort code
def sort(list):

    for i in range(len(list)-1,0,-1):
        for j in range(i):

            if list[j] > list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]


list=[4,2,7,1,5]

sort(list)

print(list)
