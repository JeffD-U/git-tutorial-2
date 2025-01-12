"""
This is a simple example of a graphical application implemented
with PyGame. It opens a blank window and, every time you click on
the window, it will add a circle in that position of the window.

You can run this example by running the following from the
Linux terminal:

    python3 clicker.py

This example highlights two important aspects of PyGame (and,
more generally, of graphical applications):

1. The event loop: A graphical application will typically perform
   some setup operations (e.g., opening a window of a specific size)
   and will then enter an "event loop". This is an effectively infinite
   loop where the program just waits for "events" to happen, so we can
   react to them. Events can include mouse clicks, key presses, etc.

   For example, if the user clicks on a position of the window, we need
   to add a circle in that position. Similarly, if the user closes the
   window, we will want to break out of the infinite loop, and end the
   program.

2. Separating "drawing" from other program logic: Graphical applications
   render (or "draw") the internal state of a program graphically. For
   example, if we were implementing a game of chess, our internal state
   could be an 8x8 list of lists, where each position contains a Piece
   object, or the value None. We will perform many operations on that
   state, such as checking for valid moves, moving pieces, etc.

   In a graphical application, we want to keep the drawing of that internal
   state completely separate from the actual logic of the application. There
   will typically be a separate function whose purpose is to take the current
   internal state of the application, and to produce a graphical representation
   of it (along with any interface elements like buttons, menus, etc.)

   In the example code below, our application keeps track of a list of circles
   or, more specifically, the (x,y) coordinates of the center of each circle
   (in our example, all circles will have a radius of 20 pixels). We said
   earlier that clicking on the window will add a circle on that location
   of the window. This just means that, when a mouse click happens, we will
   add a new circle to our list of circles, but we will *not* draw that
   circle when processing the mouse click. Instead, we have a "drawing
   function" that draws all the circles; after processing the event, we will
   call this function, and the new circle will be reflected in the graphical
   representation produced by that function.

Make sure to read the code below in the order in which it is presented.
You will find additional comments below that explain what the code does.


"""

import sys
import pygame

# In our example, we will be alternating between red, blue, and green
# circles. We explain the meaning of these 3-tuples further below.
CIRCLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]


class Clicker:
    """
    This class demonstrates how to handle mouse clicks in Pygame.
    It maintains a list of circle positions that are updated in response to
    user clicks.
    """

    _circles: list[tuple[int, int]]

    def __init__(self) -> None:
        """
        The constructor initializes the Pygame modules, sets up the display
        window, and initiates the event loop.
        """

        # List to store the positions of circles
        self._circles = []
        self.rad = 3
        self.color = (255, 0, 0)  # Start with red color

        # Initialize all imported Pygame modules
        pygame.init()

        # Set the title of the display window
        pygame.display.set_caption("Clicker")

        # Create a window of size 600x600
        self.surface = pygame.display.set_mode((600, 600))

        # Create a clock object
        self.clock = pygame.time.Clock()

        # Flag to control visibility of the help message
        self.show_help = False  # **Added this line**

        # Begin the event loop
        self.run_event_loop()

    def run_event_loop(self) -> None:
        """
        The event loop for our application. Inside this loop, we will
        repeatedly perform the following operations:
            1. Check for new events
            2. If there are any new events, process the events.
            3. Re-draw the window
        """
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self._circles.append(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.rad += 1  # Increase radius
                        self.draw_window()
                    elif event.key == pygame.K_LEFT:
                        if self.rad > 1:
                            self.rad -= 1  # Decrease radius but not below 1
                        self.draw_window()
                    elif event.key == pygame.K_UP:
                        # Cycle through colors
                        self.color = CIRCLE_COLORS[(CIRCLE_COLORS.index(self.color) + 1) % len(CIRCLE_COLORS)]
                        self.draw_window()
                    elif event.key == pygame.K_ESCAPE:
                        self.rad = 3
                        self.color = (255, 0, 0)
                        self._circles.clear()  # Clear all circles
                        self.show_help = False  # **Reset help message visibility**
                        self.draw_window()
                    elif event.key == pygame.K_h:
                        self.show_help = not self.show_help
                        self.draw_window()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit(0)
            self.draw_window()
            self.clock.tick(24)

    def draw_window(self) -> None:
        """
        Clears the window and redraws all circles. This method separates the
        rendering (drawing) from the application logic and event processing.
        """
        self.surface.fill((128, 128, 128))
        for i, circle in enumerate(self._circles):
            color = CIRCLE_COLORS[i % 3]
            pygame.draw.circle(self.surface, color=color,
                               center=circle, radius=self.rad)
        if self.show_help:
            font = pygame.font.SysFont("Arial", 24)
            help_text = font.render("Use arrows to resize, ESC to reset, H for help, Q to quit", True, (255, 255, 255))
            self.surface.blit(help_text, (10, 10))
        pygame.display.update()
if __name__ == "__main__":
    Clicker()