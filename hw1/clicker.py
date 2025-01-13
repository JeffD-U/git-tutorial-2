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
        self.color = (255, 0, 0)

        # Initialize all imported Pygame modules
        # We must include this in any PyGame application
        pygame.init()

        # Set the title of the display window
        pygame.display.set_caption("Clicker")

        # Create a window of size 600x600. This is referred to as the "surface"
        # of our application (sometimes also known as our "canvas"). We will be
        # able to refer to specific coordinates of this surface using (x,y)
        # coordinates, where the top-left corner of the window is coordinate
        # (0, 0). Note that the y coordinates grow *down* not up. For example,
        # the bottom-left corner of the window would be (0, 599)
        self.surface = pygame.display.set_mode((600, 600))

        # Create a clock object. This will later allow us to control how
        # often our window is redrawn.
        self.clock = pygame.time.Clock()
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
        image = pygame.image.load('help.png')
        while True:
            # Retrieve the latest events. More specifically, any time
            # events happen, PyGame places them on a queue (to await
            # processing). The pygame.event.get() method retrieves any
            # events that have been placed on that queue.
            #
            # Individual events are represented as Event objects. You
            # can read more about this here:
            # https://www.pygame.org/docs/ref/event.html
            events = pygame.event.get()

            # Process each event
            for event in events:
                # In this application, we only process two events: the QUIT
                # event (which happens when the user closes the window) and the
                # MOUSEBUTTONUP (which happens when a mouse button is released,
                # i.e., when "the pressed mouse button goes back up")

                if event.type == pygame.QUIT:
                    # When the close button of the window is clicked, we...

                    # Uninitialize all Pygame modules
                    pygame.quit()

                    # And terminate the program
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:

                    # When the mouse button is released, add a new circle
                    # In the MOUSEBUTTONUP event, the Event object will include
                    # a "pos" attribute telling us the position of the surface
                    # that was clicked.
                    #
                    # Notice how all we do is add a circle to the list of
                    # circles. We don't actually draw anything on the surface
                    # at this point.
                    self._circles.append(event.pos)

                    # Uncomment the following line to see the exact positions
                    # that are being clicked on the window.

                    # print(f"Mouse clicked at position {event.pos}")
                
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
                        # Reset to initial state
                        self.rad = 3
                        self.color = (255, 0, 0)
                        self._circles.clear()  # Clear all circles
                        self.draw_window()
                    elif event.key == pygame.K_h:
                        # Toggle help message visibility
                        pygame.surface.blit(image,(0,0))
                        self.draw_window()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit(0)

            # Once we're done processing events, we redraw the window:
            self.draw_window()

            # The following ensures the surface is refreshed at 24 frames per
            # second. If we omit this, the surface will be refreshed constantly
            # (which will typically result in the application running slowly,
            # because it's spending all its time constantly redrawing the
            # window)
            self.clock.tick(24)

    def draw_window(self) -> None:
        """
        Clears the window and redraws all circles. This method separates the
        rendering (drawing) from the application logic and event processing.

        Remember that we have a 600x600 surface to draw on. While we can
        manipulate individual pixels, PyGame provides many convenience
        functions to draw lines, circles, etc. You can find many of them here:
        https://www.pygame.org/docs/ref/draw.html
        """

        # Fill the surface with a grey color
        # (128, 128, 128) is an RGB (Red Green Blue) color code,
        # specifying the amount of each color on a scale from 0 to 255.
        self.surface.fill((128, 128, 128))

        # For each circle in our list of circles, draw the circle.
        for i, circle in enumerate(self._circles):
            # Alternate circle colors between red, green, and blue
            color = self.color

            # Use pygame.draw.circle to draw a circle
            pygame.draw.circle(self.surface, color=color,
                               center=circle, radius=self.rad)

        # Instruct PyGame to actually refresh the window with
        # the elements we have just drawn
        pygame.display.update()


# If you're unsure about what the following lines mean, make sure to review
# this: https://book.cs-apps.org/getting_started/organization/index.html
if __name__ == "__main__":
    Clicker()