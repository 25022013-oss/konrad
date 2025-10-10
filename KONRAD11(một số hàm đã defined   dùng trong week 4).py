'''(FUNCTION1)'''
def vesosao(n):#cái này để vẽ hexagram (W2A15)
 k=6 + (n-2)*6
 l=0
 o=2*(n-1)-2
 m=6+(n-2)*4
 if n == 1 :
   print("*")
 elif n > 1:
   for i in range(1,n,1):
    print(k*" ",i*"*   "," \n")
    k=k-2
   for i in range(3*n-2,2*n-2,-1):
    print(l*" ",i*"*   "," \n")
    l=l+2
   for i in range(2*n,3*n-1,1):
    print(o*" ",i*"*   "," \n")
    o=o-2
   for i in range(n-1,0,-1):
    print(m*" ",i*"*   "," \n")
    m=m+2


'''(FUNCTION2)'''
from math import sqrt
def checkSoNguyenTo(n):#cái này để ktra số nguyên tốốốốố
  PosInt = int(n)
  cotmoc = sqrt(PosInt)//1
  if (PosInt%2==0 and PosInt!=2) or PosInt == 1:
    kq = "False"
  else:
    i = cotmoc
    while 1<=i<=cotmoc:
      if i == 1:
        kq = "True"
        break
      if PosInt % i != 0:
        i = i-1
      else :
        kq = "False"
        break
  return kq


'''(FUNCTION3)'''
def daonguocso (p):#cái này ĐẢONGƯỢCSỐ
 a = list(str(p))
 ds = []
 for i in range(len(a)-1,-1,-1):
   ds.append(a[i])
 return int("".join(ds))


