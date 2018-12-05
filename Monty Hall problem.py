'''
TODO: Monty Hall problem = The car-goat problem
'''
import random
#Đầu tiên giả sử 3 cánh cửa được đánh số 1,2 và 3. Trong đó 1 cánh cửa dẫn đến cơ hội sở hữu Lamborghini của chúng ta.
prizeDoor = random.randint(1,3)
#Khởi đầu game show, mình sẽ chọn 1 trong 3 cánh cửa một cách ngẫu nhiên
chooseDoor = random.randint(1,3)
'''
Tiếp theo là phần thú vị, Monty bước lên và nhẹ nhàng mở 1 trong 2 cánh cửa còn lại, và đằng sau đó là chú dê thần thánh. Để giả lập sự kiện này cần 1 vòng while loop vô hạn, bắt máy tính chọn đến khi nào thoả mãn 2 điều kiện:

- Cánh cửa mở ra không phải là cánh cửa dẫn đến Lamborghini
- Cánh cửa mở ra không phải là cánh cửa mình chọn ban đầu.
'''

while 1:
  openDoor = random.randint(1,3)
  if (openDoor != prizeDoor) and (openDoor != chooseDoor):
    break

'''
Bây giờ đến thời khắc quyết định: mình có cơ hội chọn lại cánh cửa mới hoặc giữ nguyên lựa chọn ban đầu. Để giả lập hành động chọn lại mình sẽ dùng 1 vòng while vô hạn nữa, cánh cửa chọn lại cũng thoả mãn 2 điều kiện

- Cảnh cửa chọn lại không phải là cánh cửa Monty vừa mở ra
- Cánh cửa chọn lại không phải là cánh cửa ban đầu đã chọn.
'''
while 1:
  changeMind = random.randint(1,3)
  if (changeMind != openDoor) and (changeMind != chooseDoor):
    break
'''
Và cuối cùng là màn đo kết quả. Không giống như đời thật, mình có thể "chơi thử" 1000 lần và xem liệu quyết định thay đổi lựa chọn 
có xác suất đổi đời cao hơn quyết định ban đầu hay không.

'''

originalChance = 0
changeMindChance = 0

for i in range(1000):
  # ... Game show code
  if chooseDoor == prizeDoor:
    originalChance+=1
  if changeMind == prizeDoor:
    changeMindChance+=1

print(originalChance)
print(changeMindChance)
# 311 <- OriginalChange
# 689 <- changeMindChance

for i in range(1000):
  prizeDoor = random.randint(1,3)
  chooseDoor = random.randint(1,3)
  if chooseDoor == prizeDoor:
    originalChance+=1
  else:
    changeMindChance+=1