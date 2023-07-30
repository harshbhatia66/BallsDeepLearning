First we download the audio for the desired youtube channel - download_audio.py

Then we break down the audio into segments. This will allow for speaker verification and clean up messy audio - segment_audio.py

Clean the filenames so there are no errors - remove_special_char.ipynb

Then we transcribe the audio. This will create a metadata file for all the transcripts and their filenames - transcribe_audio.ipynb

Then we will perfrom speaker identification, this will create a verification metadata file - filter_audio.ipynb
It needs a reference folder of audio clips to use to identify our desired speaker.
Note: Currently this will identify only one person and, we need to add capability to recognise other speakers as well.

Compile the transcript dataset using this metadata - identify.py

Note: Create an env using the requirements.txt file. 