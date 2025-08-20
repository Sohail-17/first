from ursina import *

# Set up the app window
app = Ursina()

# Create a beautiful skybox (sky texture)
sky = Sky()

# Add a ground plane (your scenery base)
ground = Entity(model='plane', scale=(100,1,100), texture='water', texture_scale=(10,10))

# Add some cubes to the scene (just to make things more interesting)
cube1 = Entity(model='cube', color=color.red, scale=(2,2,2), position=(5, 1, 5))
cube2 = Entity(model='cube', color=color.blue, scale=(2,2,2), position=(-5, 1, 5))
cube3 = Entity(model='cube', color=color.green, scale=(2,2,2), position=(0, 1, -5))

# Add a camera controller so you can move around
camera.position = (0, 100, 20)
camera.look_at(Vec3(0, 0, 0))  # Look at the center of the scene

# Move camera around with arrow keys
def update():
    if held_keys['w']:
        camera.z += 1
    if held_keys['s']:
        camera.z -= 1
    if held_keys['a']:
        camera.x -= 1
    if held_keys['d']:
        camera.x += 1
    if held_keys['q']:
        camera.pan +=1
    if held_keys['e']:
        camera.pan -=1                                                                        
# Run the game
app.run()
