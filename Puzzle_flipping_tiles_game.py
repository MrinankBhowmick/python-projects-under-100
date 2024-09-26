#Import Modules
import random
import pygame
import sys
from pygame.locals import *








# Main Function
def main():
    global Frame_Speed_Clock, DIS_PlaySurf
    pygame.init()
    Frame_Speed_Clock = pygame.time.Clock()
    DIS_PlaySurf = pygame.display.set_mode((Window_Width, Window_Height))
 
    X_mouse  = 0 
    Y_mouse = 0 
    pygame.display.set_caption('Memory Game by PythonGeeks')
 
    Board = Randomized_Board()
    Boxes_revealed = GenerateData_RevealedBoxes(False)
 
    first_Selection = None  
    DIS_PlaySurf.fill(BackGround_color)
    Start_Game(Board)
 
    while True: 
        mouse_Clicked = False
 
        DIS_PlaySurf.fill(BackGround_color) 
        Draw_Board(Board, Boxes_revealed)
 
        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                X_mouse, Y_mouse = event.pos
            elif event.type == MOUSEBUTTONUP:
                X_mouse, Y_mouse = event.pos
                mouse_Clicked = True
 
        x_box, y_box = Box_Pixel(X_mouse, Y_mouse)
        if x_box != None and y_box != None:
            if not Boxes_revealed[x_box][y_box]:
                Draw_HighlightBox(x_box, y_box)
            if not Boxes_revealed[x_box][y_box] and mouse_Clicked:
                Reveal_Boxes_Animation(Board, [(x_box, y_box)])
                Boxes_revealed[x_box][y_box] = True 
                if first_Selection == None: 
                    first_Selection = (x_box, y_box)
                else:
                    icon1shape, icon1color = get_Shape_Color(Board, first_Selection[0], first_Selection[1])
                    icon2shape, icon2color = get_Shape_Color(Board, x_box, y_box)
 
                    if icon1shape != icon2shape or icon1color != icon2color:
                        pygame.time.wait(1000) 
                        Cover_Boxes_Animation(Board, [(first_Selection[0], first_Selection[1]), (x_box, y_box)])
                        Boxes_revealed[first_Selection[0]][first_Selection[1]] = False
                        Boxes_revealed[x_box][y_box] = False
                    elif Won(Boxes_revealed): 
                        Game_Won(Board)
                        pygame.time.wait(2000)
 
                        Board = Randomized_Board()
                        Boxes_revealed = GenerateData_RevealedBoxes(False)
                        Draw_Board(Board, Boxes_revealed)
                        pygame.display.update()
                        pygame.time.wait(1000)
 
                        Start_Game (Board)
                    first_Selection = None 
        pygame.display.update()
        Frame_Speed_Clock.tick(Frame_Speed)












#Creating Revealed box function
def GenerateData_RevealedBoxes(val):
    Boxes_revealed = []
    for i in range(Border_Width):
        Boxes_revealed.append([val] * Border_Height)
    return Boxes_revealed









# Creating a board
def Randomized_Board():
    icon = []
    for color in All_Colors:
        for shape in All_Shapes:
            icon.append( (shape, color) )
 
    random.shuffle(icon) 
    num_IconsUsed = int(Border_Width * Border_Height / 2) 
    icon = icon[:num_IconsUsed] * 2 
    random.shuffle(icon)
 
    board = []
    for x in range(Border_Width):
        column = []
        for y in range(Border_Height):
            column.append(icon[0])
            del icon[0] 
        board.append(column)
    return board








# Splitting a list into lists
def Split_Groups(group_Size, List):
    result = []
    for i in range(0, len(List), group_Size):
        result.append(List[i:i + group_Size])
    return result









# Create coordinate function
def leftTop_Coord(x_box, y_box):
    left = x_box * (Box_Size + Gap_Size) + X_margin
    top = y_box * (Box_Size + Gap_Size) + Y_margin
    return (left, top)










#Converting to pixel coordinates to box coordinates
def Box_Pixel(x, y):
    for x_box in range(Border_Width):
        for y_box in range(Border_Height):
            left, top = leftTop_Coord(x_box, y_box)
            box_Rect = pygame.Rect(left, top, Box_Size, Box_Size)
            if box_Rect.collidepoint(x, y):
                return (x_box, y_box)
    return (None, None)









