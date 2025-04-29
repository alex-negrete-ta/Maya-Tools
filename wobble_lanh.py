import maya.cmds as cmds
import math
# Get the animation frame range.
def get_framerange():
    '''
    Description:
        Gets the frame range from your animation timeline to use.
    Input:
        None. it gets it from maya.
    Output:
        frame_dict (dict): It returns a dictionary with 
        the first frame and last frame of the animation.
    '''
    frame_dict = dict()
    frame_dict['min_frame'] = cmds.playbackOptions( query = True, minTime = True)
    frame_dict['max_frame'] = cmds.playbackOptions( query = True, maxTime = True)
    return frame_dict
    
# Set the wobble of the animation.
def set_wobble ( selected_geo, frequency = 1, amplitude = 1, offset = 0, phase = 0):
    '''
    Description:
        Set the geometry selected to the wobble animation with a frequency 
        and amplitude desired.
    Input:
        object: selection of the geometry.
        frequency (float): frequency of the animation graph.
        amplitude (float): amplitude of the animation graph.
    Output:
        x_rot (float): The X position of the rotation of the object.
        z_rot (float): The Z position of the rotation of the object.
    '''
    framerange = get_framerange()
    for frame in range(int(framerange['min_frame']),int(framerange['max_frame'])):
        x_rot = math.sin ( (frame + phase)* frequency )*amplitude + offset
        z_rot = math.cos ( (frame + phase)* frequency )*amplitude + offset
        cmds.setKeyframe( 
                        selected_geo, 
                        attribute = 'rotateX', 
                        value = x_rot, 
                        time = frame 
                        )
        cmds.setKeyframe( 
                        selected_geo, 
                        attribute = 'rotateZ', 
                        value = z_rot, 
                        time = frame 
                        )
    return x_rot, z_rot

      
#To run it: set_wobble(cmds.ls(sl=True,o=True),.5,.5)