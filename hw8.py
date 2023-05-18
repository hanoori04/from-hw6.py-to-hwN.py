shopping_bag = {}

def buy(shopping_ba):

    while True :
        product_name = input('상품명을 입력하세요: ')

        if product_name == '' :
            break

        quantity = int(input('수량을 입력하세요: '))

        shopping_bag[product_name] = quantity

        show(shopping_bag)


        # print(f"장바구니에 {product_name}가(이) {quantity}개 담겼습니다.")
        
        
    
    print('>>>>> 장바구니 보기 : ',shopping_bag)
        

def show(shopping_b):

    for product, quantity in shopping_bag.items():
        print(f"장바구니에 {product} {quantity}개가 담겼습니다.")

def find(shopping):

    while True :
        product_name = input("확인하고자 하는 상품명을 입력하세요: ")

        if product_name == '' :
            break

        if product_name in shopping_bag:
            quantity = shopping_bag[product_name]
            print(f"{product_name}는 {quantity}개 담겨있습니다.")

        else:
            print(f"장바구니에 {product_name}는 없습니다.")


buy(shopping_bag)
find(shopping_bag)





    


   

