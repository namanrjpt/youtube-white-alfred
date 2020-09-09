# encoding: utf-8

import sys
import os
from workflow import Workflow, ICON_WEB, web
from youtube import working_api

videoId = sys.argv[1]

def video_info(videoId):
	r = web.get('https://www.googleapis.com/youtube/v3/videos', dict(key=working_api(),
																	part='snippet,contentDetails,statistics',
																	id=videoId))
	r.raise_for_status()
	return r.json()

#sample search of channel #not used anywhere i think
def channel_videos(channelId, order, maxResults=5):
	#order{'date', 'relevance', 'rating', 'title', 'videoCount', 'viewcount'}
	r = web.get('https://www.googleapis.com/youtube/v3/search', dict(key=working_api(),
																	part='snippet',
																	type='video',
																	safeSearch='none',
																	maxResults=maxResults,
																	q='shwetabh+gangwar',
																	channelId=channelId,
																	order=order))

	

def main(wf):

	video_data = video_info(videoId)
	wf.add_item(title=video_data['items'][0]['snippet']['title'],
				subtitle=video_data['items'][0]['contentDetails']['duration']+' | '+video_data['items'][0]['snippet']['channelTitle'],
				arg='https://youtu.be/'+video_data['items'][0]['id'],
				valid=True,
				icon=os.path.join(os.path.dirname(__file__), 'youtubeRed.png'))
	#go to channel
	wf.add_item(title='View '+video_data['items'][0]['snippet']['channelTitle']+'\'s'+' channel',
				subtitle='View recent and popular uploads',
				arg=video_data['items'][0]['snippet']['channelId'],
				valid=True,
				icon=os.path.join(os.path.dirname(__file__), 'user.png'))
	#mpv controls
	wf.add_item(title='Play in mpv',
				subtitle='mpv player will play the highest quality',
				arg='command/mpv '+'https://youtu.be/'+videoId,
				valid=True,
				icon=os.path.join(os.path.dirname(__file__), 'mpvLogo.png'))
	wf.add_item(title='Play in 1080p : HD',
				subtitle='mpv player will play 1080p as the highest quality',
				arg='command/yth '+'https://youtu.be/'+videoId,
				valid=True,
				icon=os.path.join(os.path.dirname(__file__), 'mpvLogo.png'))
	wf.add_item(title='Play in 720p',
				subtitle='mpv player will play 1080p as the highest quality',
				arg='command/yts '+'https://youtu.be/'+videoId,
				valid=True,
				icon=os.path.join(os.path.dirname(__file__), 'mpvLogo.png'))
	wf.add_item(title='Play audio track',
				subtitle='mpv player will play the audio track in the background',
				arg='command/mpv --no-video '+'https://youtu.be/'+videoId,
				valid=True,
				icon=os.path.join(os.path.dirname(__file__), 'musicNote.png'))
	
	wf.send_feedback()


#channel_videos('UC2gQaoCItAC-IbT8RNwWqLQ', 'viewCount' )
# video_info(videoId)

if __name__ == u'__main__':
	wf = Workflow()
	sys.exit(wf.run(main))