import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z

list_a = [[1, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0, 0]]

for i in range(0, len(list_a)):
    for j in range(0, len(list_a[i])):
        if list_a[i][j] == 1:
            mc.setBlock(x+i, y, z+j, block.TNT.id)
        if list_a[i][j] == 0:
            mc.setBlock(x+i, y, z+j, block.AIR.id)
