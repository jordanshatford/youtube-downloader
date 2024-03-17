import type { Channel } from './Channel';

export type Video = {
	id: string;
	url: string;
	title: string;
	duration: string;
	thumbnail: string;
	channel: Channel;
};
