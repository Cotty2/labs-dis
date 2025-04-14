# Универсум - {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# структура данных "множество как двоичный вектор"
A_bin = [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]

# структура данных "множество как список значений"
A = [1, 2, 4, 6, 9]

# преобразует множество из одного представления в другое -
#  двоичный вектор в список
def SET_convert_bin_to_list(M_bin):
    assert(len(M_bin) == 10)
    M_list = []
    for i in range(0, 10):
        if M_bin[i]:
            M_list.append(i)
    return M_list

# преобразует множество из одного представления в другое -
#  список в двоичный вектор
def SET_convert_list_to_bin(M_list):
    M_bin = [0] * 10
    for elem in M_list:
        M_bin[elem] = 1
    return M_bin

# возвращает объединение двух множеств, представленных
#  в виде двоичных векторов
def SET_bin_union(A, B):
    return [a or b for a, b in zip(A, B)]

# возвращает пересечение двух множеств, представленных
#  в виде двоичных векторов
def SET_bin_intersection(A, B):
    return [a and b for a, b in zip(A, B)]

# возвращает разность двух множеств, представленных
#  в виде двоичных векторов
def SET_bin_difference(A, B):
    return [a and not b for a, b in zip(A, B)]

# возвращает симметрическую разность двух множеств, представленных
#  в виде двоичных векторов
def SET_bin_symm_difference(A, B):
    return [a != b for a, b in zip(A, B)]

def SET_bin_complement(A):
    return [not a for a in A]

def test_set_operations(A_list, B_list):
    A_bin = SET_convert_list_to_bin(A_list)
    B_bin = SET_convert_list_to_bin(B_list)
    print("Множества:", SET_convert_bin_to_list(A_bin), SET_convert_bin_to_list(B_bin)) 
    print("Объединение:", SET_convert_bin_to_list(SET_bin_union(A_bin, B_bin)))
    print("Пересечение:", SET_convert_bin_to_list(SET_bin_intersection(A_bin, B_bin)))
    print("Разность:", SET_convert_bin_to_list(SET_bin_difference(A_bin, B_bin)))
    print("Симметрическая разность:", SET_convert_bin_to_list(SET_bin_symm_difference(A_bin, B_bin)))
    print("Дополнение:", SET_convert_bin_to_list(SET_bin_complement(A_bin)))

print(SET_convert_bin_to_list(A_bin))
print(SET_convert_list_to_bin(A))

# тестирование
A = [4, 5, 3, 1, 9]
B = [1, 2, 3, 4, 5]
test_set_operations(A, B)


A = [0, 1, 2]  # Книги по математике
B = [3, 4]     # Книги по информатике
C = [5, 6]     # Книги по физике
Old = [0, 1, 5]  # Старые книги
D = [2, 3, 6]    # Новые книги
print('\n')

man_choice = SET_bin_union(
    SET_bin_intersection(SET_convert_list_to_bin(A), SET_convert_list_to_bin(Old)),
    SET_bin_intersection(SET_convert_list_to_bin(C), SET_convert_list_to_bin(Old))
)
print("Выбор парня:", SET_convert_bin_to_list(man_choice))  

woman_choice = SET_bin_intersection(SET_convert_list_to_bin(B), SET_convert_list_to_bin(D))
print("Выбор девушки:", SET_convert_bin_to_list(woman_choice))  

X = SET_convert_bin_to_list(man_choice)
Y = SET_convert_bin_to_list(woman_choice)
cartesian_product = [(x, y) for x in X for y in Y]
print("Декартово произведение:", cartesian_product) 

from itertools import combinations
E = [0, 1]
powerset = [list(combinations(E, i)) for i in range(len(E) + 1)]
powerset = [item for sublist in powerset for item in sublist]
print("Булеан E:", powerset)        


print('\n')

R = [('Иванов', 'chiken burger'), ('Петров', 'pelmenes')]
S = [('chiken burger', 'kartoshka'), ('pelmenes', 'varenikes')]


R_S = []
for student, dish in R:
    for dish_s, product in S:
        if dish == dish_s:
            R_S.append((student, product))

print("Суперпозиция R ∘ S:", R_S)


def check_relation_properties(relation, domain, codomain):
    # Всюду определенность
    students = {pair[0] for pair in relation}
    is_total = all(student in students for student in domain)
    
    # Функциональность
    student_to_dishes = {}
    for student, dish in relation:
        student_to_dishes.setdefault(student, set()).add(dish)
    is_functional = all(len(dishes) <= 1 for dishes in student_to_dishes.values())
    
    # Сюръективность
    dishes_in_relation = {pair[1] for pair in relation}
    is_surjective = all(dish in dishes_in_relation for dish in codomain)
    
    # Инъективность
    dish_to_students = {}
    for student, dish in relation:
        dish_to_students.setdefault(dish, set()).add(student)
    is_injective = all(len(students) <= 1 for students in dish_to_students.values())
    
    return {
        'Всюду определенность': is_total,
        'Функциональность': is_functional,
        'Сюръективность': is_surjective,
        'Инъективность': is_injective,
        'Биективность': is_surjective and is_injective
    }


students = ['Иванов', 'Петров']
dishes = ['chiken burger', 'pelmenes']
products = ['kartoshka', 'varenikes']

print("Свойства R:", check_relation_properties(R, students, dishes))
print("Свойства S:", check_relation_properties(S, dishes, products))