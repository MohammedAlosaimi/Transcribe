from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/0de3ef1f-6128-4a66-a97c-f77b9ce2c5f6"
apikey = "KLKtkwGi_PUo19UQHsmYEyGxZ2Z23MvE0pclPiIjqKoz"
# Setup Service
authenticator = IAMAuthenticator(apikey)
# New TTS Service
tts = TextToSpeechV1(
    authenticator=authenticator
)
# Set Service URL
tts.set_service_url(url)


def storeMP3File():
    # open the txt file and take the results
    with open('output.txt', 'r') as out:
        text = out.readlines()

    # combine the multi lines in one line
    text = [line.replace('\n', '') for line in text]
    text = ''.join(str(line) for line in text)

    # convert the text to speech and then store it in mp3 file
    with open('output.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)

