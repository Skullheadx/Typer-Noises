import pygame

pygame.init()

WIDTH, HEIGHT = 720, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bee Movie Typer")

COMMAND_EXIT = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

clock = pygame.time.Clock()
delta = 0


class Words:
    with open("BeeMovieScript.txt", "r") as f:
        script = f.read()

    font = pygame.font.Font("MonospaceTypewriter.ttf", 10)

    lines = script.split('\n')

    def __init__(self):
        self.words = [self.font.render(word, True, GRAY) for word in self.lines]
        self.index = 0
        self.typed_words = [""]
        self.display_words = [self.font.render("", True, BLACK)]

    def update(self, delta):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                return COMMAND_EXIT
            elif event.type == pygame.TEXTINPUT:
                char = event.text
                self.typed_words[-1] += char
                self.display_words[-1] = self.font.render(self.typed_words[-1], True, BLACK, WHITE)
                if char == self.script[self.index]:
                    self.index += 1

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.typed_words[-1] = self.typed_words[-1][:-1]
                    self.display_words[-1] = self.font.render(self.typed_words[-1], True, BLACK, WHITE)

                elif event.key == pygame.K_RETURN:
                    self.typed_words.append("")
                    self.display_words.append(self.font.render("", True, BLACK))

    def draw(self, surf):
        surf.fill(WHITE)
        prev = pygame.Vector2(0, 0)
        for word in self.words:
            surf.blit(word, word.get_rect(topleft=prev))
            prev.y += word.get_height()
        prev = pygame.Vector2(0, 0)
        for word in self.display_words:
            surf.blit(word, word.get_rect(topleft=prev))
            prev.y += word.get_height()


game = Words()

is_running = True
while is_running:

    status = game.update(delta)
    if status == COMMAND_EXIT:
        is_running = False

    game.draw(screen)

    pygame.display.flip()
    delta = clock.tick()

pygame.quit()
