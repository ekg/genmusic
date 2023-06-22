import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

model = MusicGen.get_pretrained('large')
model.set_generation_params(duration=8)  # generate 8 seconds.

# read descriptions file name as the first argument
descriptions_file = sys.argv[1]

# take descriptions as input
# descriptions are separated by a blank line in the text file
descriptions = []
with open(descriptions_file, 'r') as f:
    descriptions = f.read().split('\n\n')

#descriptions = ['happy rock', 'energetic EDM', 'sad jazz']
print(descriptions)

# generate audio
wav = model.generate(descriptions)  # generates N samples

for idx, one_wav in enumerate(wav):
    # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
    audio_write(f'{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness")
