// rectangle.c
#include "rectangle.h"
#include <stdio.h>

// 初始化矩形
void init_rectangle(Rectangle *rectangle, double length, double width) {
    rectangle->length = length;
    rectangle->width = width;
    rectangle->shape.area = length * width;  // 矩形面积公式
    rectangle->shape.perimeter = 2 * (length + width);  // 矩形周长公式
}

// 计算矩形的面积
double calculate_rectangle_area(Rectangle *rectangle) {
    return calculate_area(&rectangle->shape);  // 调用通用的面积计算函数
}

// 计算矩形的周长
double calculate_rectangle_perimeter(Rectangle *rectangle) {
    return calculate_perimeter(&rectangle->shape);  // 调用通用的周长计算函数
}
