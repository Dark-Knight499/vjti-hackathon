import cv2
import speech_recognition as sr
import asyncio
from concurrent.futures import ThreadPoolExecutor
import threading
import queue

class CameraCapture:
    def __init__(self):
        self.frame_queue = queue.Queue(maxsize=1)
        self.stop_event = threading.Event()
        self.capture_event = threading.Event()

    def camera_thread(self):
        cap = cv2.VideoCapture(0)
        while not self.stop_event.is_set():
            ret, frame = cap.read()
            if ret:
                # Always keep only the latest frame
                if self.frame_queue.full():
                    self.frame_queue.get()
                self.frame_queue.put(frame)
                cv2.imshow('Camera', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.stop_event.set()
        cap.release()
        cv2.destroyAllWindows()

    async def listen_for_command(self, recognizer, source):
        try:
            print("Listening...")
            # Increase timeout and adjust recognition parameters
            recognizer.energy_threshold = 3000  # Lower threshold
            recognizer.dynamic_energy_threshold = True
            recognizer.pause_threshold = 0.8  # Shorter pause threshold
            
            # Increase timeout to 5 seconds
            audio = await asyncio.get_event_loop().run_in_executor(
                None, lambda: recognizer.listen(source, timeout=5, phrase_time_limit=5)
            )
            print("Processing speech...")
            text = await asyncio.get_event_loop().run_in_executor(
                None, recognizer.recognize_google, audio
            )
            print(f"Heard: {text.lower()}")
            return text.lower()
        except sr.WaitTimeoutError:
            print("No speech detected, listening again...")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio, please try again...")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    async def voice_recognition_thread(self):
        r = sr.Recognizer()
        while not self.stop_event.is_set():
            with sr.Microphone() as source:
                # Shorter ambient noise adjustment
                print("Adjusting for ambient noise...")
                r.adjust_for_ambient_noise(source, duration=0.2)
                
                text = await self.listen_for_command(r, source)
                await asyncio.sleep(0.1)  # Small delay between attempts
                if text:
                    trigger_words = ['click', 'take', 'capture', 'photo']
                    if any(word in text for word in trigger_words):
                        print("Command detected!")
                        self.capture_event.set()

    async def capture_image(self):
        print("Say 'click' to capture an image...")
        
        # Start camera thread
        camera_thread = threading.Thread(target=self.camera_thread)
        camera_thread.start()

        # Start voice recognition in the background
        voice_task = asyncio.create_task(self.voice_recognition_thread())

        try:
            while not self.stop_event.is_set():
                if self.capture_event.is_set():
                    if not self.frame_queue.empty():
                        frame = self.frame_queue.get()
                        try:
                            filename = 'captured_image.jpg'
                            success = cv2.imwrite(filename, frame)
                            if success:
                                print(f"Image successfully saved to {filename}")
                            else:
                                print("Failed to save image!")
                            break
                        except Exception as e:
                            print(f"Error saving image: {e}")
                await asyncio.sleep(0.1)
        finally:
            self.stop_event.set()
            camera_thread.join()
            await voice_task
            print(filename)
            return filename

if __name__ == "__main__":
    capture = CameraCapture()
    asyncio.run(capture.capture_image())