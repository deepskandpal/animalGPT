# animalGPT
LLM model which answers questions about Animal (2023)

## Steps
- [x] Common steps
   - [x] Extract audio file from video, convert to WAV format. Expected output: `audio.wav`
- [x] Speaker identification on complete file. Expected output
   ```py
   speaker_with_timestamps=[{"start": 0.0, "end":10.0, "speaker": "Speaker1"},...]
   ```
   - [x] Invoke LLM model to run on the audio file
   
- [x] Transcription of audio on complete file. Expected output: 
    ```py
    audio_with_timestamps=[{"start": 0.0, "end":10.0, "word": "lalala"},{"start": 10.0, "end":20.0, "word": "lalala"}...]
    ```
   - [x] Split audio file into 10 second chunks. Expected output: `audio001.wav,audio002.wav...`
   - [x] Call the Transcript API with each file.
      - [ ] Actual output:
         ```py
         audio_with_raw_timestamps=[{"start": 0.0, "end":10.0, "word": "lalala"},{"start": 0.0, "end":10.0, "word": "lalala"}...]
         ```
      - [ ] Expected output: `audio001.txt,audio002.txt...`
      - [ ] Offset each element of `file<n+1>.txt` with the timestamp of last element of `file<n>.txt`
   - [ ] Transform each element of previous output to have each item having offset timestamp
- [ ] Final expected output: 
   ```py
   combined_output=[{"start": 0.0, "end":10.0, "speaker": "Speaker1", "word": "lalala"},...]
   ```
