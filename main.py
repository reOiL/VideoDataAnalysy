import event_handler
import threading
import graphics

event_handler.load_handle_event_scripts()
graphics_tread = threading.Thread(target=graphics.draw_loop)
graphics_tread.start()
# graphics_tread.join()
# slow mode because thread make like shit

graphics.g_kevent_stack_worker.push(event_handler.handle_event(3))
while event_handler.processing:
    graphics.g_kevent_stack_worker.push(event_handler.handle_event(0))
