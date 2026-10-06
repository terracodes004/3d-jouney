from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
import math, time
app=Ursina(title="free fire",  development_mode=False)
# EditorCamera()
hp = 1000

ground = Entity(model="plane", texture="grass", scale=1000, collider="box")
# sky = Entity(model="plane", texture="sky_default", scale=10000, collider="box")
player = FirstPersonController(model="cube", origin_y=-.5,  color=color.orange, collider="box",has_pickup=False)
shoot = Audio("shoot.wav", autoplay=False)
hit = Audio("hit.wav", autoplay=False)


enemies = []

for i in range(30):
  enemy = Entity(model="cube", color=color.red,collider="box", origin_y=-.5,)
  enemy.y = player.y
  enemy.x = randint(-300, 300)
  enemy.z = randint(-300, 300)
  enemy.look_at_xz(player)
  print(enemy.rotation_y)
  enemies.append(enemy)
  
for i in range(50):
  v = Entity(model="cube", texture="home-1781163826369_0000.png", position=(randint(-500, 500), player.y,  randint(-500, 500)), collider="box", scale=randint(75,100), origin_y=-.5)
  Entity(model="cube", texture="brick", position=(v.x+int(v.scale.x), v.y, v.z), collider="box", scale=randint(1,3), origin_y=-.5)
  Entity(model="cube", texture="brick", position=(v.x, v.y, v.z+v.scale.x), collider="box", scale=randint(1,3), origin_y=-.5)
  Entity(model="cube", texture="brick", position=(v.x+v.scale.x, v.y, v.z+v.scale.x), collider="box", scale=randint(1,3), origin_y=-.5)
  Entity(model="cube", texture="brick", position=(v.x*2+v.scale.x, v.y, v.z+v.scale.x), collider="box", scale=randint(1,3), origin_y=-.5)
  Entity(model="cube", texture="brick", position=(v.x*2+v.scale.x, v.y, v.z*2+v.scale.x), collider="box", scale=randint(1,3), origin_y=-.5)

bullet = Entity(model="cube", scale=(0.25, 0.25, 100), origin_y=-.5, position=(player.x, player.y+100, player.z), collider="box")
index = 0
move = 0
score = Text(f"""
enemies: {len(enemies)}
HP : {"."*int(hp/100)}
""", position=(-0.85,0), scale=1.5)
# sky.rotation_x = 90
def input(k):
  global index, move
  
  if k == "left mouse down":
    bullet.y = player.y+0.5
    shoot.play()
    move+=1
    
      
    index+=1
    if index>29:
      index=0
    
exiht=False
def update():

  global enemies, move, index, hp, exiht
  if exiht:
    sys.exit()
  if hp<=0:
    score.text = "You lose..."
    time.sleep(3)
    exiht = True
  elif len(enemies)<=0:
    score.text = "You win..."
    time.sleep(3)
    exiht = True
  score.text = f"""
enemies: {len(enemies)}
HP : {"#"*int(hp/100)}
"""
  bullet.x = player.x+50*math.sin(math.radians(player.rotation_y))
  bullet.z = player.z+50*math.cos(math.radians(player.rotation_y))
  bullet.rotation_y = player.rotation_y
  if move > 3:
    move = 0
    bullet.y = player.y+100
  if move == 0:
    bullet.y = player.y+100
  move +=1
  for h in enemies:
    h.look_at_xz(player)
    if(distance(player, h)>10):

      h.x += randint(3,7)*math.sin(math.radians(h.rotation_y))*time.dt
      h.z += randint(3,7)*math.cos(math.radians(h.rotation_y))*time.dt
    else:
      hp-=1
      shoot.play()
    if bullet.intersects(h).hit:
      destroy(h)
      enemies.remove(h)
      hit.play()
      
app.run()