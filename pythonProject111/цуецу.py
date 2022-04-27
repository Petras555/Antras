def showGameSurvival():


game = gamemode_normal()

while game.health != 0:
    game.next = False
    clearScreen()
    changeBackground("Survival")

    # Placing Labels on the screen for game.....

    # ... Health
    root.update()

    lblCountDownLeft = Label(root, bg="White", fg="Green", font=XXLARGE_BUTTON_FONT)
    lblCountDownLeft.place(x=169, y=350, anchor=CENTER)
    lblCountDownRight = Label(root, bg="White", fg="Green", font=XXLARGE_BUTTON_FONT)
    lblCountDownRight.place(x=1111, y=350, anchor=CENTER)
    # CountDown
    count = 7
    while count > 0:
        lblCountDownLeft['text'] = count
        lblCountDownRight['text'] = count
        root.update()
        count -= 1
        time.sleep(1)

    lblCountDownLeft.destroy()
    lblCountDownRight.destroy()
    root.update()
    # Num on left x=169, right, x=1111 y=360

    game.measureDistance()
    if game.playerDistance >= game.lowerBound() and game.playerDistance <= game.upperBound():
        game.level += 1
        clearScreen()
        changeBackground("Survival")
        graphicalDisplay(game)

        # NextLevelButton
        btnNextLevel = Button(root,
                              bg=lbBlue,
                              fg="white",
                              text="Level" + str(game.level),
                              font=SMALL_BUTTON_FONT,
                              activebackground="white",
                              activeforeground=lbBlue,
                              command=lambda: nextLevel(game),
                              bd=0)
        btnNextLevel.place(x=1003, y=492, anchor=NW, width=247, height=78)
        root.update()
        while game.next == False:
            print(game.next)
    else:
        game.health -= 1

    if game.allowance > 4:
        game.allowance = int(game.allowance * 0.9)

# when game is over delete the shit
if game.health == 0:
    del game