import maya.cmds as cmds
import random

#Check if there is a selection.
def check_selection():
    '''
    Description:
        To select the vertices and check to see if you have a selection.
    Input:
        None
    Output:
        A selection of vertices, or a print saying you have no geometry selected.
    '''
    selection = cmds.ls(sl=True, o= True) 
    if not selection:
        print ( 'You have no geometry selected.' )
        quit()
    else:
        sel_vtx = random.sample(cmds.ls('{}.vtx[:]'.format(selection[0]), fl=True),50)
        return sel_vtx

# Create rock generators.
def create_rock(distortion = .1, subdivisions = 16):
    '''
    Description:
    Creates a rock geometry into your script.

    Input:
    distortion (int/float): The amount each vertex distorts
    subdivisions (int/float): The amount of subdivision of the sphere.

    Output:
    Generaters a random distort sphere to simulate a rock.
    '''
    rock = cmds.polySphere(sx = subdivisions, sy = subdivisions, name = 'rock_')[0]
    for vertex in range(cmds.polyEvaluate(rock,v=True)):
        cmds.polyMoveVertex('{}.vtx[{}]'.format(rock, vertex),
            t =(random.uniform( -(distortion), distortion),
                random.uniform( -(distortion), distortion),
                random.uniform( -(distortion), distortion),
                ))
    return rock
    
# Place geometry
def place_geometry( vertices, x_scale = .5 , y_scale = 1, offset = .2, r = 2):
    '''
    Description:
    Place random rock geometry into a plane.

    Input:
    vertices (int): a selection of the vertices you want to scatter to.
    x_scale (float/int): x scale of the rocks scattered.
    y_scale (float/int): y scale of the rocks scattered. 

    Output:
    Rock scattered accross a geometry.
    '''
    for vert in vertices:
        # Get position.
        position= cmds.xform(vert, query = True, t = True, ws=True)
        # Generate rock.
        rock_transform = create_rock()
        # Set position on rocks.
        cmds.xform(
            rock_transform,
            t=position,
            scale=(
                random.uniform( x_scale, y_scale ),
                random.uniform( x_scale, y_scale ),
                random.uniform( x_scale, y_scale )
                )
            )
        cmds.xform(
            rock_transform,
            r = True,
            t =(
                random.uniform( -(offset), offset ),
                random.uniform( -(offset), offset ),
                random.uniform( -(offset), offset )
                ),
            ro =(
                random.uniform(-(r), r ),
                random.uniform(-(r), r ),
                random.uniform(-(r), r )
                )
            )
        cmds.makeIdentity(apply=True, t=True, r=True, s=True, n=0, pn = 1)
        

       
#place_geometry(check_selection())      