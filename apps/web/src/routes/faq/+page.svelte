<script lang="ts" module>
	import config from '$lib/config';

	import { Accordion } from '@yd/ui';

	type Question = {
		question: string;
		answer: string;
	};

	const faqs: Question[] = [
		{
			question: 'Is this website free to use?',
			answer:
				'Yes, it is completely free to use as long as you have permissions to download any copyright material.'
		},
		{
			question: 'Is there a limit to the number of videos I can download?',
			answer:
				'No, there is no strict limit. You may see that some video remain in a waiting state until others have completed.'
		},
		{
			question: 'How do I use this website?',
			answer:
				'First take a look through the various settings pages to ensure that you have configured our available options as you ' +
				'desire. Then you can search for a video using a search term, link, channel name, etc. Add the relevant video to the ' +
				'queue. Status information of the download can be found on the downloads page. Finally, once it has completely you can ' +
				'download the file directly to your device.'
		},
		{
			question: 'How long does it take to download a video?',
			answer:
				'The time it takes to download can vary drastically based on the length of the video and the settings you ' +
				'have configured. You will be provided with progress information for the download on the downloads page.'
		},
		{
			question: 'Can I use this website on a mobile device?',
			answer: 'Yes, this site is mobile device friendly.'
		},
		{
			question: 'My download appears to be stalled, what should I do?',
			answer:
				'If your download has been stalled for some time, you may need to reload and try again. If the video itself ' +
				'is long, then the download may take awhile, so please be patient.'
		},
		{
			question: 'There was an error trying to download, what should I do?',
			answer:
				'If an error has occured you can attempt to retry the download from the downloads page. If the error occurs ' +
				'multiple times, the video may be unavailable to download. This may be due to YouTube blocking the download.'
		},
		{
			question:
				'The subtitles embedded in the download are not in the subtitle language I configured, what should I do?',
			answer:
				'It may not be possible to download the subtitle language you have requested for a given video. This is a ' +
				'preferred value that we will attempt to use when possible. If you believe the correct subtitles do exist for the ' +
				'video you are requesting, please report an issue via GitHub.'
		},
		{
			question:
				'There was no subtitles embedded in the download even though I enabled it, what should I do?',
			answer:
				'It may not be possible to download any subtitles for a given video. This could mean that YouTube does not have ' +
				'any. If you believe subtitles do exist for the video you are requesting, please report an issue via GitHub.'
		},
		{
			question: 'What is batch downloading?',
			answer:
				'The batch downloading functionality allows you to input a list of YouTube video or playlist URLs and it will ' +
				'download all related videos using the settings you have configured. All of these files will be included in a ' +
				'single ZIP file available to the user on completion.'
		},
		{
			question: 'What is the maximum number of URLs I can input with batch downloading?',
			answer: 'With batch downloading you can input up to 25 URLs at a time.'
		},
		{
			question: 'Can my batch download mix and match video and playlist URLs?',
			answer:
				'Yes! You can mix and match any types of YouTube URLs. If one of the URLs provided is a playlist URL, then only ' +
				'the first 20 items from that playlist will be attempted to be downloaded. The other URL entries will download ' +
				'as normal.'
		},
		{
			question: 'Why is my batch download missing some files?',
			answer:
				'When batch downloading it may not be possible to download certain videos or playlists you have requested. ' +
				'Rather than failing the entire batch download, it will skip over those entries. You can see a list on the ' +
				'batch download page with the statuses of all current items in the batch.'
		}
	];
</script>

<svelte:head>
	<title>FAQ - {config.head.title}</title>
</svelte:head>

<Accordion.Root type="multiple" class="mx-auto max-w-4xl">
	{#each faqs as faq (faq.question)}
		<Accordion.Item value={faq.question}>
			<Accordion.Trigger>{faq.question}</Accordion.Trigger>
			<Accordion.Content>
				{faq.answer}
			</Accordion.Content>
		</Accordion.Item>
	{/each}
</Accordion.Root>
