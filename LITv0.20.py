from PIL import Image
from gtts import gTTS
import tesserocr
from libcamera import controls
from picamera2 import Picamera2, Preview
import pygame
pygame.init()
from io import BytesIO
my_stream = BytesIO()
from gpiozero import Button
picam2 = Picamera2()
#preview_config = picam2.create_preview_configuration(main={"size": (640, 480)})
#capture_config = picam2.create_still_configuration(main={'size': (2304,1296)})
preview_config = picam2.create_preview_configuration(main={"size": (2304,1296)})
picam2.configure(preview_config)
preview = picam2.start_preview(Preview.QTGL, x=0,y=0,width=576,height=324)
picam2.start()
picam2.set_controls({"AfMode":controls.AfModeEnum.Continuous})
test6 = "test"
isRunning = 1   
isImage = 0
buttonReleased = True
isString = 0
pressed = False
button = Button(16)
while True:
    if button.is_pressed:
        if buttonReleased:
            print("else")
            
            #picam2.switch_mode_and_capture_file(capture_config,"test.png")
            picam2.capture_file("test.png")
            isImage = 1
            buttonReleased = False
    else:
        buttonReleased = True   
    if isString == 1:
        if result == "":
            result = "Try Again, I couldn't see too well!"
        print("isString")
        tts = gTTS(result,lang ='en')
        tts.save('test6.mp3')
        result = ""
        my_sound = pygame.mixer.Sound('test6.mp3')
        my_sound.play()
        isString = 0
    if isImage == 1:
        print("isImage")
        result = tesserocr.file_to_text('test.png')
        print(result)
        isString = 1
        isImage = 0
            




