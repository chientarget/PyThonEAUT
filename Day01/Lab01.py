import math

print('            **            **    **   **    ********     ****               **     **        **    **       **    **              **                                                       ')
print('        **        **      **    **   **    **           *******            **     **        **    **       **      **          **                                                                      ')
print('    **                    **    **   **    **           **     **          **     **        **    **       **        **       **                                                                  ')
print('   **                     **    **   **    **           **       **        **     **        **    **       **          **    **                                                                     ')
print('   **                     ********   **    ********     **         **      **     ************    **       **            **                                                                                 ')
print('   **                     ********   **    ********     **           **    **     ************    **       **             **                                                                      ')
print('   **                     **    **   **    **           **             **  **     **        **    **       **             **                                                                                                ')
print('      **      **          **    **   **    **           **               ****     **        **     **      **             **                                                                    ')
print('          **              **    **   **    ********     **                 **     **        **         **                 ***                                                   ')



a = int(input('Nhập giá trị cho a: '))
b = int(input('Nhập giá trị cho b: '))

# Calculate and print the results
print(f'Tổng a + b = {a + b}')
print(f'Hiêụ a - b = {a - b}')
print(f'Tích a * b = {a * b}')
print(f'Thương a / b = {a / b}')

a = float(input('Nhập vào cạnh a: '))
b = float(input('Nhập vào cạnh b: '))
c = float(input('Nhập vào cạnh c: '))


chu_vi = a + b + c
print(f'Chu vi của tam giác là: {chu_vi}')

p = chu_vi / 2
dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f'Diện tích của tam giác là: {dien_tich}')



