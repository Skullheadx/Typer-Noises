import pygame

pygame.init()

WIDTH, HEIGHT = 1080, 640

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

    font = pygame.font.Font("MonospaceTypewriter.ttf", 35)

    lines = script.split('\n')

    def __init__(self):
        self.left_bound, self.right_bound = WIDTH * 0.05, WIDTH * 0.8

        self.words = []
        for l in self.lines:
            line = ""
            l = l.split()
            for i, word in enumerate(l):
                line += word + ' '
                rendered = self.font.render(line, True, GRAY)
                if rendered.get_width() >= self.right_bound or i == len(l) - 1:
                    self.words.append(rendered)
                    line = ""
        for i in self.words:
            if i.get_width() > self.right_bound:
                self.right_bound = i.get_width()

        self.index = 0
        self.typed_words = [""]
        self.display_words = [self.font.render("", True, BLACK)]
        self.position = pygame.Vector2(self.left_bound, HEIGHT/2)

        self.draw_cursor = True
        self.time = 0

    def update(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_EXIT
            elif event.type == pygame.TEXTINPUT:
                char = event.text
                if self.display_words[-1].get_width() >= self.words[len(self.display_words) - 1].get_width():
                    self.add_new_line()

                self.typed_words[-1] += char
                self.display_words[-1] = self.font.render(self.typed_words[-1], True, BLACK, WHITE)
                if char == self.script[self.index]:
                    self.index += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.typed_words[-1] = self.typed_words[-1][:-1]
                    self.display_words[-1] = self.font.render(self.typed_words[-1], True, BLACK, WHITE)

                elif event.key == pygame.K_RETURN:
                    self.add_new_line()

        if self.time >= 500:
            self.draw_cursor = not self.draw_cursor
            self.time = 0
        self.time += delta
    def add_new_line(self):
        self.position.y -= self.display_words[-1].get_height()
        self.typed_words.append("")
        self.display_words.append(self.font.render("", True, BLACK))


    def draw(self, surf):
        surf.fill(WHITE)
        prev = self.position.copy()
        for word in self.words:
            surf.blit(word, word.get_rect(topleft=prev))
            prev.y += word.get_height()
        prev = self.position.copy()
        for word in self.display_words:
            surf.blit(word, word.get_rect(topleft=prev))
            prev.y += word.get_height()
        # pygame.draw.line(surf, BLACK, (self.left_bound, 0), (self.left_bound, HEIGHT))
        # pygame.draw.line(surf, BLACK, (self.right_bound, 0), (self.right_bound, HEIGHT))
        if self.draw_cursor:
            pygame.draw.line(surf, BLACK, (prev.x + self.display_words[-1].get_width(),prev.y - self.display_words[-1].get_height()),(prev.x + self.display_words[-1].get_width(),prev.y))


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
