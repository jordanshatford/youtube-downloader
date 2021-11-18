import type { SvelteComponent } from 'svelte'

// The status of a video being converted to MP3
export enum Status {
	WAITING = 'WAITING',
	DOWNLOADING = 'DOWNLOADING',
	PROCESSING = 'PROCESSING',
	DONE = 'DONE',
	ERROR = 'ERROR',
	UNDEFINED = 'UNDEFINED'
}

export enum Variant {
	DANGER = 'danger',
	SUCCESS = 'success',
	WARNING = 'warning',
	INFO = 'info'
}

export enum Theme {
	LIGHT = 'light',
	DARK = 'dark'
}

export type ChannelInfo = {
	name: string
	url?: string
	thumbnail?: string
}

export type VideoInfo = {
	id: string
	url: string
	title: string
	thumbnail: string
	duration?: string
	channel?: ChannelInfo
	status?: Status
}

export type Notification = {
	id: string
	time: Date
	title: string
	message: string
	type: Variant
	icon?: typeof SvelteComponent
}
