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
				'The sutitles embedded in the download are not in the subtitle language I configured, what should I do?',
			answer:
				'It may not be possible to download the subtitle language you have requested for a given video. This is a ' +
				'preferred value that we will attempt to use when possible. If you believe the correct subtitles do exist for the ' +
				'video you are requesting, please report an issue via GitHub.'
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
