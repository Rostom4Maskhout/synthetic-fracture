import os
import time
import numpy as np
from PIL import Image

# date_string = time.strftime("%m-%d-%H:%M:%S")


f = open('/home/miller/PycharmProjects/synthetic:fracture/Data 21-8-2018a/fracturedataset1/fracture1/fracture1.top.frt', 'r')
mine = ''
for line in f:
    line = line.strip()
    line = line.replace('  ', ',')    #   a method to remove spaces and make the file readable
    line = line.replace(' ', ',')
    line = line.replace(',,', ',')
    mine = mine + line + '\n'

text_file = open("Output.txt", "w")
text_file.write(mine)
text_file.close()

mylist = np.genfromtxt('Output.txt', delimiter=',')  # generate a list from the file

pic = np.asarray(mylist)  # covert list into array
b = np.zeros(2)  # number of columns
b = np.shape(pic)  # my invention to get the columns and rows
print(b)

x = 450 # displacement in x direction
y = 0  # displacement in y direction

os.mkdir('displacement' + str(x))

uppersurface = np.zeros([int(b[0]/2), b[1] ], dtype=float)  # upper surface  that will move
lowersurface = np.zeros([int(b[0]/2), b[1]], dtype=float)  # lower surface

for i in range(int(b[0]/2)):
    for g in range(b[1]):
        uppersurface[i, g] = pic[i + x, g + y]      # at different x uppersurface will read diferent sufrace
        lowersurface[i, g] = pic[i, g]
print(np.min(uppersurface))
print(np.min(lowersurface))

uppersurface = uppersurface + 1
lowersurface = lowersurface + 1

subtract = uppersurface - lowersurface
print(subtract)

print(np.min(subtract))

uppersurface = uppersurface - np.min(subtract)
aperture = uppersurface - lowersurface
print(np.min(aperture))

indices = np.where(aperture == aperture.min())
print(indices[0])

el = int(np.max(uppersurface) + np.min(lowersurface)) + 10

geometery = np.full([el+2, (b[1] - y)+2, (int(b[0]/2))+2], 2)

for g in range(int(b[0]/2)):
    photo_pix = np.zeros([el, b[1]], dtype=np.uint8)
    row = np.zeros(b[1] - y)
    row1 = np.zeros(b[1] - y)
    for i in range(b[1] - y):
        row[i] = lowersurface[g, i]
        row1[i] = uppersurface[g, i]

    for i in range(b[1] - y):
        z = int(row[i])
        z1 = int(row1[i])

        for q in range(z + 5, z1 + 5):
            photo_pix[q, i] = 255

            geometery[q+1, i+1, g+1] = 0

    img = Image.fromarray(photo_pix)
    img.save("./displacement" + str(x) + "/fracture" + str(g) + ".png")

lg = int(b[0]/2)
li = b[1] - y

for g in range(1,lg+1):
    for i in range(1,li+1):
        for q in range(1,el+1):
            if geometery[q, i, g] == 0:

                if geometery[q + 1, i, g] == 2:
                    geometery[q + 1, i, g] = 1

                if geometery[q + 1, i, g + 1] == 2:
                    geometery[q + 1, i, g + 1] = 1

                if geometery[q + 1, i, g - 1] == 2:
                    geometery[q + 1, i, g - 1] = 1

                if geometery[q + 1, i + 1, g] == 2:
                    geometery[q + 1, i + 1, g] = 1

                if geometery[q + 1, i + 1, g + 1] == 2:
                    geometery[q + 1, i + 1, g + 1] = 1

                if geometery[q + 1, i + 1, g - 1] == 2:
                    geometery[q + 1, i + 1, g - 1] = 1

                if geometery[q + 1, i - 1, g] == 2:
                    geometery[q + 1, i - 1, g] = 1

                if geometery[q + 1, i - 1, g + 1] == 2:
                    geometery[q + 1, i - 1, g + 1] = 1

                if geometery[q + 1, i - 1, g - 1] == 2:
                    geometery[q + 1, i - 1, g - 1] = 1

                #####

                if geometery[q, i, g + 1] == 2:
                    geometery[q, i, g + 1] = 1

                if geometery[q, i, g - 1] == 2:
                    geometery[q, i, g - 1] = 1

                if geometery[q, i + 1, g] == 2:
                    geometery[q, i + 1, g] = 1

                if geometery[q, i + 1, g + 1] == 2:
                    geometery[q, i + 1, g + 1] = 1

                if geometery[q, i + 1, g - 1] == 2:
                    geometery[q, i + 1, g - 1] = 1

                if geometery[q, i - 1, g] == 2:
                    geometery[q, i - 1, g] = 1

                if geometery[q, i - 1, g + 1] == 2:
                    geometery[q, i - 1, g + 1] = 1

                if geometery[q, i - 1, g - 1] == 2:
                    geometery[q, i - 1, g - 1] = 1

                    #######
                if geometery[q - 1, i, g] == 2:
                    geometery[q - 1, i, g] = 1

                if geometery[q - 1, i, g + 1] == 2:
                    geometery[q, i, g + 1] = 1

                if geometery[q - 1, i, g - 1] == 2:
                    geometery[q - 1, i, g - 1] = 1

                if geometery[q - 1, i + 1, g] == 2:
                    geometery[q - 1, i + 1, g] = 1

                if geometery[q - 1, i + 1, g + 1] == 2:
                    geometery[q - 1, i + 1, g + 1] = 1

                if geometery[q - 1, i + 1, g - 1] == 2:
                    geometery[q, i + 1, g - 1] = 1

                if geometery[q - 1, i - 1, g] == 2:
                    geometery[q, i - 1, g] = 1

                if geometery[q - 1, i - 1, g + 1] == 2:
                    geometery[q - 1, i - 1, g + 1] = 1

                if geometery[q - 1, i - 1, g - 1] == 2:
                    geometery[q - 1, i - 1, g - 1] = 1



list = []

for g in range(1,lg+1):
    for i in range(1,li+1):
        for q in range(1,el+1):
            list.append(geometery[q, i, g])

print(geometery.shape)


print(lg,li,el)


out = np.savetxt('./displacement' + str(x)+'/df2.0-diplace'+str(x)+'-'+str(li)+'-'+str(el)+'-'+str(lg)+'.dat', list, fmt='%d', delimiter='\n')
