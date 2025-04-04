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
def set_wobble ( object, frequency = 1, amplitude = 1):
    '''
    Description:
        Set the geometry selected to the wobble animation with a frequency and amplitude desired.
    Input:
        object: selection of the geometry.
        frequency (float): frequency of the animation graph.
        amplitude (float): amplitude of the animation graph.
    Output:
        A wobble animation graph on the selected geometry.
    '''
    framerange = get_framerange()
    for frame in range(int(framerange['min_frame']),int(framerange['max_frame'])):
        x_rot = math.sin ( frame * frequency )*amplitude
        z_rot = math.cos ( frame * frequency )*amplitude
        cmds.setKeyframe( object, attribute = 'rotateX', value = x_rot, time = frame )
        cmds.setKeyframe( object, attribute = 'rotateZ', value = z_rot, time = frame )      
      
#To run it: set_wobble(cmds.ls(sl=True,o=True),.5,.5)