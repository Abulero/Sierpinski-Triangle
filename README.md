# SierpinskiTriangle
Here's a cool thought exercise:

Let's think of a triangle and name its vertices V1, V2 and V3.

![Sierpinski](/resources/Triangle1.bmp)

Pick a random vertex, say, V2 and put a dot on it.

![Sierpinski](/resources/Triangle2.bmp)

After that, randomize another vertex, say, V3, and put another dot halfway between dot 1 and V3.

![Sierpinski](/resources/Triangle3.bmp)

After that, we'll continue to add dots, randomizing the target vertex of the movement. Always going halfway.
For example, now to V1:

![Sierpinski](/resources/Triangle4.bmp)

After performing many more movements, the result would be:


![Sierpinski](/resources/Triangle5.bmp)

I think that's enough. The question is:

What would happen if we added 100, 1000 or even 1000000 more dots?

The result is pretty interesting, but for that we'll need some computer power. Just clone the .py file and execute it using:

```
python SierpinskiTriangle.py [IMAGE SIZE] [NUMBER OF DOTS]
```

Where [IMAGE SIZE] is the size of the square image generated in pixels and [NUMBER OF DOTS] is the number of dots to be added. For good measure, the following yields good results:

```
python SierpinskiTriangle.py 2000 1000000
```

I'll not spoil the results. And if you are interested in understanding what it all means, check out this page on wikipedia:

https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
