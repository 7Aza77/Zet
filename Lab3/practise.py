from functions1 import getc, solve , histogram

fr = int(input('Enter temperature: '))
print(getc(fr))


nh = int(input('Enter numheads: '))
nl = int(input('Enter numlegs: '))
ch,rb  = solve(nh, nl)
print(f'chickens: {ch}, rabbits: {rb}')


gist = input('Enter numbers: ')
gist = gist.split()
gist = [int(num) for num in gist]
histogram(gist)