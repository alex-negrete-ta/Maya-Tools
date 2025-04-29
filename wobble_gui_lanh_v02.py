import maya.cmds as cmds
import wobble_lanh as wobble

def main():
    '''
    Description: Runs the program.
    Input: none.
    Output: None
    '''
    # Runs the program.
    wobble_win_UI()
    return

def wobble_win_UI(width = 250, height = 350, spacing = 10, cwidth = 350):
    '''
    Description:
        Builds an UI for the function of Wobble.
    Input:
        width (int): Width of the window.
        height (int): height of the window.
        spacing (int): spacing of the rows.
        cwidth (int): column width.
    Output:
        wiggle_window_ui (object): It returns a window with the buttons.
    '''
    # Check if there is an instanced window, if there is it closes it.
    close_ui_CB()
    # Create a window set to width = 250, height 200 and title Wiggle.
    wiggle_window_ui = cmds.window(
                                'wobble_win',
                                title = 'wobble animation', 
                                widthHeight = (width,height)
                                )
    # Add a simple layout to the controlers.
    cmds.columnLayout( 
                    columnAttach=('both', 6), 
                    rowSpacing= spacing, 
                    columnWidth= cwidth, 
                    adjustableColumn = True 
                    )
    # Set the values for the dimensions of the buttons.
    c_width_01 = int(cwidth * 0.17)
    c_width_02 = int(cwidth * 0.14)
    # Add controls to the window.
    cmds.text(label = 'Wobble Animation')
    cmds.text(label = 'Select an object.', align = 'left')
    cmds.text(label = 'Frequency: Speed.', align = 'left')
    cmds.text(label = 'Amplitude: Angle of rotation', align = 'left')
    cmds.text(label = 'Offset: Shift the start angle.', align = 'left')
    cmds.text(label = 'Phase: Shift the start.', align = 'left')
    frequency = cmds.floatSliderGrp( 
                        'frequency',
                        label = 'Frequency:', 
                        field = True, 
                        minValue = 0.0, 
                        maxValue = 10, 
                        value = .1, 
                        columnAlign = (1,'left'), 
                        columnWidth3 = (c_width_01, c_width_02, c_width_02),
                        annotation = 'Speed'
                        )
    amplitude = cmds.floatSliderGrp(
                        'amplitude',
                        label = 'Amplitude:', 
                        field = True, 
                        minValue = 0.0, 
                        maxValue = 10, 
                        value = 5.0, 
                        columnAlign = (1,'left'), 
                        columnWidth3 = (c_width_01, c_width_02, c_width_02),
                        annotation = 'Angle of the rotation.'
                        )
    offset = cmds.floatSliderGrp(
                        'offset',
                        label = 'Offset:', 
                        field = True, 
                        minValue = 0.0, 
                        maxValue = 10, 
                        value = 0.0, 
                        columnAlign = (1,'left'), 
                        columnWidth3 = (c_width_01, c_width_02, c_width_02),
                        annotation = 'Shifts the start of the angle.'
                        )
    phase = cmds.floatSliderGrp( 
                        'phase',
                        label = 'Phase:', 
                        field = True, 
                        minValue = 0.0, 
                        maxValue = 10, 
                        value = 0.0, 
                        columnAlign = (1,'left'), 
                        columnWidth3 = (c_width_01, c_width_02, c_width_02),
                        annotation = 'Shifts the start.'
                        )
    cmds.rowColumnLayout ( adjustableColumn = True, numberOfColumns = 3)
    cmds.button(
                label = 'Wobble and close', 
                command = 'import wobble_gui_lanh; wobble_gui_lanh.wobble_close_CB()'

                )
    cmds.button(
                label = 'Wobble', 
                command = 'import wobble_gui_lanh; wobble_gui_lanh.wobble_CB()'
                )
    cmds.button(
                label = 'Close', 
                command = 'import wobble_gui_lanh; wobble_gui_lanh.close_ui_CB()'
                )
    
    # Show the window.
    cmds.showWindow(wiggle_window_ui)

    return frequency, amplitude, offset, phase
    
def wobble_CB():
    '''
    Description:
        Queerys the GUI
    Inputs:
        None
    Outputs:
        new_frequency (float): New input value of the frequency input. 
        new_amplitude (float): New input value of the amplitude input.  
        new_offset (float): New input value of the offset input.  
        new_phase (float): New input value of the phase input. 
    '''
    # Queerys the new users values as inputs.
    new_frequency =   cmds.floatSliderGrp(
                                frequency,
                                query = True, 
                                field = True, 
                                value = True, 
                                )
    new_amplitude =   cmds.floatSliderGrp(
                                amplitude,
                                query = True, 
                                field = True, 
                                value = True, 
                                )
    new_offset =   ocmds.floatSliderGrp(
                        offset,
                        query = True, 
                        field = True, 
                        value = True, 
                        )
    new_phase =   cmds.floatSliderGrp(
                        phase,
                        query = True, 
                        field = True, 
                        value = True, 
                        )
    # Sets the original wobble functionwith the new inputs.
    wobble.set_wobble ( 
                        cmds.ls(sl=True, o = True), 
                        new_frequency, 
                        new_amplitude, 
                        new_offset, 
                        new_phase
                        )
    return new_frequency, new_amplitude, new_offset, new_phase

def wobble_close_CB():
    '''
    Description: It excutes the wobble and the close CB functions.
    Input: None.
    Output: None.
    '''
    # It runs the wobble_CB() function.
    wobble_CB()
    # It runs the close_ui_CB() function.
    close_ui_CB()

    return

def close_ui_CB():
    '''
    Description:
    It closes the window.
    Input: none.
    Output: none.
    '''
    # It closes the window if the window exists.
    if cmds.window('wobble_win', exists = True):
        cmds.deleteUI('wobble_win')
    
    return
    
#wobble_win_UI()