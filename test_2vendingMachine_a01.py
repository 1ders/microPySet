product_price = int(input('product :'))
insert_price = int(input('insert :'))
insert_more = 0

payment_slot = {
    50000 : 1,
    10000 : 2,
    5000 : 3,
    1000 : 4,
    500 : 5,
    100 : 6,
    50 : 7,
    10 : 8
}

for pay_unit, pay_slot in payment_slot.items():
    insert_more = insert_more+ pay_unit*pay_slot

print('잔돈'+str(insert_more)+'원까지 환불가능')

while product_price - insert_price > 0 :
    print('돈 더 필요해. 안 살라면 enter 눌러')
    insert_more = input('insert more : ')

    if not insert_more or int(insert_more) < 0 :
        print('구입의사가 없으신 것으로 판단하였습니다.')
        print(str(insert_price) + ' 입력한 모든 돈 반환했어요')
        break
    else :
        insert_price = insert_price + int(insert_more)


change = int(insert_price) - int(product_price)
print(str(change)+'원을 반환합니다.')


for pay_unit, pay_slot in payment_slot.items():
    if change - pay_unit < 0 :
        print(str(pay_unit) + ' : ' + str(0)) 
    else:
        unitN,slotN = divmod(change, pay_unit)
        
        
        if pay_slot-unitN < 0 :
            print(str(pay_unit)+' : '+ str(unitN-pay_slot)+'장 지폐 부족')
            payment_slot[pay_unit] = 0
            print(str(pay_unit) + ' : ' + str(pay_slot)) 
            change = change - pay_unit*pay_slot
            continue
        else:
            change = slotN
    
        payment_slot[pay_unit] = pay_slot-unitN
        print(str(pay_unit) + ' : ' + str(unitN)) 


for pay_unit, pay_slot in payment_slot.items():
    sum = + pay_unit*pay_slot
    print(str(pay_unit) + ' : ' + str(pay_slot))