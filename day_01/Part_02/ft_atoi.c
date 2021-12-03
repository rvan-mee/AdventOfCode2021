#include "solver_day_01.h"

int	ft_atoi(const char *nptr)
{
	int	c;
	int	value;

	c = 0;
	value = 1;
	while (*nptr != '\0' && ft_isspace(*nptr))
		nptr++;
	if (*nptr == '-' || *nptr == '+')
	{
		if (*nptr == '-')
			value *= -1;
		nptr++;
	}
	while (ft_isdigit(*nptr))
	{
		c *= 10;
		c += *nptr - 48;
		nptr++;
	}
	return ((int) c * value);
}
