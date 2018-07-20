import os
from plane_Sprite import *


class Game:

    def __init__(self):
        print("init")
        # set location
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % WINDOW_LOCATION
        pygame.init()
        self.window = pygame.display.set_mode(WINDOW.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FILE_EVENT, 500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("start")

        while(True):
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__update_sprites()
            pygame.display.update()
            self.__check_collide()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.__game_over()
            elif event.type == ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FILE_EVENT:
                self.hero.fire()

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif key[pygame.K_LEFT]:
            self.hero.speed = -2
        elif key[pygame.K_UP]:
            self.hero.speed = -2
        elif key[pygame.K_DOWN]:
            self.hero.speed = -2

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            Game.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.window)
        self.enemy_group.update()
        self.enemy_group.draw(self.window)
        self.hero_group.update()
        self.hero_group.draw(self.window)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.window)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = Game()
    game.start_game()
    pass
