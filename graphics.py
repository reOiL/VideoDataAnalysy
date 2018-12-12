import pygame
import event_handler


class event_stack_worker:
    def __init__(self):
        self.event_list = []

    def push(self, event_code):
        self.event_list.append(event_code)

    def pop(self):
        if len(self.event_list) == 0:
            return 0
        temp_ret = self.event_list[0]
        self.event_list.pop(0)
        return temp_ret


g_kevent_stack_worker = event_stack_worker()


class event_message:
    def __init__(self):
        self.img = 'NULL'

    def one_tick(self, screen):
        if self.img != 'NULL':
            screen.blit(self.img, (300 / 2, 300 / 2))
        self.show_msg(g_kevent_stack_worker.pop())

    def show_msg(self, msg_type):
        if event_handler.dange_level['WARNING'] == msg_type:
            self.img = pygame.image.load("Warn.png")
        elif event_handler.dange_level['CRITICAL'] == msg_type:
            self.img = pygame.image.load("Error.png")

    def hide_msg(self):
        self.img = 'NULL'


def draw_loop():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    k_event_message = event_message()
    while event_handler.processing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_handler.processing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                k_event_message.hide_msg()
        screen.fill((0, 0, 0))
        k_event_message.one_tick(screen)
        pygame.display.flip()
        pygame.time.wait(10)