# Draw icon and synthetic sugar
def Draw_Icon(shape, color, x_box, y_box):
    quarter = int(Box_Size * 0.25) 
    half    = int(Box_Size * 0.5)  
 
    left, top = leftTop_Coord(x_box, y_box) 
 
    if shape == CIRCLE:
        pygame.draw.circle(DIS_PlaySurf, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DIS_PlaySurf, BackGround_color, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DIS_PlaySurf, color, (left + quarter, top + quarter, Box_Size - half, Box_Size - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DIS_PlaySurf, color, ((left + half, top), (left + Box_Size - 1, top + half), (left + half, top + Box_Size - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, Box_Size, 4):
            pygame.draw.line(DIS_PlaySurf, color, (left, top + i), (left + i, top))
            pygame.draw.line(DIS_PlaySurf, color, (left + i, top + Box_Size - 1), (left + Box_Size - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DIS_PlaySurf, color, (left, top + quarter, Box_Size, half))
 
def get_Shape_Color(board, x_box, y_box):
    return board[x_box][y_box][0], board[x_box][y_box][1]









#Drawing box cover
def Box_Cover(board, boxes, coverage):
    for box in boxes:
        left, top = leftTop_Coord(box[0], box[1])
        pygame.draw.rect(DIS_PlaySurf, BackGround_color, (left, top, Box_Size, Box_Size))
        shape, color = get_Shape_Color(board, box[0], box[1])
        Draw_Icon(shape, color, box[0], box[1])
        if coverage > 0: # only draw the cover if there is an coverage
            pygame.draw.rect(DIS_PlaySurf, Box_Color, (left, top, coverage, Box_Size))
    pygame.display.update()
    Frame_Speed_Clock.tick(Frame_Speed)









#Revealing and covering animation
def Reveal_Boxes_Animation(board, boxesToReveal):
    for coverage in range(Box_Size, (-Speed_Reveal) - 1, -Speed_Reveal):
        Box_Cover(board, boxesToReveal, coverage)
 
def Cover_Boxes_Animation(board, boxesToCover):
    for coverage in range(0, Box_Size + Speed_Reveal, Speed_Reveal):
        Box_Cover(board, boxesToCover, coverage)









#Drawing entire board and Highlight
def Draw_Board(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for x_box in range(Border_Width):
        for y_box in range(Border_Height):
            left, top = leftTop_Coord(x_box, y_box)
            if not revealed[x_box][y_box]:                pygame.draw.rect(DIS_PlaySurf, Box_Color, (left, top, Box_Size, Box_Size))
            else:
                shape, color = get_Shape_Color(board, x_box, y_box)
                Draw_Icon(shape, color, x_box, y_box)
 
def Draw_HighlightBox(x_box, y_box):
    left, top = leftTop_Coord(x_box, y_box)
    pygame.draw.rect(DIS_PlaySurf, HighLight_Color, (left - 5, top - 5, Box_Size + 10, Box_Size + 10), 4)









#Start the game animation
def Start_Game(board):
    covered_Boxes = GenerateData_RevealedBoxes(False)
    boxes = []
    for x in range(Border_Width):
        for y in range(Border_Height):
            boxes.append( (x, y) )
    random.shuffle(boxes)
    box_Groups = Split_Groups(8, boxes)
 
    Draw_Board(board, covered_Boxes)
    for boxGroup in box_Groups:
        Reveal_Boxes_Animation(board, boxGroup)
        Cover_Boxes_Animation(board, boxGroup)









#Creating function for game won
def Game_Won (board):
    coveredBoxes = GenerateData_RevealedBoxes(True)
    color_1 = Light_BackGround_color
    color_2 = BackGround_color
 
    for i in range(13):
        color_1, color_2 = color_2, color_1 
        DIS_PlaySurf.fill(color_1)
        Draw_Board(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)
 
def Won(Boxes_revealed):
    # Returns True if all the boxes have been revealed, otherwise False
    for i in Boxes_revealed:
        if False in i:
            return False 
    return True








Frame_Speed = 30 
Window_Width = 640 
Window_Height = 480
Speed_Reveal = 8 
Box_Size = 40 
Gap_Size = 10 
Border_Width = 10 
Border_Height = 7 
 
assert (Border_Width * Border_Height) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
X_margin = int((Window_Width - (Border_Width * (Box_Size + Gap_Size))) / 2)
Y_margin = int((Window_Height - (Border_Height * (Box_Size + Gap_Size))) / 2)
 
#            R    G    B
Gray     = (100, 100, 100)
Navyblue = ( 60,  60, 100)
White    = (255, 255, 255)
Red      = (255,   0,   0)
Green    = (  0, 255,   0)
Blue     = (  0,   0, 255)
Yellow   = (255, 255,   0)
Orange   = (255, 128,   0)
Purple   = (255,   0, 255)
Cyan     = (  0, 255, 255)
 
BackGround_color = Gray
Light_BackGround_color = Navyblue
Box_Color = Cyan
HighLight_Color = Yellow
 
CIRCLE = 'circle'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'
 
All_Colors = (Red, Green, Blue, Yellow, Orange, Purple, Cyan)
All_Shapes = (CIRCLE, SQUARE, DIAMOND, LINES, OVAL)
assert len(All_Colors)* len(All_Shapes) * 2 >= Border_Width * Border_Height, "Board is too big for the number of shapes/colors defined.”
 
if __name__ == '__main__':
    main()
