#!/usr/bin/env python
# coding=utf-8
import turtle


def draw_square():
    t = turtle.Turtle()
    t.shape('turtle')
    t.color('black')
    t.speed(2)

    for i in range(4):
        t.forward(200)
        t.right(90)


def main():
    window = turtle.Screen()
    window.bgcolor('red')

    draw_square()

    window.exitonclick()

if __name__ == '__main__':
    main()
