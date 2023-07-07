import os
import collections

def parse_files(ver_metadata_file, trans_metadata_file):
    # Load verification metadata into a dictionary
    ver_dict = {}
    with open(ver_metadata_file, 'r', encoding='utf-8') as f:
        for line in f:
            filename, speaker = line.strip().split('|')
            ver_dict[filename] = int(speaker)

    # Load transcription metadata and output new transcriptions
    transcriptions = []
    current_video = None

    with open(trans_metadata_file, 'r', encoding='utf-8') as f:
        for line in f:
            path, trans = line.strip().split('|', 1)
            filename = path
            video_name = "_".join(filename.split('_')[:-1])  # Get the video name, excluding the chunk number

            # If the video has changed, append three new lines to transcriptions
            if video_name != current_video:
                current_video = video_name
                transcriptions.append('\n'*2)

            speaker = ver_dict[filename]  # Get the speaker label
            speaker_label = "[Charlie]" if speaker == 1 else "[Content]"
            transcriptions.append(f"{speaker_label} {trans}")

    # Write out the new transcriptions in a new file
    with open("transcriptions.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(transcriptions))

# Update these file paths as necessary
ver_metadata_file = r"C:\Users\Harsh\Documents\gap\gapvoice\audio_preprocessing\src\verification_metadata.txt"
trans_metadata_file = r"C:\Users\Harsh\Documents\gap\gapvoice\audio_preprocessing\src\metadata.txt"

parse_files(ver_metadata_file, trans_metadata_file)
