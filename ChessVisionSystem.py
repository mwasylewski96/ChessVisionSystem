import numpy as np
import cv2
import imutils
import os
os.remove("C:\\Users\\mwasy\\OneDrive\\Pulpit\\\pgny\\partia.txt")
fh = open("C:\\Users\\mwasy\\OneDrive\\Pulpit\\\pgny\\partia.txt", "w")
fh.close()
"""def getContours(subtract):
    contours,hierarchy = cv2.findContours(subtract,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area) """
tablica_pól = [
["R","a","8"],["N","b","8"],["B","c","8"],["Q","d","8"],["K","e","8"],["B","f","8"],["N","g","8"],["R","h","8"],
["p","a","7"],["p","b","7"],["p","c","7"],["p","d","7"],["p","e","7"],["p","f","7"],["p","g","7"],["p","h","7"],
["","a","6"],["","b","6"],["","c","6"],["","d","6"],["","e","6"],["","f","6"],["","g","6"],["","h","6"],
["","a","5"],["","b","5"],["","c","5"],["","d","5"],["","e","5"],["","f","5"],["","g","5"],["","h","5"],
["","a","4"],["","b","4"],["","c","4"],["","d","4"],["","e","4"],["","f","4"],["","g","4"],["","h","4"],
["","a","3"],["","b","3"],["","c","3"],["","d","3"],["","e","3"],["","f","3"],["","g","3"],["","h","3"],
["p","a","2"],["p","b","2"],["p","c","2"],["p","d","2"],["p","e","2"],["p","f","2"],["p","g","2"],["p","h","2"],
["R","a","1"],["N","b","1"],["B","c","1"],["Q","d","1"],["K","e","1"],["B","f","1"],["N","g","1"],["R","h","1"]]
"""0-7"""
"""8-15"""
"""16-23"""
"""24-31"""
"""32-39"""
"""40-47"""
"""48-55"""
"""56-63"""
# fh = open("C:\\Users\\mwasy\\OneDrive\\Pulpit\\\pgny\\partia.txt", "w")
k=1
begin = -1
end = -1
castlekingside = False
castlequeenside = False
def checkingcastle (cXlist, cYlist):
    if cXlist[0] > coordinates[22][0] and cXlist[0] < coordinates[30][0] and cYlist[0] > coordinates[22][1] and cYlist[0] < coordinates[23][1] and cXlist[0] > coordinates[30][0] and cXlist[0] < coordinates[38][0] and cYlist[0] > coordinates[30][1] and cYlist[0] < coordinates[31][1]:
        castlekingside = True
    if cXlist[1] > coordinates[22][0] and cXlist[1] < coordinates[30][0] and cYlist[1] > coordinates[22][1] and cYlist[1] < coordinates[23][1] and cXlist[1] > coordinates[30][0] and cXlist[1] < coordinates[38][0] and cYlist[1] > coordinates[30][1] and cYlist[1] < coordinates[31][1]:
        castlekingside = True
def checkingfigurepositionbefore (begin):
    for i in range(7):

        if cXlist[1] > coordinates[i*8][0] and cXlist[1] < coordinates[i*8+8][0] and cYlist[1] < coordinates[i*8][1]:
            print("8")
            begin = 0+i
        if cXlist[1] > coordinates[i*8][0] and cXlist[1] < coordinates[i*8+8][0] and cYlist[1] > coordinates[i*8][
            1] and cYlist[1] < coordinates[i*8+1][1]:
            print("7")
            begin = 8+i
        if cXlist[1] > coordinates[i*8+1][0] and cXlist[1] < coordinates[i*8+9][0] and cYlist[1] > coordinates[i*8+1][
            1] and cYlist[1] < coordinates[i*8+2][1]:
            print("6")
            begin = 16+i
        if cXlist[1] > coordinates[i*8+2][0] and cXlist[1] < coordinates[i*8+10][0] and cYlist[1] > coordinates[i*8+2][
            1] and cYlist[1] < coordinates[i*8+3][1]:
            print("5")
            begin = 24+i
        if cXlist[1] > coordinates[i*8+3][0] and cXlist[1] < coordinates[i*8+11][0] and cYlist[1] > coordinates[i*8+3][
            1] and cYlist[1] < coordinates[i*8+4][1]:
            print("4")
            begin = 32+i
        if cXlist[1] > coordinates[i*8+4][0] and cXlist[1] < coordinates[i*8+12][0] and cYlist[1] > coordinates[i*8+4][
            1] and cYlist[1] < coordinates[i*8+5][1]:
            print("3")
            begin = 40+i
        if cXlist[1] > coordinates[i*8+5][0] and cXlist[1] < coordinates[i*8+13][0] and cYlist[1] > coordinates[i*8+5][
            1] and cYlist[1] < coordinates[i*8+6][1]:
            print("2")
            begin = 48+i
        if cXlist[1] > coordinates[i*8+6][0] and cXlist[1] < coordinates[i*8+14][0] and cYlist[1] > coordinates[i*8+6][
            1] and cYlist[1] < coordinates[i*8+7][1]:
            print("1")
            begin = 56+i
    if cXlist[1] > coordinates[56][0] and cXlist[1] < coordinates[56][0]+70 and cYlist[1] < coordinates[56][1]:
        print("8")
        begin = 7
    if cXlist[1] > coordinates[56][0] and cXlist[1] < coordinates[56][0]+70 and cYlist[1] > coordinates[56][1] and cYlist[1] < coordinates[57][1]:
        print("7")
        begin = 15
    if cXlist[1] > coordinates[57][0] and cXlist[1] < coordinates[57][0]+70 and cYlist[1] > coordinates[57][1] and cYlist[1] < coordinates[58][1]:
        print("6")
        begin = 23
    if cXlist[1] > coordinates[58][0] and cXlist[1] < coordinates[58][0]+70 and cYlist[1] > coordinates[58][1] and cYlist[1] < coordinates[59][1]:
        print("5")
        begin = 31
    if cXlist[1] > coordinates[59][0] and cXlist[1] < coordinates[59][0]+70 and cYlist[1] > coordinates[59][1] and cYlist[1] < coordinates[60][1]:
        print("4")
        begin = 39
    if cXlist[1] > coordinates[60][0] and cXlist[1] < coordinates[60][0]+70 and cYlist[1] > coordinates[60][1] and cYlist[1] < coordinates[61][1]:
        print("3")
        begin = 47
    if cXlist[1] > coordinates[61][0] and cXlist[1] < coordinates[61][0]+70 and cYlist[1] > coordinates[61][1] and cYlist[1] < coordinates[62][1]:
        print("2")
        begin = 55
    if cXlist[1] > coordinates[62][0] and cXlist[1] < coordinates[62][0] and cYlist[1] > coordinates[62][1] and cYlist[1] < coordinates[63][1]:
        print("1")
        begin = 63
    return begin

