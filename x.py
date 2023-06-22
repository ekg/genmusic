import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import sys

# read descriptions file name as the first argument
descriptions_file = sys.argv[1]
# and output as second argument, or cwd if not provided
output_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
# use length as the third argument, or 8 seconds if not provided
length = int(sys.argv[3]) if len(sys.argv) > 3 else 8
# batch the descriptions into groups of batch_size
# get this from the command line as argument 4, or 4 if not provided
batch_size = int(sys.argv[4]) if len(sys.argv) > 4 else 4

# load the model
model = MusicGen.get_pretrained('large')
model.set_generation_params(duration=length)

print("loaded the model")

# make sure the output directory exists
import os
os.makedirs(output_dir, exist_ok=True)

# take descriptions as input
# descriptions are separated by a blank line in the text file
descriptions = []
with open(descriptions_file, 'r') as f:
    descriptions = f.read().split('\n\n')

#descriptions = ['happy rock', 'energetic EDM', 'sad jazz']
print(descriptions)

# (the batch size of the model)
batches = [descriptions[i:i+batch_size] for i in range(0, len(descriptions), batch_size)]
for batch in batches:
    # generate audio
    print(batch)
    print("generating audio")
    wav = model.generate(batch)  # generates N samples

    for idx, one_wav in enumerate(wav):
        # save the generated audio to the current directory with a filename
        # replace spaces and invalid characters for filenames (slashes) with underscores.
        name = batch[idx].replace(' ', '_').replace('/', '_')
        # and remove any final periods or trailing newlines
        name = name.strip()
        name = name[:-1] if name[-1] == '.' else name
        # trim the name to 100 characters to avoid long filenames
        name = name[:100]
        # Will save with loudness normalization at -14 db LUFS.
        audio_write(f'{output_dir}/{name}', one_wav.cpu(), model.sample_rate, strategy="loudness")
        # recode to mp3
        # writing to output_dir
        torchaudio.save(f'{output_dir}/{name}.mp3', one_wav.cpu(), model.sample_rate)
