<script lang="ts">
	let currentTab: chrome.tabs.Tab | null = null;
	chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
		currentTab = tabs[0]
	});
</script>

<div>
  <h2 class="text-center">
    YouTube Downloader
  </h2>
  <div class="container">
		{#if currentTab}
			<p>Current Tab: { currentTab.title }</p>
		{/if}
  </div>
  <a href="https://youtubedownloader.duckdns.org" target="_blank">Go to site</a>
</div>

<style>
  .container {
    min-width: 470px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 47px;
  }
  .text-center {
    text-align: center;
  }
</style>