def checkingfigurepositionafter(end):
    for i in range(7):

        if cXlist[0] > coordinates[i*8][0] and cXlist[0] < coordinates[i*8+8][0] and cYlist[0] < coordinates[i*8][1]:
            print("8")
            end = 0+i
        if cXlist[0] > coordinates[i*8][0] and cXlist[0] < coordinates[i*8+8][0] and cYlist[0] > coordinates[i*8][
            1] and cYlist[0] < coordinates[i*8+1][1]:
            print("7")
            end = 8+i
        if cXlist[0] > coordinates[i*8+1][0] and cXlist[0] < coordinates[i*8+9][0] and cYlist[0] > coordinates[i*8+1][
            1] and cYlist[0] < coordinates[i*8+2][1]:
            print("6")
            end = 16+i
        if cXlist[0] > coordinates[i*8+2][0] and cXlist[0] < coordinates[i*8+10][0] and cYlist[0] > coordinates[i*8+2][
            1] and cYlist[0] < coordinates[i*8+3][1]:
            print("5")
            end = 24+i
        if cXlist[0] > coordinates[i*8+3][0] and cXlist[0] < coordinates[i*8+11][0] and cYlist[0] > coordinates[i*8+3][
            1] and cYlist[0] < coordinates[i*8+4][1]:
            print("4")
            end = 32+i
        if cXlist[0] > coordinates[i*8+4][0] and cXlist[0] < coordinates[i*8+12][0] and cYlist[0] > coordinates[i*8+4][
            1] and cYlist[0] < coordinates[i*8+5][1]:
            print("3")
            end = 40+i
        if cXlist[0] > coordinates[i*8+5][0] and cXlist[0] < coordinates[i*8+13][0] and cYlist[0] > coordinates[i*8+5][
            1] and cYlist[0] < coordinates[i*8+6][1]:
            print("2")
            end = 48+i
        if cXlist[0] > coordinates[i*8+6][0] and cXlist[0] < coordinates[i*8+14][0] and cYlist[0] > coordinates[i*8+6][
            1] and cYlist[0] < coordinates[i*8+7][1]:
            print("1")
            end = 56+i

    if cXlist[0] > coordinates[56][0] and cXlist[0] < coordinates[56][0]+70 and cYlist[0] < coordinates[56][1]:
        print("8")
        end = 7
    if cXlist[0] > coordinates[56][0] and cXlist[0] < coordinates[56][0]+70 and cYlist[0] > coordinates[56][1] and cYlist[0] < coordinates[57][1]:
        print("7")
        end = 15
    if cXlist[0] > coordinates[57][0] and cXlist[0] < coordinates[57][0]+70 and cYlist[0] > coordinates[57][1] and cYlist[0] < coordinates[58][1]:
        print("6")
        end = 23
    if cXlist[0] > coordinates[58][0] and cXlist[0] < coordinates[58][0]+70 and cYlist[0] > coordinates[58][1] and cYlist[0] < coordinates[59][1]:
        print("5")
        end = 31
    if cXlist[0] > coordinates[59][0] and cXlist[0] < coordinates[59][0]+70 and cYlist[0] > coordinates[59][1] and cYlist[0] < coordinates[60][1]:
        print("4")
        end = 39
    if cXlist[0] > coordinates[60][0] and cXlist[0] < coordinates[60][0]+70 and cYlist[0] > coordinates[60][1] and cYlist[0] < coordinates[61][1]:
        print("3")
        end = 47
    if cXlist[0] > coordinates[61][0] and cXlist[0] < coordinates[61][0]+70 and cYlist[0] > coordinates[61][1] and cYlist[0] < coordinates[62][1]:
        print("2")
        end = 55
    if cXlist[0] > coordinates[62][0] and cXlist[0] < coordinates[62][0]+70 and cYlist[0] > coordinates[62][1] and cYlist[0] < coordinates[63][1]:
        print("1")
        end = 63
    return end


