#ifndef HOLBERTON_H
#define HOLBERTON_H

int wildcmp(char *s1, char *s2);

#endif /* HOLBERTON_H */

#include "holberton.h"

int wildcmp(char *s1, char *s2)
{
    if (*s1 == '\0' && *s2 == '\0')
        return (1);
    if (*s2 == '*')
    {
        if (wildcmp(s1, s2 + 1))
            return (1);
        if (*s1 != '\0' && wildcmp(s1 + 1, s2))
            return (1);
        return (0);
    }
    if (*s1 == *s2)
        return (wildcmp(s1 + 1, s2 + 1));
    return (0);
}
