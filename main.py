product = []
product_and_number = []
how_many = []
while True:

    print("")
    option = input(
        "1.Maxsulot qo'shish:\n2.Maxsulotni yangilash:\n3.Maxsulot soni:\n4.Qolmagan maxsulotlarni korsatish:\n5.Tugatish:\n"
    )

    if option == "1":

        name_of_product = input("Maxsulot nomini kiriting:\n")
        img = name_of_product.upper()
        if img in product:
            print(f"siz {name_of_product} ni royxatga olgansiz!!!")
        else:
            number_of_product = input("Maxsulot sonini kiriting:\n")
            product.append(img)
            product_and_number.append(
                {"Maxsulot nomi:": name_of_product, "Maxsulot soni:": number_of_product}
            )
            how_many.append(number_of_product)
            print(name_of_product, " Royxatga olindi!")

    elif option == "2":

        if len(product) > 0:
            name_of_product = input("Maxsulot nomini kiriting:\n")
            img = name_of_product.upper()
            if img in product:
                option_1 = input(
                    "1.Maxsulotni olib tashlash:\n2.Maxsulot sonini o'zgartirish:\n"
                )
                if option_1 == "1":
                    for index in range(0, len(product) - 1):
                        if product[index] == img:
                            how_many.pop(index)
                            product.remove(img)
                            print(f"{img} olib tashlandi!")
                elif option_1 == "2":
                    number = input(f"{name_of_product} ni yangi sonini kiriting:")
                    for index in range(0, len(product) - 1):
                        if product[index] == name_of_product:
                            how_many[index] = number
                            print(name_of_product, " soni o'zgartirildi")
            else:
                print("Bunday maxsulot yoq!")
        else:
            print("Hali maxsulot mavjud emas!!!")

    elif option == "3":

        if len(product) > 0:
            for number in range(len(product)):
                print(product[number], ":", how_many[number])
        else:
            print("Hali maxsulot mavjud emas!!!")

    elif option == "4":

        counter = 0
        for a in range(0, len(how_many)):
            if how_many[a] == "0":
                counter += 1
                print(product[a], ":", how_many[a])
        if counter == 0:
            print("Tugagan maxsulotlar mavjud emas!!!")
    elif option == "5":
        option_2 = input(
            "Agar dasturni toxtatsangiz, barcha malumotlar o'chib ketadi.Bunga rozimisiz.\n1.Ha\n2.Yoq\n"
        )
        if option_2 == "1":
            break
        elif option_2 == "2":
            continue
        else:
            print("Bunday tanlov mavjud emas!!!")
    else:
        print("Bunday tanlov mavjud emas!!!")
        continue
