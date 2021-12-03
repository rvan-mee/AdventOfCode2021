#include "solver_day_01.h"

int	ft_isspace(int c)
{
	if (c == '\t' || c == '\v' || c == '\f'
		|| c == '\r' || c == '\n' || c == ' ')
		return (1);
	else
		return (0);
}
