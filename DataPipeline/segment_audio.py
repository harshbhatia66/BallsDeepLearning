from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import multiprocessing

def split_audio(filename, audio_folder='audio_folder', output_folder='segments'):
    # Check if output folder exists and if not, create it
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    filepath = os.path.join(audio_folder, filename)
    audio_file = AudioSegment.from_mp3(filepath)

    # Split track where the silence is 300 milliseconds or more and get chunks
    chunks = split_on_silence(
        audio_file,
        # Must be silent for at least 300 milliseconds
        min_silence_len=300,
        # Consider it silent if quieter than -36 dBFS
        silence_thresh=-36
    )

    # If chunks shorter than 2 seconds, append to the previous chunk
    min_len = 2 * 1000  # 2 seconds in ms
    chunks_corrected = []
    for chunk in chunks:
        if len(chunk) < min_len and chunks_corrected:
            chunks_corrected[-1] += chunk
        else:
            chunks_corrected.append(chunk)

    # Export all of the individual chunks as .mp3 files
    for i, chunk in enumerate(chunks_corrected):
        # Remove the last 4 characters of filename (.mp3)
        out_file = os.path.join(output_folder, f"{filename[:-4]}_segment{i}.mp3")
        chunk.export(out_file, format="mp3")
    print(f"Finished splitting{out_file}")

def main(audio_folder):
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.mp3')]
    pool.starmap(split_audio, [(f, audio_folder) for f in audio_files])

if __name__ == "__main__":
    main(r"C:\Users\Harsh\Documents\gap\gapvoice\audio_preprocessing\mp3")
