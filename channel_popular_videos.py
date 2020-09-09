import sys
import os
from workflow import Workflow, ICON_WEB, web
from youtube import working_api

channelId = sys.argv[1]

def popular_video_search(channelId):
	r = web.get('https://www.googleapis.com/youtube/v3/search', dict(key=working_api(),
																	part='snippet',
																	channelId=channelId,
																	maxResults=50,
																	order='viewCount',
																	safeSearch='None',
																	type='video',
																	vidoeType='any'
																	))

	r.raise_for_status()
	return r.json()

def main(wf):
	for post in popular_video_search(channelId)['items']:
		wf.add_item(title=post['snippet']['title'],
					subtitle = post['snippet']['channelTitle']+' | '+post['snippet']['publishedAt'],
					arg='https://i.ytimg.com/vi/'+post['id']['videoId']+'/mqdefault.jpg',
					valid=True,
					icon='')

	# Send the results to Alfred as XML
	wf.send_feedback()



if __name__ == u"__main__":
	wf = Workflow()
	sys.exit(wf.run(main))