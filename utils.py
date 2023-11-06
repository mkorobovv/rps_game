import cv2

def condition_rock(ind_pip, ind_tip, mid_pip, mid_tip, 
                   ring_pip, ring_tip, pinky_pip, pinky_tip) -> bool:
    
    return (ind_pip < ind_tip) and (mid_pip < mid_tip) and (ring_pip < ring_tip) and (pinky_pip < pinky_tip)
    
def condition_paper(ind_pip, ind_tip, mid_pip, mid_tip, 
                   ring_pip, ring_tip, pinky_pip, pinky_tip) -> bool:
    
    return (ind_pip > ind_tip) and (mid_pip > mid_tip) and (ring_pip > ring_tip) and (pinky_pip > pinky_tip)

def condition_scissors(ind_pip, ind_tip, mid_pip, mid_tip, 
                   ring_pip, ring_tip, pinky_pip, pinky_tip) -> bool:
    
    return (ind_pip > ind_tip) and (mid_pip > mid_tip) and (ring_pip < ring_tip) and (pinky_pip < pinky_tip)

def win_condition(human_choice: str, ai_choice: str) -> int:
    
    if (human_choice == 'rock' and ai_choice == 'paper') or\
    (human_choice == 'paper' and ai_choice == 'scissors') or\
    (human_choice == 'scissors' and ai_choice == 'rock'):
        return -1
    elif (ai_choice == 'rock' and human_choice == 'paper') or\
    (ai_choice == 'paper' and human_choice == 'scissors') or\
    (ai_choice == 'scissors' and human_choice == 'rock'):
        return 1
    else:
        return 0
    

def magic_human(gesture: str, frame) -> str: # This function drawing the image and returns naming of gesture
    
    image = cv2.imread(f'/Volumes/disk/dev/python/ML/rps_game/public/{gesture}.png')
    image_width, image_height, _ = image.shape
    frame[0:image_width, 0:image_height] = image
    
    return f'{gesture.capitalize()}'

def magic_ai(gesture:str, frame):
    
    image = cv2.imread(f'/Volumes/disk/dev/python/ML/rps_game/public/{gesture}.png', cv2.IMREAD_UNCHANGED)
    image_width, image_height, _ = image.shape
    frame[0:image_width, 1000:image_height + 1000] = image
    