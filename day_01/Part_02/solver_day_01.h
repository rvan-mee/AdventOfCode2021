/* ************************************************************************** */
/*                                                                            */
/*                                                        ::::::::            */
/*   solver_day_01.h                                    :+:    :+:            */
/*                                                     +:+                    */
/*   By: rvan-mee <rvan-mee@student.codam.nl>         +#+                     */
/*                                                   +#+                      */
/*   Created: 2021/10/28 13:09:16 by rvan-mee      #+#    #+#                 */
/*   Updated: 2021/12/01 13:08:01 by rvan-mee      ########   odam.nl         */
/*                                                                            */
/* ************************************************************************** */

#ifndef SOLVER_DAY_01_H
# define SOLVER_DAY_01_H
# include <unistd.h>
# include <stddef.h>
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <limits.h>
#include <fcntl.h>

char	*get_next_line(int fd);
int		ft_strlen(char *str);
char	*remove_till_newline(char *str);
char	*merge_str(char *src, char *buffer);
char	*strcopy(char *src, char *dst);
int		ft_strlen(char *str);
char	*ft_calloc(ssize_t len);
void	memsetzero(char *str, ssize_t len);
int		ft_atoi(const char *nptr);
int		ft_isspace(int c);
int		ft_isdigit(int c);

#endif
