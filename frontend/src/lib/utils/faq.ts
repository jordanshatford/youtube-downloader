import { RoutePathConstants } from '$lib/utils/route'
import type { ListItem } from '$lib/utils/types'

export const websiteName = RoutePathConstants.PUBLIC_HOST_NAME

export const faqs: ListItem[] = [
	{
		title: `Is ${websiteName} free to use?`,
		description: `Yes, ${websiteName} is completely free to use as long as you permissions to do so with any copyright material.`
	},
	{
		title: 'Is there a limit to the number of videos I can convert?',
		description: 'No, there is no limit so you can convert as many videos as you want.'
	},
	{
		title: 'How do I convert a video to MP3?',
		description:
			'To convert a video to MP3, you can search for a video or paste a link into the search bar on the home page. Then click ' +
			'the plus icon to start the download process. To see information on the status of the download, navigate to the ' +
			'downloads page. Once it has completely the download icon located to the right of the respective video on the downloads ' +
			'page can be clicked to download the audio file.'
	},
	{
		title: 'How long does it take to convert a video?',
		description:
			'The time to convert a video may vary drastically based on the length of the video. On average it should take a minute ' +
			'or so to convert a video 5 minutes in length.'
	},
	{
		title: 'Is it possible to change the audio quality or format?',
		description:
			'It is currently not possible to change the audio quality or format. Each video will be converted to a MP3 file at 192kbps.'
	},
	{
		title: 'Can I convert videos on my mobile device?',
		description: `Yes, ${websiteName} supports converting and downloading files on mobile devices.`
	},
	{
		title: 'My download is stuck on (waiting, downloading, processing), what should I do?',
		description:
			'If your download has been stuck for awhile, you may need to refresh the page and try to download again. If the video is ' +
			'long then then the downloading portion of the process may take awhile so please be patient.'
	},
	{
		title: 'There was an error while trying to download, what should I do?',
		description:
			'If an error has occured it is likely that you will not be able to download that video for one of many reasons. You can ' +
			'attempt the download process again, but if an error occurs multiple times, the video may not be available to download.'
	}
]
