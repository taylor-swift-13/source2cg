// shape.h
#ifndef SHAPE_H
#define SHAPE_H

// 通用的形状结构
typedef struct {
    double area;
    double perimeter;
} Shape;

// 计算形状的周长
double calculate_perimeter(Shape *shape);

// 计算形状的面积
double calculate_area(Shape *shape);

#endif // SHAPE_H