# def finding_center_of_change_black_on_board (subtractBlackcopy):
#     # find contours in the thresholded image
#     cnts = cv2.findContours(subtractBlackcopy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     # loop over the contours
#     for c in cnts:
#         # compute the center of the contour
#         if cv2.contourArea(c) > 3:
#             # process the contour
#             M = cv2.moments(c)
#             cX = int(M["m10"] / M["m00"])
#             cY = int(M["m01"] / M["m00"])
#             # draw the contour and center of the shape on the image
#             cv2.drawContours(subtractBlackcopy, [c], -1, (0, 255, 0), 2)
#             cv2.circle(subtractBlackcopy, (cX, cY), 7, (0, 0, 255), -1)
#             cv2.putText(subtractBlackcopy, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#             area = cv2.contourArea(c)
#             area = str(area)
#             cv2.putText(subtractBlackcopy, area, (cX - 20, cY + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#     return subtractBlackcopy
# def finding_center_of_change_white_on_board (subtractWhitecopy):
#     # # find contours in the thresholded image
#     # subtractWhitecopy = cv2.cvtColor(subtractWhitecopy, cv2.COLOR_HSV2GRAY)
#     cnts = cv2.findContours(subtractWhitecopy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     # subtractWhitecopy = cv2.COLOR(subtractWhitecopy, cv2.COLOR_GRAY2BGR)
#
#     # loop over the contours
#     for c in cnts:
#         # compute the center of the contour
#         if cv2.contourArea(c) > 10:
#             # process the contour
#             M = cv2.moments(c)
#             cX = int(M["m10"] / M["m00"])
#             cY = int(M["m01"] / M["m00"])
#             # draw the contour and center of the shape on the image
#             cv2.drawContours(subtractWhitecopy, [c], -1, (0, 255, 0), 2)
#             cv2.circle(subtractWhitecopy, (cX, cY), 7, (0, 0, 255), -1)
#             cv2.putText(subtractWhitecopy, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#             area = cv2.contourArea(c)
#             area = str(area)
#             cv2.putText(subtractWhitecopy, area, (cX - 20, cY + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#     return subtractWhitecopy


def whitemove(a,b):
    if  a == 1000 and b == 1000:
        fh.write(str(k) + ". 0-0-0")
        tablica_pól[56][0] = ""
        tablica_pól[60][0] = ""
        tablica_pól[58][0] = "K"
        tablica_pól[59][0] = "R"
    if  a == 100 and b == 100:
        fh.write(str(k) + ". 0-0")
        tablica_pól[60][0] = ""
        tablica_pól[63][0] = ""
        tablica_pól[62][0] = "K"
        tablica_pól[61][0] = "R"
    if a != 1000 and b != 1000 and a != 100 and b !=100:
        if tablica_pól[b][0] == "":
            if tablica_pól[a][0] == "p":
                fh.write(str(k) + ". " + tablica_pól[b][1] + tablica_pól[b][2])
                tablica_pól[b][0] = tablica_pól[a][0]
                tablica_pól[a][0] = ""
            else:
                fh.write(str(k) + ". " + tablica_pól[a][0] + tablica_pól[b][1] + tablica_pól[b][2])
                tablica_pól[b][0] = tablica_pól[a][0]
                tablica_pól[a][0] = ""
        else:
            if tablica_pól[a][0] == "p":
                fh.write(str(k) + ". " + tablica_pól[a][1] + "x" + tablica_pól[b][1] + tablica_pól[b][2])
                tablica_pól[b][0] = tablica_pól[a][0]
                tablica_pól[a][0] = ""
            else:
                fh.write(str(k) + ". " + tablica_pól[a][0] + "x" + tablica_pól[b][1] + tablica_pól[b][2])
                tablica_pól[b][0] = tablica_pól[a][0]
                tablica_pól[a][0] = ""
