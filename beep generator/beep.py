import pygame

pygame.init()

BEEP = pygame.USEREVENT + 1

screen = pygame.display.set_mode((1000, 1000))

running = True

button1 = pygame.Rect(0, 400, 300, 300)
button2 = pygame.Rect(350, 400, 300, 300)
button3 = pygame.Rect(700, 400, 300, 300)

slider = pygame.Rect(200, 800, 600, 20)
sliderButton = pygame.Rect(263, 795, 30, 30)
sliderHeld = False
beepSpeed = 80


freesansbold = pygame.font.Font('freesansbold.ttf', 50)
beepSound = pygame.mixer.Sound('beep.wav')

beeps = 0
pressed = False



while running:
    mouseX, mouseY = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not pressed:
            if sliderButton.collidepoint((mouseX, mouseY)):
                sliderHeld = True

            if button1.collidepoint((mouseX, mouseY)):
                beeps += 1
                pressed = True
                pygame.draw.rect(screen, [20, 20, 20], button1, border_radius=20)

            elif button2.collidepoint((mouseX, mouseY)):
                beeps += 3
                pressed = True
                pygame.draw.rect(screen, [20, 20, 20], button2, border_radius=20)
            
            elif button3.collidepoint((mouseX, mouseY)):
                beeps += 5
                pressed = True
                pygame.draw.rect(screen, [20, 20, 20], button3, border_radius=20)

            if beeps > 0:
                pygame.time.set_timer(BEEP, beepSpeed, loops = beeps)

        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = False
            sliderHeld = False

        elif event.type == BEEP:
            beepSound.play()
            beeps -= 1        

    screen.fill("black")

    if sliderHeld:
        sliderButton.centerx = max(slider.left, min(mouseX, slider.right))
        beepSpeed = int(20 + (500-20) * (sliderButton.centerx - slider.left) / slider.width)

    pygame.draw.rect(screen, [50, 50, 50], slider)

    if not sliderHeld:
        pygame.draw.rect(screen, [100, 100, 100], sliderButton)
    elif sliderHeld:
        pygame.draw.rect(screen, [150, 150, 150], sliderButton)

    speedText = freesansbold.render("Speed: {}ms".format(beepSpeed), True, (255, 255, 255))
    screen.blit(speedText, (345, 720))



    if not pressed and button1.collidepoint((mouseX, mouseY)):
        pygame.draw.rect(screen, [50, 50, 50], button1, border_radius=20)
    
    elif not pressed and button2.collidepoint((mouseX, mouseY)):
        pygame.draw.rect(screen, [50, 50, 50], button2, border_radius=20)
    
    elif not pressed and button3.collidepoint((mouseX, mouseY)):
        pygame.draw.rect(screen, [50, 50, 50], button3, border_radius=20)

    beepsText = freesansbold.render("BEEPS: {}".format(beeps), True, (255, 255, 255))
    screen.blit(beepsText, (400, 100))

    oneBeepText = freesansbold.render("1 BEEP", True, (255, 255, 255))
    screen.blit(oneBeepText, (55, 525))
    threeBeepsText = freesansbold.render("3 BEEPS", True, (255, 255, 255))
    screen.blit(threeBeepsText, (400, 525))
    fiveBeepsText = freesansbold.render("5 BEEPS", True, (255, 255, 255))
    screen.blit(fiveBeepsText, (750, 525))

    pygame.display.flip()

