<script lang="ts" module>
	import config from '$lib/config';

	import { Accordion } from '@yd/ui';

	type Question = {
		question: string;
		answer: string;
	};

	const faqs: Question[] = [
		{
			question: 'Is this site free to use?',
			answer:
				'Yes, it is completely free to use as long as you have permissions for any copyright material.'
		},
		{
			question: 'Is there a limit to the number of videos I can download and convert?',
			answer: 'No, there is no limit, so you can convert as many videos as you want.'
		},
		{
			question: 'How do I download and convert videos?',
			answer:
				'To download and convert a video, you should first make sure that you have configured the settings to your preferred ' +
				'options. Then you can search for a video by term or with a link to get any relevant videos. Click the plus icon ' +
				'to queue the video to download. To see information on the status of the download, navigate to the downloads ' +
				'page. Once it has completely a clickable download button will appear in the table allowing you to download that video ' +
				'directly to your device.'
		},
		{
			question: 'How long does it take to download and convert a video?',
			answer:
				'The time to download and convert a video will vary drastically based on the length of the video, and the settings you ' +
				' have configured. You will be provided with progress information for progress of the download in the downloads page.'
		},
		{
			question: 'Can I convert videos on my mobile device?',
			answer: 'Yes, this site supports converting and downloading files on mobile devices.'
		},
		{
			question: 'My download appears to be stuck, what should I do?',
			answer:
				'If your download has been stuck for awhile, you may need to refresh the page and try to download again. If the video is ' +
				'long then then the download and processing portions of the process may take awhile so please be patient.'
		},
		{
			question: 'There was an error while trying to download, what should I do?',
			answer:
				'If an error has occured it is likely that you will not be able to download that video for one of many reasons. You can ' +
				'attempt the download process again, but if an error occurs multiple times, the video may be unavailable to download.'
		}
	];
</script>

<svelte:head>
	<title>FAQ - {config.head.title}</title>
</svelte:head>

<Accordion.Root type="multiple">
	{#each faqs as faq (faq.question)}
		<Accordion.Item value={faq.question}>
			<Accordion.Trigger>{faq.question}</Accordion.Trigger>
			<Accordion.Content class="flex flex-col gap-4 text-balance">
				{faq.answer}
			</Accordion.Content>
		</Accordion.Item>
	{/each}
</Accordion.Root>
