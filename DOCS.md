#Документация
Мы имеем 3 регистра, 0x00 обозначает новую комманду,это все что нужно покачто знать

##0x01-0x03
вставляет значение в регистр, пример
`\x01Hi`, он просто вставляет данные в регистр

##0x04
Печатает информацию первого регистра, пример
`\x01Hi\x00\x04`

##0x05
Печатает reg1 и reg2, пример
`\x01Hel\x00\x02lo\x00\x05`

##0x06
Перемещяет в формате куда/откуда, не работает с переменными, пример
`\x03Hi\x00\x0613\x00\x04`

##0x07
Выполняет операцию с reg1 и reg2, сохраняет в reg1, аргумет действие, пример
`\x015\x00\x025\x07+\x00\x04`

##0x08
если reg2 и reg3 равны, следующий код будет выполнен, укажите 0x01 аргумент для обычного if, что угодно для if not, не забудьте написать 0xff чтобы обозначить конец условия, пример
`\x025\x00\x032\x00\x08s\x00\x05\x00\xff\x00`

##0x09
Создаст пустую переменую, аргумент будет названием

##0x0a
укажет/создаст переменую со значением reg3, аргумент название

##0x0b
вставит в reg3 значение переменой, аргумент название

###пример использования переменых

`\x03Hi\x00\x0al\x00\x0b\x00\x0bl\x00\x0613\x00\x04`

##0x0c
просто ввод от пользователя, сохраняет в reg3

##0x0d
завершает программу

##0x0e
вставляет в reg3 пустой лист

##0x0f
добавляет в лист переменную значение reg3

##0x10
цикл for, аргумент название переменной, 0xff также обозначает конец

##0x11
Соеденяет reg1 reg2, сохраняет в reg1

##0x12
while True цикл

##0x13
достает из списка который в reg3, в reg2, номер это аргумент

##0x14
break для циклов

##0x15
Определяет функцию, аргумент название

##0x16
вызывает функцию, аргумент название

##0x17
импортирует библиотеку пайтон, аргумент название, библиотека должна быть в стиле генерированого кода(поддерживаться)

##0x18
Вставляет в reg3 range обьект, аргумент количество

---

# Documentation
We have 3 registers, 0x00 indicates a new command, that's all you need to know for now.

## 0x01-0x03
Inserts a value into the register, for example: `\x01Hi` simply inserts data into the register.

## 0x04
Prints the information of the first register, for example: `\x01Hi\x00\x04`.

## 0x05
Prints reg1 and reg2, for example: `\x01Hel\x00\x02lo\x00\x05`.

## 0x06
Moves data from one place to another, works with variables, for example: `\x03Hi\x00\x0613\x00\x04`.

## 0x07
Performs an operation on reg1 and reg2, stores it in reg1, argument specifies the operation, for example: `\x015\x00\x025\x07+\x00\x04`.

## 0x08
If reg2 and reg3 are equal, the next code will be executed. Use 0x01 as an argument for a regular "if", anything else for "if not". Don't forget to write 0xff to indicate the end of the condition, for example: `\x025\x00\x032\x00\x08s\x00\x05\x00\xff\x00`.

## 0x09
Creates an empty variable, the argument will be its name.

## 0x0a
Specifies or creates a variable with the value of reg3, the argument is the variable name.

## 0x0b
Inserts the value of a variable into reg3, the argument is the variable name.

### Example of using variables:

`\x03Hi\x00\x0al\x00\x0b\x00\x0bl\x00\x0613\x00\x04`.

## 0x0c
Simple user input, saves it in reg3.

## 0x0d
Ends the program.

## 0x0e
Inserts an empty list into reg3.

## 0x0f
Adds the value of reg3 to the list.

## 0x10
For loop, the argument is the variable name, 0xff also indicates the end.

## 0x11
Concatenates reg1 and reg2, saves it in reg1.

## 0x12
Infinite `while True` loop.

## 0x13
Retrieves an item from the list into reg3, the argument is the item's index.

## 0x14
break for cycles

##0x15
defines a command, arg is name

##0x16
executes the command, arg is name

##0x17
imports python liblary, arg is name, lib must be in tlanslated code by pbm style(suported)

##0x18
makes range object in reg3, arg is quantity