#include "solver_day_01.h"

int	main()
{
	static int	input[2000];
	int			i = 0;
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
	i = 0;
	while (input[i])
	{
		if (input[i] > input[i - 1] && i != 0)
			count++;
		i++;
	}
	printf("amount of increases: %d\n", count);
	close(fd);
	return (0);
}
