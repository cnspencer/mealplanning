
import food


def main(ls):
	get = True
	while get:
		count = 1
		for foo in ls:
			print(f"{count}. {foo}")
			count += 1
		print(f"{count}. Go back")
		op = input()
		if op.isdigit():
			if int(op) < count:
				ls.remove(ls[int(op) - 1])
			elif int(op) == count:  # exit
				get = False
		else:
			print("invalid input")
