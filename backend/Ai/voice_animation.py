import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import pyaudio
import audioop
import threading

# Initialize Pygame and OpenGL
pygame.init()

# Screen Dimensions
screen_width, screen_height = 800, 600
pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
gluPerspective(45, (screen_width / screen_height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10)

# Audio Variables
chunk = 1024  # Number of audio frames per buffer
audio_intensity = 0  # Global variable to store audio intensity
is_running = True  # Flag to keep the program running

def listen_to_audio():
    """Capture audio input and calculate its intensity."""
    global audio_intensity
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=chunk)

    while is_running:
        data = stream.read(chunk, exception_on_overflow=False)
        audio_intensity = audioop.rms(data, 2)  # Get audio intensity

    stream.stop_stream()
    stream.close()
    p.terminate()

# Start Audio Listening in a Separate Thread
audio_thread = threading.Thread(target=listen_to_audio, daemon=True)
audio_thread.start()

def draw_cube(size, color):
    """Draw a cube with the given size and color."""
    glBegin(GL_QUADS)
    glColor3fv(color)
    for vertex in [
        [-size, -size, -size],
        [size, -size, -size],
        [size, size, -size],
        [-size, size, -size],
    ]:
        glVertex3fv(vertex)
    glEnd()

def render_visualizer():
    """Render the 3D audio visualizer."""
    global audio_intensity
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global is_running
                is_running = False

        # Clear Screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw 3D Cubes
        num_cubes = 10
        spacing = 2
        max_size = 1.5
        for i in range(num_cubes):
            glPushMatrix()
            x = (i - num_cubes // 2) * spacing
            size = max_size * (audio_intensity / 10000) * (i + 1) / num_cubes
            size = min(size, max_size)  # Cap the size
            glTranslatef(x, 0, 0)
            draw_cube(size, (0.1 * i, 1 - 0.1 * i, 0.5))
            glPopMatrix()

        # Rotate the scene
        glRotatef(1, 0, 1, 0)

        # Update Screen
        pygame.display.flip()
        pygame.time.wait(10)

# Run the visualizer
try:
    render_visualizer()
finally:
    pygame.quit()
    is_running = False