def blackmove(a,b):
    if  a == 1000 and b == 1000:
        fh.write(" 0-0-0" + "\n")
        tablica_pól[0][0] = ""
        tablica_pól[4][0] = ""
        tablica_pól[2][0] = "K"
        tablica_pól[3][0] = "R"
    if  a == 100 and b == 100:
        fh.write(" 0-0" + "\n")
        tablica_pól[4][0] = ""
        tablica_pól[7][0] = ""
        tablica_pól[6][0] = "K"
        tablica_pól[5][0] = "R"
    if a != 1000 and b != 1000 and a != 100 and b != 100:
        if tablica_pól[b][0] == "":
            if tablica_pól[a][0] == "p":
                fh.write(" " + tablica_pól[b][1] + tablica_pól[b][2] + "\n")
                tablica_pól[b][0] = tablica_pól[a][0]
                tablica_pól[a][0] = ""
            else:
                fh.write(" " + tablica_pól[a][0] + tablica_pól[b][1] + tablica_pól[b][2] + "\n")
                tablica_pól[b][0] = tablica_pól[a][0]
                tablica_pól[a][0] = ""
        else:
            if tablica_pól[a][0] == "p":
                fh.write(" " + tablica_pól[a][1] + "x" + tablica_pól[b][1] + tablica_pól[b][2] + "\n")
                tablica_pól[b][0] = tablica_pól[a][0]
                tablica_pól[a][0] = ""
            else:
                fh.write(" " + tablica_pól[a][0] + "x" + tablica_pól[b][1] + tablica_pól[b][2] + "\n")
                tablica_pól[b][0] = tablica_pól[a][0]
                tablica_pól[a][0] = ""

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def drawCalibrateRect(img):
    cv2.rectangle(img, (640, 360), (715, 435), (255, 0, 0), 2)
    cv2.putText(img, "e4", (640, 420), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0))


def detectCorners(img):
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mycorners = cv2.goodFeaturesToTrack(grayimg, 250, 0.2, 20)
    mycorners = np.int0(mycorners)
    return mycorners

def isOnBoard(x,y):
    return x < 900 and x > 320 and y > 70 and y < 680

def drawCornerMarks(corners,img):
    for corner in corners:
        x, y = corner.ravel()
        if isOnBoard(x,y):
            coordinates.append([x, y])
            img = cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

    return img

def isCalibrationButtonPressed():
    a = cv2.waitKey(1) & 0xFF == ord('r')
    return a

