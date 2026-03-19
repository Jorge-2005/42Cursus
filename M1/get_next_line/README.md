*Este proyecto ha sido creado como parte del currículo de 42 por jovillal.*

## Descripción

**get_next_line** es un proyecto que consiste en programar una función capaz de leer una línea desde un file descriptor. 

El objetivo es crear una función que devuelva una línea leída desde un file descriptor, permitiendo leer archivos línea por línea de manera eficiente. La función debe manejar correctamente diferentes tamaños de buffer, y gestionar adecuadamente la memoria para evitar fugas.

La función retorna la línea leída (incluyendo el carácter `\n` si existe), o `NULL` si no hay más líneas que leer o si ocurre un error.

## Instrucciones

### Uso

Para utilizar `get_next_line` en tu proyecto:

1. Incluye el header en tu archivo:

include "get_next_line.h"

2. Compila tu programa junto con los archivos fuente de get_next_line:

cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c


3. Define el tamaño del buffer durante la compilación usando `-D BUFFER_SIZE=n` donde `n` es el tamaño deseado.

### Ejemplo de uso básico

```c
/*
int	main(void)
{
	int	fd;

	fd = open("text.txt", O_RDONLY);
	if (fd < 0)
		return (0);
	printf("%s", get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	printf("%s",get_next_line(fd));
	close(fd);
	return (0);
}*//*
int main(int argc, char **argv)
{
	(void)argc;
	int   fd;
    char *line;

    fd = open(argv[1], O_RDONLY);
    if (fd < 0)
        return (0);
    while ((line = get_next_line(fd)) != NULL)
    {
        printf("%s", line);
        free(line);
    }
    close(fd);
}*/
```
### Uso de IA en el Proyecto

Solo he usado la inteligencia artificial para la explicación de conceptos, como por ejemplo el uso de variables estáticas o cuándo es necesario liberar memoria, así como para ayudar a mejorar la presentación del archivo README.

