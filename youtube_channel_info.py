# encoding: utf-8

import sys
import os
from workflow import Workflow, ICON_WEB, web
from youtube import working_api

channelId = sys.argv[1]

def channel_info(channelId):
	r = web.get('https://www.googleapis.com/youtube/v3/channels', dict(key=working_api(),
																	part='snippet',
																	id=channelId))
	r.raise_for_status()
	return r.json()


def main(wf):

	channel_data = channel_info(channelId)

	#basic channel info / open channel page in browser
	wf.add_item(title='Go to '+channel_data['items'][0]['snippet']['title']+'\'s page', 
				subtitle=channel_data['items'][0]['snippet']['description'],
				arg='https://youtube.com/channel/'+channelId,
				valid=True,
				icon=os.path.join(os.path.dirname(__file__), 'user.png')
				)

	#vew recent videos
	wf.add_item(title='Latest videos',
				subtitle='',
				arg='recent_videos/'+channelId,
				valid=True,
				icon=os.path.join(os.path.dirname(__file__), 'gift.png')
				)


	#vew most popular videos
	wf.add_item(title='Most popular videos',
				subtitle='',
				arg='popular_videos/'+channelId,
				valid=True,
				icon=os.path.join(os.path.dirname(__file__), 'star.png')
				)


	wf.send_feedback()



if __name__ == u'__main__':
	wf = Workflow()
	sys.exit(wf.run(main))