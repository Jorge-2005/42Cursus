*This project has been created as part of the 42 curriculum by jovillal.*

## Descripción

**push_swap** es un proyecto que consiste en ordenar una lista de números enteros utilizando dos pilas y un conjunto limitado de operaciones.

El objetivo es generar la menor cantidad posible de instrucciones para ordenar los números en orden ascendente. Para ello, el programa recibe los números como argumentos y devuelve por la salida estándar las operaciones necesarias para ordenarlos.

El programa debe:
- Aceptar números como argumentos
- Detectar errores de entrada
- No permitir números duplicados
- Manejar correctamente la memoria
- Ordenar los números con el menor número de movimientos posible

Para tamaños pequeños (2, 3, 4 y 5 números) se utiliza ordenación manual, mientras que para tamaños mayores se utiliza un algoritmo basado en radix sort.

El programa imprime las operaciones necesarias para ordenar la pila `a`, utilizando la pila `b` como apoyo.

---

## Instrucciones

### Compilación
```
Para compilar el programa:

- make

Esto generará el ejecutable:

- push_swap
```
### Uso
```
Ejecuta el programa pasando números como argumentos:

./push_swap 3 2 1

También se pueden pasar entre comillas:

./push_swap "3 2 1"

El programa mostrará por pantalla las instrucciones necesarias para ordenar los números.
```

### Operaciones permitidas

```
sa  -> intercambia los dos primeros elementos de a
sb  -> intercambia los dos primeros elementos de b
ss  -> sa y sb a la vez
pa  -> mueve el primer elemento de b a a
pb  -> mueve el primer elemento de a a b
ra  -> rota a hacia arriba
rb  -> rota b hacia arriba
rr  -> ra y rb a la vez
rra -> rota a hacia abajo
rrb -> rota b hacia abajo
rrr -> rra y rrb a la vez
```

---

### Ejemplo de uso

```
./push_swap 4 2 1 3
./push_swap "4 67 3 87 23"
./push_swap 4 67 "3 87" 23

Juntandolo con el checker_linux
ARG="4 67 3 87 23"; ./push_swap $ARG | ./checker_linux $ARG
ARG=$(seq 1 100 | shuf | tr '\n' ' '); ./push_swap $ARG | ./checker_linux $ARG

Esto cuenta el numero de operaciones
./push_swap 5 4 3 2 1 | wc -l

```
Salida posible:

```
ra
pb
sa
pa
```
### Errores

El programa mostrará:

```
Error
```

Si:
- Hay caracteres inválidos
- Hay números duplicados
- Hay overflow de int
- Los argumentos no son válidos

### Funcionamiento

El programa funciona de la siguiente manera:

- Se validan los argumentos
- Se convierten a números
- Se comprueba que no haya duplicados
- Se almacenan en una lista enlazada
- Se ordenan según el tamaño:

```
2 números -> swap si es necesario
3 números -> ordenación manual
4 números -> mover mínimo a b y ordenar 3
5 números -> mover mínimo a b y ordenar 4
>5 números -> radix sort
```

## Recursos

Algunos recursos utilizados para entender el proyecto:

- Manual oficial de 42
- Explicaciones sobre listas enlazadas
- Explicaciones sobre radix sort

## Uso de IA en el Proyecto

Solo he usado la inteligencia artificial para:

- Explicación de conceptos
- Resolución de dudas sobre memoria
- Comprensión del algoritmo
- Ayuda para estructurar el README

No se ha utilizado IA para generar directamente el algoritmo principal del proyecto.
