import moth_world
import nengo
world = moth_world.World(x=0, y=0, heading=0,
                         bounds_x=(-1000.0, 1000.0),
                         bounds_y=(-1000.0, 1000.0),
                         grid_size=(100, 100),
                         sensor_dist=50,
                         trail_length=500,
                         acceleration=0.2,
                         drag=0.5,
                         trail_dt=0.1)

model = nengo.Network()
with model:
    visualization = world.make_visualize()
    movement = world.make_movement(0.1)
    pos = world.make_position()