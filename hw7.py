shopping_bag = {}

print('[구입]')

while True:

    item = input("상품명?")

    if item == "":

        print(">>>장바구니 보기 :",shopping_bag)
        
        break

    num = input('수량은?')

    shopping_bag[item] = num
    print(f"장바구니에 {item}가(이) {num}개 담겼습니다.")


print('[검색]')

name = input('장바구니에서 확인하고자 하는 상품은? ')

if name in shopping_bag:

    print(f"{name}은(는) {shopping_bag[name]}개 담겨있습니다.")

   

