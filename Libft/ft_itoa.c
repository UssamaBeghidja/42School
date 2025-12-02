#include "libft.h"

char	*ft_itoa(int n)
{
	char	*res;
	long	num;
	int		len;
	long	tmp;

	len = (n <= 0);
	num = n;
	if (n < 0)
		num = -num;
	tmp = num;
	while (tmp > 0 && len++)
		tmp /= 10;
	res = ft_calloc(len + 1, sizeof(char));
	if (!res)
		return (NULL);
	if (n == 0)
		res[0] = '0';
	while (num > 0)
	{
		res[--len] = (num % 10) + '0';
		num /= 10;
	}
	if (n < 0)
		res[0] = '-';
	return (res);
}