def calibration(img):
    if isCalibrationButtonPressed():
        drawCalibrateRect(img)
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
coordinates = []
framesBLACK = []
framesWHITE = []
frameNumber = 0
oneTime = True
move = 1
cXlist = []
cYlist = []
chessmistake = False
while True:
    # cap = cv2.VideoCapture(0)
    # cap2 = cv2.VideoCapture(0)
    # cap.set(3, 1280)
    # cap.set(4, 720)
    # cap2.set(3, 1280)
    # cap2.set(4, 720)
    success, img_cam = cap.read()
    calibration(img_cam)
    cv2.waitKey(1)


    """img_cam = cv2.rectangle(img_cam, (320, 70), (900, 680), (255, 0, 255), 2)"""
    if len(coordinates) != 64:
        corners = detectCorners(img_cam)
        img_cam = drawCornerMarks(corners,img_cam)
        print("Coordinates length" + str(len(coordinates)))
        coordinates = []
    if len(coordinates) == 64:
        i = 0
        while i < 64:
            img_cam = cv2.circle(img_cam, (coordinates[i][0], coordinates[i][1]), 5, (0, 0, 255), -1)
            i = i + 1
    blackframe = cv2.cvtColor(img_cam, cv2.COLOR_BGR2HSV)
    imgCZARNE = cv2.inRange(blackframe, np.array([81, 82, 0]), np.array([100, 255, 255]))
    whiteframe = cv2.cvtColor(img_cam, cv2.COLOR_BGR2HSV)
    imgBIALE = cv2.inRange(whiteframe, np.array([100, 83, 0]), np.array([130, 255, 255]))
    blackframe = imgCZARNE
    whiteframe = imgBIALE
    # cap.release()
    if move % 2 == 0 and frameNumber>-1:
        a=1
        b=1
        while a==1:
            chessmistake = False
            centerelements = 0
            framesBLACK = []
            framesBLACK.append(blackframe)
            print("Black turn")
            input()
            # success, img_cam_move = cap2.read()
            cv2.waitKey(1)
            # cap2.release()
            success, img_cam = cap.read()
            blackframe2 = cv2.cvtColor(img_cam, cv2.COLOR_BGR2HSV)
            imgCZARNE2 = cv2.inRange(blackframe2, np.array([81, 82, 0]), np.array([100, 255, 255]))
            blackframe2 = imgCZARNE2
            framesBLACK.append(blackframe2)
            print("move % 2 =",move % 2)
            subtractBlack = framesBLACK[1] - framesBLACK[0]
            subtractBlack2 = framesBLACK[0] - framesBLACK[1]
            framesBLACK = []
            subtractBlack = cv2.medianBlur(subtractBlack, 31)
            subtractBlack2 = cv2.medianBlur(subtractBlack2, 31)
            subtractBlackmedianblur = subtractBlack
            subtractBlackmedianblur2 = subtractBlack2
            subtractBlackcopy = subtractBlack
            subtractBlackcopy2 = subtractBlack2
            subtractBlack = cv2.threshold(subtractBlack, 127, 255, cv2.THRESH_BINARY)[1]
            # finding_center_of_change_white_on_board(subtractWhitecopy)
            # find contours in the thresholded image
            cnts = cv2.findContours(subtractBlack.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            centerarea = []
            # subtractWhitecopy = cv2.COLOR(subtractWhitecopy, cv2.COLOR_GRAY2BGR)
            # loop over the contours
            for c in cnts:
                # compute the center of the contour
                if cv2.contourArea(c) > 20:
                    # process the contour
                    M = cv2.moments(c)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    # draw the contour and center of the shape on the image
                    cv2.drawContours(subtractBlackcopy, [c], -1, (255, 255, 255), 2)
                    cv2.drawContours(subtractBlack, [c], -1, (255, 255, 255), 2)
                    # cv2.circle(subtractWhitecopy, (cX, cY), 7, (0, 255, 255), -1)
                    cv2.putText(subtractBlackcopy, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2)
                    if cX > 330 and cX < 950 and cY > 45 and cY < 667:
                        cXlist.append(cX)
                        cYlist.append(cY)
                        area = cv2.contourArea(c)
                        area = str(area)
                        centerarea.append(area)
                        cv2.putText(subtractBlackcopy, area, (cX - 20, cY + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (255, 255, 255),
                                    2)
            centerelements = len(centerarea)
            print(centerelements)

            if centerelements == 2:
                if cXlist[0] > coordinates[16][0] and cXlist[0] < coordinates[24][0] and cYlist[0] < coordinates[17][1] and cXlist[1] > coordinates[24][0] and cXlist[1] < coordinates[32][0] and cYlist[1] < coordinates[25][1] and tablica_pól[0][0] == "R" and tablica_pól[4][0] == "K":
                    castlequeenside = True
                if cXlist[1] > coordinates[16][0] and cXlist[1] < coordinates[24][0] and cYlist[1] < coordinates[17][1] and cXlist[0] > coordinates[24][0] and cXlist[0] < coordinates[32][0] and cYlist[0] < coordinates[25][1] and tablica_pól[0][0] == "R" and tablica_pól[4][0] == "K":
                    castlequeenside = True
                if cXlist[0] > coordinates[40][0] and cXlist[0] < coordinates[48][0] and cYlist[0] < coordinates[41][1] and cXlist[1] > coordinates[48][0] and cXlist[1] < coordinates[56][0] and cYlist[1] < coordinates[49][1] and tablica_pól[7][0] == "R" and tablica_pól[4][0] == "K":
                    castlekingside = True
                if cXlist[1] > coordinates[40][0] and cXlist[1] < coordinates[48][0] and cYlist[1] < coordinates[41][1] and cXlist[0] > coordinates[48][0] and cXlist[0] < coordinates[56][0] and cYlist[0] < coordinates[49][1] and tablica_pól[7][0] == "R" and tablica_pól[4][0] == "K":
                    castlekingside = True


            if centerelements == 1 or castlekingside == True or castlequeenside == True:
                subtractBlack2 = cv2.threshold(subtractBlack2, 127, 255, cv2.THRESH_BINARY)[1]
                # finding_center_of_change_white_on_board(subtractWhitecopy)
                # find contours in the thresholded image
                cnts = cv2.findContours(subtractBlack2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                # subtractWhitecopy = cv2.COLOR(subtractWhitecopy, cv2.COLOR_GRAY2BGR)

                # loop over the contours
                for c in cnts:
                    # compute the center of the contour
                    if cv2.contourArea(c) > 20:
                        # process the contour
                        M = cv2.moments(c)
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        # draw the contour and center of the shape on the image
                        cv2.drawContours(subtractBlackcopy2, [c], -1, (255, 255, 255), 2)
                        cv2.drawContours(subtractBlack, [c], -1, (255, 255, 255), 2)
                        # cv2.circle(subtractWhitecopy, (cX, cY), 7, (0, 255, 255), -1)
                        cv2.putText(subtractBlackcopy2, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (255, 255, 255), 2)
                        if cX > 330 and cX < 950 and cY > 45 and cY < 667:
                            cXlist.append(cX)
                            cYlist.append(cY)
                            area = cv2.contourArea(c)
                            area = str(area)
                            centerarea.append(area)
                            cv2.putText(subtractBlackcopy2, area, (cX - 20, cY + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (255, 255, 255),
                                        2)
                centerelements = len(centerarea)
                print(centerelements)
                if centerelements == 2 or castlekingside == True or castlequeenside == True:
                    cv2.circle(img_cam, (cXlist[1], cYlist[1]), 20, (0, 0, 255),
                               -1)
                    print(cXlist)
                    print(cYlist)
                    # cXlist[1] skąd sie przemiescila a cXlist[0] dokąd

                    begin = -1

                    end = -1

                    a = 0
                    b = 0
                    if chessmistake == False:

                        begin = checkingfigurepositionbefore(begin)
                        end = checkingfigurepositionafter(end)
                        if castlequeenside == True:
                            begin = 1000
                            end = 1000
                        if castlekingside == True:
                            begin = 100
                            end = 100
                        fh = open("C:\\Users\\mwasy\\OneDrive\\Pulpit\\\pgny\\partia.txt", "a")
                        blackmove(begin, end)
                        fh.close()
                        k = k + 1

                    castlequeenside = False
                    castlekingside = False
                    cXlist = []
                    cYlist = []
                    chessmistake = False

                if centerelements != 2 and centerelements != 4:
                    print("Prosze ustawić jeszcze raz")
                    input()
                    centerelements = 0
                    chessmistake = True



            if centerelements != 1 and b!=0:
                cXlist = []
                cYlist = []
                print("Prosze ustawić jeszcze raz")
                input()
                chessmistake = True

        # cv2.imshow("Kamerka", subtractBlack)
    if move % 2 == 1 and frameNumber>-1:
        a=1
        b=1
        while a==1:
            chessmistake = False
            centerelements = 0
            framesWHITE = []
            framesWHITE.append(whiteframe)
            print("White turn")
            input()
            # success, img_cam_move = cap2.read()
            cv2.waitKey(1)
            # cap2.release()
            success, img_cam = cap.read()
            whiteframe2 = cv2.cvtColor(img_cam, cv2.COLOR_BGR2HSV)
            imgBIALE2 = cv2.inRange(whiteframe2, np.array([100, 83, 0]), np.array([130, 255, 255]))
            whiteframe2 = imgBIALE2
            framesWHITE.append(whiteframe2)
            print("move % 2 =",move % 2)
            subtractWhite = framesWHITE[1] - framesWHITE[0]
            subtractWhite2 = framesWHITE[0] - framesWHITE[1]
            framesWHITE = []
            subtractWhite = cv2.medianBlur(subtractWhite, 31)
            subtractWhite2 = cv2.medianBlur(subtractWhite2, 31)
            subtractWhitemedianblur = subtractWhite
            subtractWhitemedianblur2 = subtractWhite2
            subtractWhitecopy = subtractWhite
            subtractWhitecopy2 = subtractWhite2
            subtractWhite = cv2.threshold(subtractWhite, 127, 255, cv2.THRESH_BINARY)[1]
            # finding_center_of_change_white_on_board(subtractWhitecopy)
            # find contours in the thresholded image
            cnts = cv2.findContours(subtractWhite.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            centerarea = []
            # subtractWhitecopy = cv2.COLOR(subtractWhitecopy, cv2.COLOR_GRAY2BGR)

            # loop over the contours
            for c in cnts:
                # compute the center of the contour
                if cv2.contourArea(c) > 50:
                    # process the contour
                    M = cv2.moments(c)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    # draw the contour and center of the shape on the image
                    cv2.drawContours(subtractWhitecopy, [c], -1, (255, 255, 255), 2)
                    cv2.drawContours(subtractWhite, [c], -1, (255, 255, 255), 2)
                    # cv2.circle(subtractWhitecopy, (cX, cY), 7, (0, 255, 255), -1)
                    cv2.putText(subtractWhitecopy, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2)
                    if cX > 330 and cX < 950 and cY > 45 and cY < 667:
                        cXlist.append(cX)
                        cYlist.append(cY)
                        area = cv2.contourArea(c)
                        area = str(area)
                        centerarea.append(area)
                        cv2.putText(subtractWhitecopy, area, (cX - 20, cY + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (255, 255, 255),
                                    2)
            centerelements = len(centerarea)
            print(centerelements)
            coordinates = [[331, 124], [331, 200], [331, 280], [331, 355], [330, 436], [330, 511], [330, 591],
                           [329, 667],
                           [408, 125], [408, 201], [408, 281], [409, 358], [409, 434], [407, 513], [408, 589],
                           [406, 667],
                           [487, 124], [488, 204], [486, 281], [487, 358], [487, 435], [485, 514], [486, 592],
                           [486, 667],
                           [564, 128], [566, 203], [564, 283], [564, 358], [563, 437], [563, 514], [564, 590],
                           [562, 667],
                           [644, 128], [644, 203], [643, 283], [641, 360], [641, 436], [641, 514], [642, 593],
                           [641, 668],
                           [719, 130], [719, 205], [719, 284], [720, 359], [718, 438], [719, 515], [719, 590],
                           [716, 667],
                           [798, 130], [796, 207], [797, 284], [797, 361], [796, 438], [796, 513], [795, 592],
                           [795, 667],
                           [873, 131], [872, 206], [872, 285], [871, 360], [871, 438], [872, 515], [870, 592],
                           [869, 666]]
            if centerelements == 2:
                if cXlist[0] > coordinates[22][0] and cXlist[0] < coordinates[30][0] and cYlist[0] > coordinates[22][1] and cYlist[0] < coordinates[23][1] and cXlist[1] > coordinates[30][0] and cXlist[1] < coordinates[38][0] and cYlist[1] > coordinates[30][1] and cYlist[1] < coordinates[31][1] and tablica_pól[56][0] == "R" and tablica_pól[60][0] == "K":
                    castlequeenside = True
                if cXlist[1] > coordinates[22][0] and cXlist[1] < coordinates[30][0] and cYlist[1] > coordinates[22][1] and cYlist[1] < coordinates[23][1] and cXlist[0] > coordinates[30][0] and cXlist[0] < coordinates[38][0] and cYlist[0] > coordinates[30][1] and cYlist[0] < coordinates[31][1] and tablica_pól[56][0] == "R" and tablica_pól[60][0] == "K":
                    castlequeenside = True
                if cXlist[0] > coordinates[46][0] and cXlist[0] < coordinates[54][0] and cYlist[0] > coordinates[46][1] and cYlist[0] < coordinates[47][1] and cXlist[1] > coordinates[54][0] and cXlist[1] < coordinates[62][0] and cYlist[1] > coordinates[54][1] and cYlist[1] < coordinates[55][1] and tablica_pól[63][0] == "R" and tablica_pól[60][0] == "K":
                    castlekingside = True
                if cXlist[1] > coordinates[46][0] and cXlist[1] < coordinates[54][0] and cYlist[1] > coordinates[46][1] and cYlist[1] < coordinates[47][1] and cXlist[0] > coordinates[54][0] and cXlist[0] < coordinates[62][0] and cYlist[0] > coordinates[54][1] and cYlist[0] < coordinates[55][1] and tablica_pól[63][0] == "R" and tablica_pól[60][0] == "K":
                    castlekingside = True

            if centerelements == 1 or castlekingside == True or castlequeenside == True:
                subtractWhite2 = cv2.threshold(subtractWhite2, 127, 255, cv2.THRESH_BINARY)[1]
                # finding_center_of_change_white_on_board(subtractWhitecopy)
                # find contours in the thresholded image
                cnts = cv2.findContours(subtractWhite2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                # subtractWhitecopy = cv2.COLOR(subtractWhitecopy, cv2.COLOR_GRAY2BGR)

                # loop over the contours
                for c in cnts:
                    # compute the center of the contour
                    if cv2.contourArea(c) > 50:
                        # process the contour
                        M = cv2.moments(c)
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        # draw the contour and center of the shape on the image
                        cv2.drawContours(subtractWhitecopy2, [c], -1, (255, 255, 255), 2)
                        cv2.drawContours(subtractWhite, [c], -1, (255, 255, 255), 2)
                        # cv2.circle(subtractWhitecopy, (cX, cY), 7, (0, 255, 255), -1)
                        cv2.putText(subtractWhitecopy2, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (255, 255, 255), 2)
                        if cX > 330 and cX < 950 and cY > 45 and cY < 667:
                            cXlist.append(cX)
                            cYlist.append(cY)
                            area = cv2.contourArea(c)
                            area = str(area)
                            centerarea.append(area)
                            cv2.putText(subtractWhitecopy2, area, (cX - 20, cY + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (255, 255, 255),
                                        2)
                centerelements = len(centerarea)
                print(centerelements)
                coordinates = [[331, 124], [331, 200], [331, 280], [331, 355], [330, 436], [330, 511], [330, 591],
                               [329, 667], [408, 125], [408, 201], [408, 281], [409, 358], [409, 434], [407, 513],
                               [408, 589], [406, 667], [487, 124], [488, 204], [486, 281], [487, 358], [487, 435],
                               [485, 514], [486, 592], [486, 667], [564, 128], [566, 203], [564, 283], [564, 358],
                               [563, 437], [563, 514], [564, 590], [562, 667], [644, 128], [644, 203], [643, 283],
                               [641, 360], [641, 436], [641, 514], [642, 593], [641, 668], [719, 130], [719, 205],
                               [719, 284], [720, 359], [718, 438], [719, 515], [719, 590], [716, 667], [798, 130],
                               [796, 207], [797, 284], [797, 361], [796, 438], [796, 513], [795, 592], [795, 667],
                               [873, 131], [872, 206], [872, 285], [871, 360], [871, 438], [872, 515], [870, 592],
                               [869, 666]]

                if centerelements == 2 or castlekingside == True or castlequeenside == True:
                    cv2.circle(img_cam, (cXlist[1], cYlist[1]), 20, (0, 0, 255),
                               -1)
                    print(cXlist)
                    print(cYlist)

                    begin = -1

                    end = -1


                    a = 0
                    b = 0
                    if chessmistake == False:
                        begin = checkingfigurepositionbefore(begin)
                        end = checkingfigurepositionafter(end)
                        if castlequeenside == True:
                            begin = 1000
                            end = 1000
                        if castlekingside == True:
                            begin = 100
                            end = 100
                        fh = open("C:\\Users\\mwasy\\OneDrive\\Pulpit\\\pgny\\partia.txt", "a")
                        whitemove(begin, end)
                        fh.close()
                    castlekingside = False
                    castlequeenside = False
                    cXlist = []
                    cYlist = []
                    chessmistake = False

                if centerelements != 2 and centerelements != 4:
                    print("Prosze ustawic jeszcze raz")
                    input()
                    centerelements = 0
                    chessmistake = True



            if centerelements != 1 and b!=0:
                cXlist = []
                cYlist = []
                print("Prosze ustawic jeszcze raz")
                input()
                chessmistake = True



        # cv2.imshow("Kamerka",subtractWhite)
        # cv2.imshow("Kamerka", imgStack)

    # if frameNumber == 5:
    #     framesBLACK.append(blackframe)
    #     framesWHITE.append(whiteframe)
    if frameNumber > -1:
        coordinates = [[331, 124], [331, 200], [331, 280], [331, 355], [330, 436], [330, 511], [330, 591], [329, 667],
                       [408, 125], [408, 201], [408, 281], [409, 358], [409, 434], [407, 513], [408, 589], [406, 667],
                       [487, 124], [488, 204], [486, 281], [487, 358], [487, 435], [485, 514], [486, 592], [486, 667],
                       [564, 128], [566, 203], [564, 283], [564, 358], [563, 437], [563, 514], [564, 590], [562, 667],
                       [644, 128], [644, 203], [643, 283], [641, 360], [641, 436], [641, 514], [642, 593], [641, 668],
                       [719, 130], [719, 205], [719, 284], [720, 359], [718, 438], [719, 515], [719, 590], [716, 667],
                       [798, 130], [796, 207], [797, 284], [797, 361], [796, 438], [796, 513], [795, 592], [795, 667],
                       [873, 131], [872, 206], [872, 285], [871, 360], [871, 438], [872, 515], [870, 592], [869, 666]]
        if move % 2 == 1 and frameNumber > -1:
            # subtractWhite = framesWHITE[frameNumber] - framesWHITE[frameNumber - 1]
            # subtractWhite = cv2.medianBlur(subtractWhite, 31)
            j = 0
            while j < 64:
                subtractWhite = cv2.circle(subtractWhite, (coordinates[j][0], coordinates[j][1]), 2, (255, 255, 255),
                                           -1)
                j = j + 1
            subtractWhite = cv2.circle(subtractWhite, (331, 45), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (408, 45), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (487, 45), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (566, 45), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (644, 45), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (719, 45), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (796, 45), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (873, 45), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (950, 45), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (950, 124), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (950, 200), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (950, 280), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (950, 355), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (950, 436), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (950, 511), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (950, 591), 2, (255, 255, 255), -1)
            subtractWhite = cv2.circle(subtractWhite, (950, 667), 2, (255, 255, 255), -1)
            imgStack = stackImages(0.5, ([img_cam],[subtractWhite]))

        if move % 2 == 0 and frameNumber > -1:
            # subtractBlack = framesBLACK[frameNumber] - framesBLACK[frameNumber - 1]
            # subtractBlack = cv2.medianBlur(subtractBlack, 31)
            j = 0
            while j < 64:
                subtractBlack = cv2.circle(subtractBlack, (coordinates[j][0], coordinates[j][1]), 2, (255, 255, 255),
                                           -1)
                j = j + 1
            subtractBlack = cv2.circle(subtractBlack, (331, 45), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (408, 45), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (487, 45), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (566, 45), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (644, 45), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (719, 45), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (796, 45), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (873, 45), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (950, 45), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (950, 124), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (950, 200), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (950, 280), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (950, 355), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (950, 436), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (950, 511), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (950, 591), 2, (255, 255, 255), -1)
            subtractBlack = cv2.circle(subtractBlack, (950, 667), 2, (255, 255, 255), -1)
            imgStack = stackImages(0.5, ([img_cam],[subtractBlack]))
        #cv2.imshow("Kamerka", imgStack)
    # if frameNumber < 1:
    #     imgStack = stackImages(0.5, ([img_cam], [img_cam]))

    frameNumber = frameNumber + 1
    move = move+1
    cv2.imwrite('C:\\Users\\mwasy\\OneDrive\\Pulpit\\chessgame\\save.jpg', imgStack)
    cv2.imshow("Kamerka", imgStack)

    if len(coordinates) == 64 and oneTime == True:
        coordinates.sort(key=lambda i: i[0])
        line_a = coordinates[0:8]
        line_a.sort(key=lambda i: i[1])
        line_b = coordinates[8:16]
        line_b.sort(key=lambda i: i[1])
        line_c = coordinates[16:24]
        line_c.sort(key=lambda i: i[1])
        line_d = coordinates[24:32]
        line_d.sort(key=lambda i: i[1])
        line_e = coordinates[32:40]
        line_e.sort(key=lambda i: i[1])
        line_f = coordinates[40:48]
        line_f.sort(key=lambda i: i[1])
        line_g = coordinates[48:56]
        line_g.sort(key=lambda i: i[1])
        line_h = coordinates[56:64]
        line_h.sort(key=lambda i: i[1])
        print(coordinates)
        print(line_a)
        print(line_b)
        print(line_c)
        print(line_d)
        print(line_e)
        print(line_f)
        print(line_g)
        print(line_h)
        coordinates = []
        "coordinates = line_a+line_b+line_c+line_d+line_e+line_f+line_g+line_h"
        coordinates = [[331, 124], [331, 200], [331, 280], [331, 355], [330, 436], [330, 511], [330, 591], [329, 667], [408, 125], [408, 201], [408, 281], [409, 358], [409, 434], [407, 513], [408, 589], [406, 667], [487, 124], [488, 204], [486, 281], [487, 358], [487, 435], [485, 514], [486, 592], [486, 667], [564, 128], [566, 203], [564, 283], [564, 358], [563, 437], [563, 514], [564, 590], [562, 667], [644, 128], [644, 203], [643, 283], [641, 360], [641, 436], [641, 514], [642, 593], [641, 668], [719, 130], [719, 205], [719, 284], [720, 359], [718, 438], [719, 515], [719, 590], [716, 667], [798, 130], [796, 207], [797, 284], [797, 361], [796, 438], [796, 513], [795, 592], [795, 667], [873, 131], [872, 206], [872, 285], [871, 360], [871, 438], [872, 515], [870, 592], [869, 666]]
        print(coordinates)
        oneTime = False
