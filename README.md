to run, something like:

`i=vaporwaveyes; v=1; time python x.py $i.txt $i.$v 120 1 && sox $(ls -rt $i.$v/*.wav) $i.$v/output.wav && lame -V 2 $i.$v/output.wav $i.$v/output.mp3 && rsync -av $i.$v ....`

where 120 and 1 are the length in seconds and batch size