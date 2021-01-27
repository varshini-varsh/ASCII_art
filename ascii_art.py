"
coded by varshini
just tried for fun
"

# import pywhatkit module
import pywhatkit as kt

print("Here's your image turns to ASCII art")

# your own sample image
source_path = "apple.jpg"

# displays the result (ASCII art)
target_path = "demo_ascii_art2.text"

# in built function turns image to ASCII art
kt.image_to_ascii_art(source_path, target_path)
