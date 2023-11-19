"""
dependencies
pip install gTTS
python3 -m pip install PyPDF2
"""

from gtts import gTTS
import PyPDF2

# Insert the name of your PDF
pdf_path = 'myenv/The Road Not Taken.pdf'
pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))

# Initialize an empty string to store the entire text
full_text = ''

# Extract text from each page and concatenate
for page in pdf_reader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace('\n', ' ')
    full_text += clean_text + ' '

# Print the extracted text for debugging
print("Extracted Text:")
print(full_text)

# Create gTTS object
tts = gTTS(full_text, lang='en')

# Save the speech to an MP3 file
tts.save('story.mp3')

# You can play the MP3 file using a player of your choice, for example:
import os
os.system("open story.mp3")

"""
Thoughts on improvements. 
It would be cool to dynamically take the base PDF title and use that to save my .mp3 file so that way you could easily pass that without having to manually replace.
I wanted to try and use pyttsx3 and get maybe a more human like text to speech narrator, but I was running into weird compatibility issues that I wasn't able 
to resolve at this time. 
"""