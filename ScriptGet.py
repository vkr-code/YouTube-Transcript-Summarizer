import tsum
import eel

eel.init('web')

from youtube_transcript_api import YouTubeTranscriptApi

@eel.expose
def getCaption():
    outls =[]
    tx = YouTubeTranscriptApi.get_transcript('aZkG0b6oi4s')
    for i in tx:
        outxt= (i['text'])
        outls.append(outxt)
    
    with open("op2.txt","a") as opf:
        opf.write(outxt+ " ")
        tsum.generate_summary("op2.txt", 2)




#eel.start('front.html', size = (300,200))
