def check_id_num(n):
    if len(str(n)) != 18:
        return False
    var=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    var_id=['1','0','x','9','8','7','6','5','4','3','2']
    n = str(n)
    sum = 0
    for i in range(0,17):
        sum += int(n[i])*var[i]
    sum %= 11
    if (var_id[sum])==str(n[17]):
        return True
    else:
        return False

def id_num(n):
    var=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    var_id=['1','0','x','9','8','7','6','5','4','3','2']
    sum = 0
    n=n[0:17]
    for i in range(0,17):
        sum += int(n[i])*var[i]
    sum %= 11
    n=n+var_id[sum]
    return n

def numberx(frequency,_len):
    return list(str(frequency).rjust(_len,'0')) 
    
nums=input(">>:")
_nums=list(nums)
a=-1
nums_nums=[]
for i in _nums:
    a=a+1
    if i=='*':
        nums_nums.append(a)
_len=len(nums_nums)
s_nums=''
cc=0
if _len*'9'=='':
    ss=1
else:
    ss=int(_len*'9')+1
for frequency in range(ss):
    for i in range(len(nums_nums)):
        _numbrexs=numberx(frequency,_len)
        _nums[nums_nums[i]]=_numbrexs[i]
    for c in _nums:
        s_nums+=c
    if s_nums[-1:]=='&':
        s_nums=id_num(s_nums)
    else:
        if check_id_num(s_nums)==False:
            s_nums=''
            continue
    cc=cc+1
    print(s_nums)
    s_nums=''
cc=str(cc)
print("有"+cc+"种可能")

# with open("C://Users//amdin//Desktop//fff.txt","w+") as a:
#     a.write(data)