import os
import sys
from pydub import AudioSegment

# Get the input and output directories from command line arguments
input_dir = sys.argv[1]
output_dir = sys.argv[2]

# Loop through all MP3 files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith(".mp3"):
        # Load the MP3 file using pydub
        file_path = os.path.join(input_dir, file_name)
        audio = AudioSegment.from_file(file_path, format="mp3")

        # Build the output file path and save the WAV file
        output_file_name = file_name.replace(".mp3", ".wav")
        output_file_path = os.path.join(output_dir, output_file_name)
        audio.export(output_file_path, format="wav")
