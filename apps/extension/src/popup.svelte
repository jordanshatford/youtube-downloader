<script lang="ts">
	import './style.css';
	import icon from 'data-base64:~assets/icon.png';

	const isDark = window?.matchMedia?.('(prefers-color-scheme: dark)')?.matches;
	if (isDark) {
		document.querySelector('html')?.classList.add('dark');
	} else {
		document.querySelector('html')?.classList.remove('dark');
	}
</script>

<div class="min-h-[325px] w-[325px] bg-white dark:bg-zinc-900">
	<div class="flex h-screen flex-col items-center justify-center space-y-4">
		<img src={icon} alt="Logo" class="h-20 w-20" />
		<a
			href="https://youtubedownloader.duckdns.org"
			target="_blank"
			class="text-zinc-800 underline dark:text-zinc-100"
		>
			Go to site
		</a>
	</div>
</div>
