Prompts were generated in ChatGPT with GPT-4 using this structure:

```
I'm making an album of ai generated music, using prompts for each song. Here is the overall theme:

"$PROMPT"

Write 20 music generation prompts that explore this space in a unique and interesting way, mixing various pop music styles into the general theme.

Prompts should be descriptive, not imperative. Describe the music as it would be heard to a listener. Do not quote the prompts.
```

Save the output prompts in a file, say `music.txt`, and then generate tracks using something like:

`i=music.txt; v=1; time python x.py $i.txt $i.$v 120 1 && sox $(ls -rt $i.$v/*.wav) $i.$v/output.wav && lame -V 2 $i.$v/output.wav $i.$v/output.mp3`

where 120 and 1 are the length in seconds and batch size