'''(FUNCTION4)'''
def sochinhphuong(n):#cái này checkkkkk số cphuong
  if (sqrt(n)-(sqrt(n)//1)) > 0 :
     kq = "False"
  else:
      kq = "True"
  return kq


'''(FUNCTION5)'''
def repeatdigitscheck (p):#cái này check xem số đấy có các chữ số trùng nhau kooooo
   a = list(str(p))
   dat = 0
   for i in a:
     count = 0
     for k in a:
      if k==i: 
         count = count + 1
     if count == 1 :
       dat = dat + 1
     if dat == len(a):
       kq = "False"
     else:
       kq = "True"
   return kq


'''(FUNCTION6)'''
def Collatz(i):#cái này tính độ dài cái collatz jj đấyyyyyyyy 
    lan = 0 
    while i >0:
     if i%2!=0:
        if i == 1:#đặt đkien này vì nếu đầu vào là 1 sẽ mặc định lan = 1 theo định nghĩa , và sẽ không lặp ( nếu lặp thì kết quả sẽ sai đnghia)
         lan = lan + 1
         break
        else:
         kq = 3*i+1
         lan = lan + 1        
         i = kq
     else:
       kq = i/2#bước cuối để về 1 luôn phải : 2 , vì vậy khối lệnh tính toán phải ở trên đkien kq = 1
       lan = lan + 1
       if kq == 1:
        lan = lan + 1
        break
       else:
         i = kq    
    return lan


'''(FUNCTION7)'''
def maxof(ds):#tham số phải là list #cái này tính max của list thôi chứ mấy kiểu khác ko chs đc
#có thể dùng ds = [*.....] , dấu sao là để biến các số int (sau khi ép kiểu map ) thành list 
 max = ds[0]
 for i in range(1,len(ds),1):
  if ds[i]>max:
     max = ds[i]
 return max


'''(FUNCTION8)'''
def demUocChan(n):#đếm ước chẵn , như cái tênnn
  count = 0
  if n % 2 != 0:
    count = 0
  elif n % 2 ==0:
    for i in range(2,n+1,2):
      if n % i == 0:
        count = count + 1
  return count


'''(FUNCTION9)'''
def tinhtien (n,m):#tính tiềnnnnnn
  count = 0
  if m == 0:
    tien = n
  else:
   while n > 0 and m > 0:
    tien = n + n*7*10**(-3)
    count = count + 1
    if count == m:
     break
    else:
      n = tien
  TIEN = int(tien//1)
  return TIEN


'''(FUNCTION10)'''
def tongUOCexceptN(n):#không tính n nha :) # TỔNG CÁC ƯỚC TRỪ CHÍNH "n"
  tong = 0
  for i in range(1,n,1):
    if n % i == 0:
      tong = tong + i
  return tong


'''(FUNCTION11)'''
def CPN(n,m):#closepairnumber - như đề bài
  if tongUOCexceptN(n)==m and tongUOCexceptN(m)==n:
    kq = "True"
  else:
    kq = "False"
  return kq


'''(FUNCTION12)'''
def UokCkungLonNkat(n,m):#UCLN hai số
  dsUOC=[]
  if n>m:
    siu=m
  if n<m:
    siu=n
  if n==m:
    siu=n
  for i in range(1,siu+1,1):
    if n % i==0 and m % i == 0:
      dsUOC.append(i)
  return maxof(dsUOC)


'''(FUNCTION13)'''
def alimalSL(con,chan):#cái này để tính số con chó ,con gà phải tragiaaaa
   count = 0
   for i in range(0,con+1,1):
      if 4*i + 2*(con-i) == chan:
         cho = i
         ga = con-i
         count = count + 1
   if count == 0:
      kq = "Invalid"
      return kq
   else:
    return f"{ga} {cho}"


'''(FUNCTION14)'''
def UokCkung(a,b):#tìm full ước chungggg
  if a>b:
    siu=b
  if a<b:
    siu=a
  if a==b:
    siu=a
  ds = []
  for i in range(1,siu+1,1):
    if a%i==0 and b%i==0:
      ds.append(i)
  return "các ước chung là : " + " , ".join(map(str, ds))
#map(str,ds) - cái này sẽ biến mỗi phần tử trong ds thành một string ","join sẽ thêm dấu " , "để ngăn cách


'''(FUNCTION15)'''
def isLUYTHUAcua2(n):#checkk lũy thừa của 2
  if n==1:
    kq = "yes"
  if n==0 or (n%2!=0 and n!=1):
    kq = "no"
  else :
    while n>1: 
     THUONG = n / 2
     if THUONG %2 == 0:
      n = THUONG
     if THUONG == 1:
      kq = "yes"
      break
     if THUONG %2 != 0 and THUONG != 1:
      kq = "no"
      break
  return kq


'''(FUNCTION16)'''
def tongchuso(n):#cái này tính tổng chữ sốốốố
 a = list(map(int,str(n)))
 tong = 0
 for i in a:
   tong = tong + i
 return tong
'''vì n nhập vào là int nên phải ép sang str rồi mới 
dùng map ép lại sang int(thì khi đó là một dãy các chữ số int 
do ko có dấu cách ), sau đó ép kiểu = list() ta đc một dsach có 
các ptu intttttt '''


'''(FUNCTION17)'''
def phanloaiDIGITS(n):
  a = list(map(int,str(n)))#thành một list các chữ số int , gthich ở trên rùiiii
  even, odd =0,0 
  for i in a:
    if i % 2==0:
      even = even + 1
    if i % 2!=0:
      odd = odd + 1
  return f"số chứ số lẻ : {odd} , số chữ số chẵn : {even}"


'''(FUNCTION18)'''
def sigmaSOTUNHIEN(n):#tìm số k sao cho dãy 1 + 2 + 3 + 4 + 5 + ... + k nhỏ hơn số n nhập vào 
 tong = 0
 if n == 1:
   kq = "Invalid"
 if n > 1: 
  for k in range(0,n,1):
    k = k + 1
    tong = tong + k
    if tong >=n:
      kq = k - 1#nếu quá n phải trừ 1 vì lỡ cộng k thêm 1 cho nó quá rồiiii
      break
 return kq


'''(FUNCTION19)'''
def CUOCtaxi(a):#cái này tính cước taxi 
  if a == 1:
    cost = 9
  if 2<=a<=5:
    cost = 9 + (a-1)*5
  if 6<=a<=19:
    cost = 9 + 15 + (a-5)*3
  if a>=20:
    cost = 9 + 15 + 39 + (a-19)*2
  return f"Số tiền cước là : {cost}"

  
'''(FUNCTION20)'''
def agiftfromFIBONACCI(A):#1 món quà từ fibonacci :)) coi như tìm số fibonnacci gần với A nhất mà ko vượt quá A
  i=1
  k=1
  while i > 0:
    next = i + k 
    k = i
    i = next
    if next > A: 
     kq = k
     break
  return kq


'''(FUNCTION21)'''
def XOAblanksINFRONT(a):#xóa full blank đằng trc
  p = list(map(str,str(a)))
  while p[0]== " " :
    p.remove(p[0])
  return "".join(p)#từ ["..",".."......] sang ................


'''(FUNCTION22)'''
def XOAblanksBEHIND(a):#xóa full blank đằng sau
  DScuoi = []
  DSnguoc = []
  p = list(map(str,str(a)))
  for i in range(len(p)-1,-1,-1):
    DSnguoc.append(a[i])
  while DSnguoc[0] == " ":
    DSnguoc.remove(DSnguoc[0])
  for i in range(len(DSnguoc)-1,-1,-1):
    DScuoi.append(DSnguoc[i])
  return "".join(DScuoi)

 
'''(FUNCTION23)'''
def minof(ds):#tính min , ko khác max nhiều 
   min = ds[0]
   for i in range(1,len(ds),1):
    if ds[i]<min:
     min = ds[i]
   return min


'''(FUNCTION24)'''
def checkINHOA(A):#ktra xem có phải chữ in hoa koooooo
  if A != A.lower():
    kq = True
  if A == A.lower():
    kq = False
  return kq




  

  




     
         

          
