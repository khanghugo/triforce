STAR = "*"
SPACE = " "

def draw_array(arr):
	for i in arr:
		print(i)

def draw_levels(t_height, s_height, level):
	result_level = ""
	triangle_num = ((level // s_height) + 1)
	pad_num = (t_height - triangle_num) * s_height

	result_level += SPACE * pad_num

	for i in range(triangle_num):
		result_level += draw_level(s_height, (level % s_height))
		result_level += " "

	result_level += SPACE * pad_num

	return result_level

def draw_level(height, level):
	star_num = (level * 2 + 1)
	space_num = (height - level - 1)

	return (SPACE * space_num +
			STAR * star_num +
			SPACE * space_num
			)

def _draw_triforce(t_height, s_height):
	return [draw_levels(t_height, s_height, i) for i in range(t_height * s_height)]

def draw_triforce(t_height, s_height):
	draw_array(_draw_triforce(t_height, s_height))

def draw_triforce_reversed(t_height, s_height):
	draw_array(_draw_triforce(t_height, s_height)[::-1])

def main():
	star_height = 7
	triforce_height = 7

	draw_triforce_reversed(triforce_height, star_height)

if __name__ == "__main__":
	main()