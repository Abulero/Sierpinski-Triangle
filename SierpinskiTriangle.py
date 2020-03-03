#!/usr/bin/python


from PIL import Image
import random
import sys


class Sierpinski:
	def __init__(self, size):
		self.width = size
		self.height = size

		self.image = Image.new('1', (self.width, self.height))

		self.vertex_left = (0, self.height - 1)
		self.vertex_top = (self.width//2, 0)
		self.vertex_right = (self.width - 1, self.height - 1)

		starting_vertex = random.choice((self.vertex_left, self.vertex_top, self.vertex_right))
		self.pixel(starting_vertex[0], starting_vertex[1])

	def pixel(self, x, y):
		self.image.putpixel((x, y), 1)
		self.current_position = (x, y)

	def move(self):
		target_vertex = random.choice((self.vertex_left, self.vertex_top, self.vertex_right))
		moving_distance = ((target_vertex[0] - self.current_position[0])//2, (target_vertex[1] - self.current_position[1])//2)

		next_position = (self.current_position[0] + moving_distance[0], self.current_position[1] + moving_distance[1])

		self.pixel(next_position[0], next_position[1])

	def draw_triangle(self, n):
		for i in range(n+1):
			self.move()

			percentage = ((i)/n)*100
			print(f'{i}/{n} ({percentage:.2f}%)')

		self.image.show()


if __name__ == '__main__':
	size = 0
	dots = 0

	if len(sys.argv) == 2:
		try:
			size = int(sys.argv[0])
			dots = int(sys.argv[1])
		except:
			print('Arguments invalid')
			sys.exit()
	else:
		size = 1000
		dots = 200000

	st = Sierpinski(size)
	st.draw_triangle(dots)