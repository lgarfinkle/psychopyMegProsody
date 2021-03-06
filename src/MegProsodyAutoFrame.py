#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.75.01), November 05, 2012, at 21:19
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui, sound
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from psychopy import parallel

parallel.setPortAddress(0x378) #address for parallel port on many machines
pinNumber = 2 #choose a pin to write

# Store info about the experiment session
expName = 'None'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('../data'):
    os.makedirs('../data')  # if this fails (e.g. permissions) we will get error
filename = '../data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')

# Initialize components for Routine "beginfo"
beginfoClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='You will hear a short vocal utterance, when the probe with the yellow emoticons appears, press the button # that best describes the emotion heard in the voice.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "soundPresent"
soundPresentClock = core.Clock()
fixation = visual.ImageStim(win=win, name='fixation',units='pix', 
    image='../media/img/cross.bmp', mask=None,
    ori=0, pos=[0, 0], size=[1440, 900],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=False, depth=0.0)
megStim = sound.Sound('A')
megStim.setVolume(1)

# Initialize components for Routine "trial"
trialClock = core.Clock()
emoticons = visual.ImageStim(win=win, name='emoticons',units='pix', 
    image='../media/img/Emoticons_H.bmp', mask=None,
    ori=0, pos=[0, 0], size=[1440, 900],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=False, depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
completeMsg = visual.TextStim(win=win, ori=0, name='completeMsg',
    text='Thank you for completing this test!',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine"beginfo"-------
t = 0
beginfoClock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
beginfoComponents = []
beginfoComponents.append(text)
for thisComponent in beginfoComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "beginfo"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = beginfoClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    elif text.status == STARTED and frameN >= 0 + 10 * 60:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginfoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "beginfo"-------
for thisComponent in beginfoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('../conditionsFiles/Meg_prosody_block1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine"soundPresent"-------
    t = 0
    soundPresentClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    megStim.setSound('../media/audio/'+pros_stim)
    # keep track of which components have finished
    soundPresentComponents = []
    soundPresentComponents.append(fixation)
    soundPresentComponents.append(megStim)
    for thisComponent in soundPresentComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #TIMEFIX: gets the duration of the wav file for bawaSound
    stimLength = megStim.getDuration()
    # gives the stim duration in frames (60 Hz) & padded by 1 frame
    stimFrameLen = stimLength * 60 + 1
    
    #-------Start Routine "soundPresent"-------

    continueRoutine = True
    while continueRoutine:
        # get current time
        t = soundPresentClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

    # UPDATE/DRAW COMPONENTS ON EACH FRAME ==(START)=================
        
      # fixation UPDATES ==(START)===================================

        # Quick description: controls when to show fixation on screen
        
        # if: (1) on first frame (frame 0)
        #     (2) the fixation has not started
        # then: (1) record start time in seconds (t)
        #       (2) record start time in frames (frameN)
        #       (3) draw the fixation
        # else if: (1) fixation has started
        #          (2) on frame past the frame duration of the stimuli
        # then: (1) stop drawing fixation

        if frameN >= 0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t  # underestimates by a little under one frame
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        elif fixation.status == STARTED and frameN >= stimFrameLen:
            fixation.setAutoDraw(False)
            
      # fixation UPDATES ==(END)=====================================
            
      # START/STOP megStim ==(START)=================================

        # Quick description: controls when stimuli is played and stops

        # if: (1) on first frame (frame 0)
        #     (2) the stimuli has not started playing
        # then: (1) clear the parallel pins
        #       (2) record start time in seconds (t)
        #       (3) record start time in frames (frameN)
        #       (4) play the stimuli
        #       (5) set the parallel pins
        
        if frameN >= 0 and megStim.status == NOT_STARTED:
            #PARALLEL CLEAR
            parallel.setData(0) #sets all pins low
            
            # keep track of start time/frame for later
            megStim.tStart = t  # underestimates by a little under one frame
            megStim.frameNStart = frameN  # exact frame index
            megStim.play()  # start the sound (it finishes automatically)

            #PARALLEL SET
            parallel.setData(trigg_code) #sends trigg_code from conditions file

      # START/STOP megStim ==(END)===================================

    # UPDATE/DRAW COMPONENTS ON EACH FRAME ==(END)===================

    # ENDING TASKS ==(START)=========================================

      # CLEAR PARALLEL ==(START)=====================================

        # Quick description: clear parallel port

        # if: (1) 1 frame has passed (frame 1)
        # then: (1) clear the parallel pins
        
        if frameN >= 2:
            parallel.setData(0)

      # CLEAR PARALLEL ==(END)=======================================

      # SET megStim.status FINISHED ==(START)========================

        # Quick description: sets stimuli status to finished when done

        # if: (1) on frame past the frame duration of the stimuli
        #     (2) stimuli has started playing
        # then: (1) set stimuli status to finished
        #       (2) record time stimulus plays for
        
        if frameN >= stimFrameLen and megStim.status == STARTED:
            megStim.status = FINISHED
            stimEnd = soundPresentClock.getTime()

      # SET megStim.status FINISHED ==(END)==========================

    # ENDING TASKS ==(END)===========================================
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in soundPresentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "soundPresent"-------
    for thisComponent in soundPresentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine"trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(key_resp)
    trialComponents.append(emoticons)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

    # UPDATE/DRAW COMPONENTS ON EACH FRAME ==(START)=================    

      # key_resp UPDATES ==(START)===================================

        # Quick description: controls when answers can be received

        # if: (1) on first frame (frame 0)
        #     (2) key responses not being received yet
        # then: (1) record start time in seconds (t)
        #       (2) record start time in frames (frameN)
        #       (3) start receiving key responses
        #       (4) start key response clock to zero (reset)
        #       (5) clear any previous key responses
        # else if: (1) key responses are being received
        #          (2) 2.3 seconds in frames have passed
        # then: (1) stop receiving key responses
        
        if frameN >= 0 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.tStart = t  # underestimates by a little under one frame
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            event.clearEvents()
        elif key_resp.status == STARTED and frameN >= 2.3 * 60:
            key_resp.status = STOPPED

        # if: (1) key responses are being recceived
        # then: (1) record keys, response time & correct
        
        if key_resp.status == STARTED:  # only update if being drawn
            theseKeys = event.getKeys(keyList=['1', '2', '3','4'])
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp.keys == []:  # then this was the first keypress
                    key_resp.keys = theseKeys[0]  # just the first key pressed
                    key_resp.rt = key_resp.clock.getTime()
                    # was this 'correct'?
                    if (key_resp.keys == str(cor_response)): key_resp.corr = 1
                    else: key_resp.corr=0
        
      # key_resp UPDATES ==(END)=====================================

      # emoticons UPDATES ==(START)==================================
        
        # Quick description: controls when the emotions displayed
        
        # if: (1) on first frame (frame 0)
        #     (2) emoticons are not being displayed
        # then: (1) record start time in seconds (t)
        #       (2) record start time in frames (frameN)
        #       (3) draw the emoticons
        # else if: (1) emoticons being displayed
        #          (2) 2.3 seconds in frames have passed
        # then: (1) stop drawing emoticons
        #       (2) record time emoticons stay on screen
        
        if frameN >= 0 and emoticons.status == NOT_STARTED:
            # keep track of start time/frame for later
            emoticons.tStart = t  # underestimates by a little under one frame
            emoticons.frameNStart = frameN  # exact frame index
            emoticons.setAutoDraw(True)
        elif emoticons.status == STARTED and frameN >= 2.3 * 60:
            emoticons.setAutoDraw(False)
            emoticonsEnd = trialClock.getTime()

      # emoticons UPDATES ==(END)====================================

    # UPDATE/DRAW COMPONENTS ON EACH FRAME ==(END)===================
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(key_resp.keys) == 0:  # No response was made
       key_resp.keys=None
       # was no response the correct answer?!
       if str(cor_response).lower() == 'none': key_resp.corr = 1  # correct non-response
       else: key_resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('stimEnd',stimEnd)
    trials.addData('emoticonsEnd',emoticonsEnd)
    trials.addData('totalTime', stimEnd + emoticonsEnd)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):  params = []
else:  params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine"end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(completeMsg)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *completeMsg* updates
    if t >= 0.0 and completeMsg.status == NOT_STARTED:
        # keep track of start time/frame for later
        completeMsg.tStart = t  # underestimates by a little under one frame
        completeMsg.frameNStart = frameN  # exact frame index
        completeMsg.setAutoDraw(True)
    elif completeMsg.status == STARTED and t >= (0.0 + 5.0):
        completeMsg.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Shutting down:
win.close()
core.quit()
