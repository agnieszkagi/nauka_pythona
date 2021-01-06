#! /usr/bin/python3

def calculate(a, b, operacja):
    if operacja == "+":
        return a + b
    if operacja == "-":
        return a - b
    if operacja == "*":
        return a * b
    if operacja == "/":
        return a / b
    if operacja == "^":
        return a ** b
    if operacja == "%":
        return a % b

def str_calculator(a, b, operacja):
    if operacja == 'concat':
        return a + b
    if operacja == 'incl':
        return a in b
    if operacja == 'notincl':
        return a in b
    if operacja == 'end':
        return b.endswith(a)
    if operacja == 'upper':
        return b==a.upper()
