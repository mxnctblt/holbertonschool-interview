#ifndef SLIDE_LINE_H_
#define SLIDE_LINE_H_

#include <stdlib.h>
#include <stdio.h>

#define SLIDE_LEFT 2
#define SLIDE_RIGHT 1

int slide_line(int *line, size_t size, int direction);
int to_left(int *line, size_t size);
int to_right(int *line, size_t size);

#endif /* SLIDE_LINE_H_ */