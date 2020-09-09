# encoding: utf-8

import sys
from workflow import Workflow, ICON_WEB, web

#API_KEY = 'AIzaSyAWrIPT4uIsUkymkPdvK3RJ-S6PNr-LMI0'



list_of_apis = [
	#this is to avoid quota
	#make sure the api keys are from different projects. So i had to make 8 projects. each project's api key goes here.
	'<your youtube api keys go here... for regular uses 5-6 keys are enough...>',
	'<your youtube api keys go here... for regular uses 5-6 keys are enough...>',
	'<your youtube api keys go here... for regular uses 5-6 keys are enough...>',
	'<your youtube api keys go here... for regular uses 5-6 keys are enough...>',
	'<your youtube api keys go here... for regular uses 5-6 keys are enough...>',
	'<your youtube api keys go here... for regular uses 5-6 keys are enough...>',
	'<your youtube api keys go here... for regular uses 5-6 keys are enough...>',
	'<your youtube api keys go here... for regular uses 5-6 keys are enough...>'
]

#this return a working api key. checks if they key is working with loading data of a sample video
def working_api():
	for api in list_of_apis:
		try:
			r = web.get('https://www.googleapis.com/youtube/v3/videos', dict(key=api, part='snippet', id='2lAe1cqCOXo'))
			if r.json()['kind'] == 'youtube#videoListResponse':
				return(api)
		except Exception:
			pass


def main(wf):


	url='https://www.googleapis.com/youtube/v3/search'
	params= dict(key=working_api(), part='snippet', type='video', safeSearch='none' , maxResults=50, q=wf.args[0])
	r = web.get(url, params)

	# throw an error if request failed
	# Workflow will catch this and show it to the user
	r.raise_for_status()

	# Parse the JSON returned by pinboard and extract the posts
	result = r.json()
	posts = result['items']

	#print(type(posts[0]['snippet']['description']))
	#print(posts[0]['snippet']['description'])

	# Loop through the returned posts and add an item for each to
	# the list of results for Alfred
	for post in posts:
		wf.add_item(title=post['snippet']['title'],
					#subtitle = get_video_duration(post['id']['videoId'])+' | '+post['snippet']['channelTitle'],
					subtitle = post['snippet']['channelTitle']+' | '+post['snippet']['publishedAt'],
					arg='https://i.ytimg.com/vi/'+post['id']['videoId']+'/mqdefault.jpg',
					valid=True,
					icon='')

	# Send the results to Alfred as XML
	wf.send_feedback()



if __name__ == u"__main__":
	wf = Workflow()
	sys.exit(wf.run(main))