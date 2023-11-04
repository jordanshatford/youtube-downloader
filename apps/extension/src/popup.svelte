<script lang="ts">
	import './style.css';

	let prefferred = window?.matchMedia?.('(prefers-color-scheme: dark)')?.matches;

	let currentTab: chrome.tabs.Tab | null = null;
	chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
		currentTab = tabs[0];
	});
</script>

<div class="w-48">
	<h2 class="text-center text-red-800">YouTube Downloader</h2>
	<div>
		{#if currentTab}
			<p>Current Tab: {currentTab.title} dark: {prefferred}</p>
		{/if}
	</div>
	<a href="https://youtubedownloader.duckdns.org" target="_blank">Go to site</a>
</div>
