#include "libft.h"

void    *ft_memcpy(void *dest, const void *src, size_t n)
{
	dest--;
	src--;
        while (n-- > 0)
                *(unsigned char*)&*++dest = *(const unsigned char*)&*++src;
        return (dest);
}
/*
int     main(void)
{
        char dest[] = "locura";
        char src[] = "nose";
        ft_memcpy(dest, src , 5);
        printf("%s", dest);
        return (0);
}
*/
