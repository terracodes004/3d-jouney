from ursina import *

app = Ursina(title="sss")
parent = Entity(model="sphere", color=color.red, scale=2, position=(0,0,0), texture="sky_default")#parent = Entity(model="sphere", color=color.red, scale=2, position=(1,1,1), texture="home-1781163826369_0000.png")

child1 = Entity(parent=parent, model='sphere',texture="sky_default" ,color=color.orange, scale=0.3, position=(1, 0, 0))
child2 = Entity(parent=parent, model='sphere',texture="sky_default" ,color=color.orange, scale=0.3, position=(-1, 0, 0))
child3 = Entity(parent=parent, model='sphere',texture="sky_default" ,color=color.orange, scale=0.3, position=(0, 1, 0))
child4 = Entity(parent=parent, model='sphere',texture="sky_default" ,color=color.orange, scale=0.3, position=(0, -1, 0))
child5 = Entity(parent=parent, model='sphere',texture="sky_default" ,color=color.orange, scale=0.3, position=(0, 0,1))
child6 = Entity(parent=parent, model='sphere',texture="sky_default" ,color=color.orange, scale=0.3, position=(0, 0,-1))

children = [child1, child2, child3, child4, child5, child6]
def update():
  parent.rotation_y += 30 * time.dt
  parent.rotation_x += 15 * time.dt

  
  for i in children:
    if held_keys["s"]:
        i.scale -= -0.003
        camera.rotation_z += 0.01
    if held_keys["z"]:
       camera.z += -0.01
    if held_keys["o"]:
       camera.z += 0.01
    i.rotation_x += 10*time.dt
    i.rotation_y += 5*time.dt
    
def input(k):
   if k == "scroll up":
      parent.y+=0.1
   elif k=="scroll down":
      parent.y-=0.1
app.run()