#!/usr/bin/env python
# coding=utf-8
import turtle


def draw_square(t):

    for i in range(3):
        t.forward(200)
        t.left(60) if i % 2 == 0 else t.left(120)


def main():
    window = turtle.Screen()
    window.bgcolor('white')

    t = turtle.Turtle()
    t.shape('turtle')
    t.color('red')
    t.speed(6)

    for i in range(37):
        t.right(10)
        draw_square(t)

    t.left(40)
    t.forward(400)

    window.exitonclick()

if __name__ == '__main__':
    main()
