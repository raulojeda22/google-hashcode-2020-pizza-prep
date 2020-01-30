#!/usr/bin/python3.6
from datetime import time, datetime

class Pizzas():
    def __init__(self, maxSlices, types, data, file):
        self.maxSlices = maxSlices
        self.types = types
        self.data = list(map(int, data[0]))
        self.slices = []
        self.niceSlices = []
        self.total = 0
        self.niceTotal = 0
        self.file = file

    def calculateSlices(self):
        count = 1
        while self.maxSlices > self.niceTotal and count < len(self.data):
            for i in range(len(self.data) - count, -1, -1):
                if self.total + self.data[i] <= self.maxSlices:
                    self.total += self.data[i]
                    self.slices.append(i)
            if self.niceTotal <= self.total:
                self.niceSlices = self.slices
                self.niceTotal = self.total
            self.total = 0
            self.slices = []
            count += 1

    def refineSlices(self):
        self.slices = self.niceSlices
        self.total = self.niceTotal
        while self.maxSlices > self.niceTotal and len(self.slices) > 0 and self.types > 10:
            startPoint = self.slices[-1] - 1
            self.slices.pop()
            savedSlices = self.slices
            self.total = 0
            for i in self.niceSlices:
                self.total += self.data[i]
            for i in range(startPoint, -1, -1):
                if self.total + self.data[i] <= self.maxSlices:
                    self.total += self.data[i]
                    self.slices.append(i)
            if self.niceTotal <= self.total:
                self.niceSlices = self.slices
                self.niceTotal = self.total
            self.slices = savedSlices

    def getExactTotal(self):
        total = 0
        for i in self.niceSlices:
            total += self.data[i]
        return total

    def output(self):
        slices = self.slices[::-1]
        r = open("outputs/" + file +".out", "a")
        r.write(str(len(slices)))
        r.write('\n')
        r.write(' '.join(str(e) for e in slices))
        r.close()


def getPizzasFromFile(file):
    f = open(file + ".in", 'r')
    data = []
    for row in f.readlines():
        data.append(row.replace("\n", "").split(" "))
    f.close()
    rules = data.pop(0)
    pizza = Pizzas(int(rules[0]), int(rules[1]), data, file)
    return pizza

files = ['a_example', 'b_small', 'c_medium', 'd_quite_big', 'e_also_big']
for file in files:
    pizzas = getPizzasFromFile(file)
    pizzas.calculateSlices()
    pizzas.refineSlices()
    print(pizzas.getExactTotal())
    pizzas.output()
