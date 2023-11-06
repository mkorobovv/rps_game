import cv2
import numpy as np
import mediapipe as mp
from settings.config import *
from settings.utils import *
import random
import time


def main() -> None:
    
    '''Implement Meiapipe Holistic solution'''
    mp_hands = mp.solutions.holistic
    
    '''Camera setttings'''
    camera = cv2.VideoCapture(0)
    camera.set(3, 1000)      # Width
    camera.set(4, 1000)      # Height
    camera.set(10, 1000)    # Brightness
    
    timer = 0           # Timer
    stateResult = False # State result
    startGame = False   # Start condition
    scores = [0, 0]     # Scores [Human, AI]
    human_choice = 'white' # Human choice
    ai_choice = 'white'    # AI choice
    
    with mp_hands.Holistic(min_detection_confidence = 0.5, min_tracking_confidence = 0.5,
                         static_image_mode = True) as hands:
        while True:
            
            _, frame = camera.read()
            
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
            if startGame:
                
                if stateResult is False:
                    
                    human_choice = 'white'
                    ai_choice = 'white'
                    
                    timer = time.time() - initialTime
                    cv2.putText(frame, str(int(timer)), (600, 400), cv2.FONT_HERSHEY_PLAIN, 6, (102, 0, 102), 4)
                    
                    if timer > 3:
                        stateResult = True
                        timer = 0
                        
                        if results.left_hand_landmarks:      
                                
                            hand_lmark = results.left_hand_landmarks.landmark
                                
                            index_pip = hand_lmark[INDEX_FINGER_PIP].y
                            index_tip = hand_lmark[INDEX_FINGER_TIP].y
                            mid_pip = hand_lmark[MIDDLE_FINGER_PIP].y
                            mid_tip = hand_lmark[MIDDLE_FINGER_TIP].y
                            ring_pip = hand_lmark[RING_FINGER_PIP].y
                            ring_tip = hand_lmark[RING_FINGER_TIP].y
                            pinky_pip = hand_lmark[PINKY_FINGER_PIP].y
                            pinky_tip = hand_lmark[PINKY_FINGER_TIP].y
                                
                            
                            ai_choice = random.choice(AI_GESTURES)
                                
                            """ Gestures recognition logic """

                            if condition_rock(ind_pip=index_pip, ind_tip=index_tip, mid_pip=mid_pip, mid_tip=mid_tip,
                                                ring_pip=ring_pip, ring_tip=ring_tip, pinky_pip=pinky_pip, pinky_tip=pinky_tip):
                                    
                                human_choice = 'rock'
                                        
                            elif condition_paper(ind_pip=index_pip, ind_tip=index_tip, mid_pip=mid_pip, mid_tip=mid_tip,
                                                    ring_pip=ring_pip, ring_tip=ring_tip, pinky_pip=pinky_pip, pinky_tip=pinky_tip):
                                        
                                human_choice = 'paper'
                                    
                            elif condition_scissors(ind_pip=index_pip, ind_tip=index_tip, mid_pip=mid_pip, mid_tip=mid_tip,
                                                    ring_pip=ring_pip, ring_tip=ring_tip, pinky_pip=pinky_pip, pinky_tip=pinky_tip):
                                    
                                human_choice = 'scissors'
                            
                            """ Win condition logic """
                                    
                            if win_condition(human_choice=human_choice, ai_choice=ai_choice) == 1:
                                scores[0] += 1
                            elif win_condition(human_choice=human_choice, ai_choice=ai_choice) == -1:
                                scores[1] += 1
                                
                                
           
                               
            magic_human(gesture=human_choice, frame=frame)
            magic_ai(gesture=ai_choice, frame=frame)
            
            
            cv2.putText(frame,  f'YOU: {scores[0]}', (100, 600), cv2.FONT_HERSHEY_PLAIN, 4, (102, 0, 102), 6)
            cv2.putText(frame, f'AI: {scores[1]}', (1000, 600), cv2.FONT_HERSHEY_PLAIN, 4, (102, 0, 102), 6)
            
            
            
            cv2.imshow("Rock-Paper-Scissors Game", frame)
            
            """
            
            1) To start game press 's' on your keyboard
            
            2) To quit game press 'q' on your keyboard
            
            """
            
            key = cv2.waitKey(1)
            
            if key == ord('s'):
                startGame = True
                initialTime = time.time()
                stateResult = False
            
            if key == ord('q'):
                break
            
    camera.release()
    cv2.destroyAllWindows() 
    
    
if __name__ == "__main__":
    main()
    