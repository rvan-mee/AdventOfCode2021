#include "solver_day_01.h"

int	main()
{
	static int	input[2000];
	int			i = 0;
	int			a = 0;
	int			b = 0;
	int			count = 0;
	int			fd = open("input.txt", O_RDONLY);
	char		*str;

	while (1)
	{
		str = get_next_line(fd);
		if (!str)
			break;
		input[i] = ft_atoi(str);
		i++;
		free(str);
	}
	i = 2;
	a = input[i - 2] + input[i - 1] + input[i];
	i++;
	while(input[i])
	{
		b = input[i - 2] + input[i - 1] + input[i];
		if (a < b)
			count++;
		a = b;
		i++;
	}
	printf("amount of increases: %d\n", count);
	close(fd);
	return (0);
}
