# def sum(x, y)->str:
#     return x + y
# sum_result:str=sum(3,3)
# print(f'sum of two number is {sum_result}')

# def mul(x:int, y:int)->int:
#     return x + y
# mul_result:int=mul(3,3)
# print(f'multiplictaion of two number is {mul_result}')

# def get_name_with_age(name: str, age: int):
#     name_with_age = f'{name}  is this old: {age}'
#     return name_with_age
# print(get_name_with_age('ali',330))
# # Those internal types in the square brackets are called "type parameters".
# def process_items(items: list[str]):
#     for item in items:
#         print(item)
        
        
# from typing import Union

# def process_itemsw(items_t: tuple[Union[int, str],...]):
#     return items_t

# print(process_itemsw((3, 4, 'ali')))

 

 
# binary_data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64' 
# print("Bytes:", binary_data)

# my_name:str = 'arman'
# print("Name:", repr(my_name))
try:
    result = 'hello' + 123
except TypeError as e:
    print("An error occurred:", e)
    print("Repr of the error:", repr(e))
