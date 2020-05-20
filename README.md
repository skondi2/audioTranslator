# Audio Translator

This is a Python program that can transcribe and translate audio files. The transcription part is done with the AssemblyAI API and the translation part is done with the Yandex Translating API.

## Transcription:

Based off what the user specifies, this program can take in audio files that are stored locally or audio files that are directly accessible via URL. If the file is stored locally, then the file is first uploaded to the AssemblyAI API in order to transcribe it. As stated in AssemblyAI documentation, this audio file shall be deleted immediately after transcription. 

Note: this API implementation is done with my free account key and thus restrictions such as 5 hours of transcription maximum and 1 transcription at one time are in place.

Further information is given here: https://docs.assemblyai.com/overview/getting-started

## Translation:

The transcribed text that is outputted from the AssemblyAI API is then translated into the desired language specified by the user. This is done as a GET request with the Yandex API and the output is in XML format and then parsed.

Note: this API implementation is done with my account key.

Further information is given here: https://tech.yandex.com/translate/doc/dg/concepts/about-docpage/

## Usage:
Here is an example usage:
```
Audio URL or Local file path? Enter 1 or 2. 2
Enter audio URL: https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3
Enter desired language code. Enter 'options' for possible langauge codes: options
Options: 
Basque: 'eu' 
Welsh: 'cy' 
Dutch: 'nl' 
Italian: 'it'
Spanish: 'es'
German: 'de'
French: 'fr'
Danish: 'da'

Enter desired language code: es
Original Text: 
You know Demons on TV like that and and for people to expose themselves to being rejected on TV or humiliated by fear factor or.

Translated Text: 
Usted conoce a los demonios en la televisión como esa y para que las personas se expongan a ser rechazadas en la televisión o humilladas por el factor de miedo o.
Powered by Yandex.Translate.
```
