import json
# if __name__== "__main__":
#     name = input("Vvedit imia uchnya ")
#     age = input("Vvedit vik uchnya ")
#
#     frame_student = {
#         "id": id,
#         "title": title
#    }
#
#     with open("students_data.json", "r") as file:
#         students = json.load(file)
#         students.append(frame_student)
#
#     with open("students_data.json", "w") as f:
#         json.dump(students, f)

#
# if __name__ == "__main__":
#      with open("products.json", "r") as file:
#         products = json.load(file)

     # max_price = 0
     # for product in products:
     #    if product['price'] > max_price:
     #        max_price = product['price']
     #
     # print(max_price)
        # print(products)
     #
     # min_price = 999999999999
     # for product in products:
     #     if product['price'] < min_price:
     #         min_price = product['price']
     #
     # print(min_price)

# import json
# if __name__== "__main__":
#     id = input("Введіть ID товару: ")
#     title = input("Введіть title товару: ")
#     price = input("Введіть price товару: ")
#     rate = input("Введіть rate товару: ")
#
#     frame_product = {
#         "id": id,
#         "title": title,
#         "price" : price,
#         "rate" : rate
#     }
#
#     with open("products.json", "r") as file:
#          products = json.load(file)
#          products.append(frame_product)
#
#     with open("products_DATA.json", "w") as f:
#         json.dump(products, f)

import json
if __name__== "__main__":
    id = input("Введіть ID товару: ")

    frame_product = {
        "id": id,

    }

    with open("products.json", "r") as file:
         products = json.load(file)
         products.append(frame_product)