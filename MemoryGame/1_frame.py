# pip install pygame

import pygame

# 초기화
pygame.init()
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기
# 실제 화면 구성을 튜플형태에 넣음
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 게임 루프
## 사용자가 키보드랑 마우스를 사용했는지 확인하다가 게임 종료조건이 되면 탈출
running = True # 게임이 실행중인가?
while running:
    # 이벤트 루프(사용자의 동작을 지켜보는)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False # 게임이 더 이상 실행중이 아님

# 게임 종료
pygame.quit()