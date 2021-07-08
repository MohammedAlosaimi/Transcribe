# chat-bot

<!-- PROJECT IMAGE -->
<p align="center">
<img src="images/image.png" alt="image" width="500">
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Abstract](#abstract)
* [Installation](#installation)
* [Quick Start](#design)
* [Implementation](#implementation)

<!-- ABSTRACT -->
## Abstract

The idea behind this repository is to convert the speech-to-text by [Watson Text to Speech](https://www.ibm.com/cloud/watson-text-to-speech) and then save it in [`output.txt`](https://github.com/MohammedAlosaimi/watson-streaming-stt/blob/master/watson-streaming-stt/output.txt). Moreover, it converts the file [`output.txt`](https://github.com/MohammedAlosaimi/watson-streaming-stt/blob/master/watson-streaming-stt/output.txt) from text to speech by [Watson Speech to Text](https://www.ibm.com/cloud/watson-speech-to-text) and then saves it in [`output.mp3`](https://github.com/MohammedAlosaimi/watson-streaming-stt/blob/master/watson-streaming-stt/output.mp3).

<!-- INSTALLATION -->
## Installation

To install, use `pip`: 

```bash
pip install -r requirements.txt
```
if errors on windows installing `pyaudio`
Install `pipwin`: 

```bash
pip install pipwin
```

Then go install `pyaudio`: 

```bash
pipwin install pyaudio
```

<!-- QUICK START -->
## Quick Start

All you need to run this program is to Install the requirements and then you can run the program from [`transcribe`](https://github.com/MohammedAlosaimi/watson-streaming-stt/blob/master/watson-streaming-stt/transcribe.py). Note: You may need to change the "b" and "c" if you want to run it from your own server. Text-to-Speech from [`textospeech.py`](https://github.com/MohammedAlosaimi/watson-streaming-stt/blob/master/watson-streaming-stt/textospeech.py) and Speech-to-Text from [`speech.cfg`](https://github.com/MohammedAlosaimi/watson-streaming-stt/blob/master/watson-streaming-stt/speech.cfg).

<!-- IMPLEMENTATION -->
## Implementation

