with open('test.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        ingredient_count = int(file.readline())
        ingredient_list = []
        for _ in range(ingredient_count):
            ingredient = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ingredient
            ingredient_dictionary = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            ingredient_list.append(ingredient_dictionary)
        cook_book[dish_name] = ingredient_list
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_count = {}
    dishes_dictionary = {}
    for dish in dishes:
        for element in cook_book[dish]:
          
            if element['ingredient_name'] not in dishes_dictionary:
                ingredient_count['quantity'] = int(element['quantity']) * person_count 
                ingredient_count['measure'] = element['measure'] 
                dishes_dictionary[element['ingredient_name']] = dict.copy(ingredient_count) 
               
            else:        
                ingredient_count['measure'] = element['measure']
                ingredient_count['quantity'] = int(element['quantity']) * person_count + dishes_dictionary[element['ingredient_name']]['quantity']               
                dishes_dictionary[element['ingredient_name']] = dict.copy(ingredient_count)
    
    print(dishes_dictionary)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 7)   


file_count = {}
with open('1.txt', 'rt', encoding = 'utf-8') as file:
    count_1 = 0
    for _ in file:
        count_1 += 1
    file_count[str(count_1)] = '1.txt'

with open('2.txt', 'rt', encoding = 'utf-8') as file:
    count_2 = 0
    for _ in file:
        count_2 += 1
    file_count[str(count_2)] = '2.txt'
with open ('3.txt', 'rt', encoding= 'utf_8') as file:
    count_3 = 0
    for _ in file:
        count_3 +=1
    file_count[str(count_3)] = '3.txt'
        
file_count = dict(sorted(file_count.items(), reverse = True))
        
with open('4.txt', 'a', encoding= 'utf-8') as document:
    for x in file_count:
        document.write(f'{file_count[x]}\n')
        document.write(f'{x}\n')
        with open(f'{file_count[x]}', 'r', encoding= 'utf-8') as file:
                line = file.read()         
                document.write(f'{line}\n')
