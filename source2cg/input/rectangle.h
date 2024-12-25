// rectangle.h
#ifndef RECTANGLE_H
#define RECTANGLE_H

#include "shape.h"

// 矩形结构体
typedef struct {
    Shape shape; // 继承形状
    double length;
    double width;
} Rectangle;

// 初始化矩形
void init_rectangle(Rectangle *rectangle, double length, double width);

// 计算矩形的面积
double calculate_rectangle_area(Rectangle *rectangle);

// 计算矩形的周长
double calculate_rectangle_perimeter(Rectangle *rectangle);

#endif // RECTANGLE_H
