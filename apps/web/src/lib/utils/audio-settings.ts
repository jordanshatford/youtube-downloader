import { AudioFormat } from '@yad/client';

export const audioFormatOptions = [
	{ value: AudioFormat.MP3, text: 'MP3' },
	{ value: AudioFormat.AAC, text: 'AAC' },
	{ value: AudioFormat.FLAC, text: 'FLAC' },
	{ value: AudioFormat.M4A, text: 'M4A' },
	{ value: AudioFormat.OPUS, text: 'OPUS' },
	{ value: AudioFormat.WAV, text: 'WAV' }
];

export const audioFormatDescriptions = {
	[AudioFormat.MP3]:
		'An MP3 file is an audio file saved in a compressed audio format developed by the ' +
		'Moving Picture Experts Group (MPEG) that uses "Layer 3" audio compression ' +
		'(MP3). MP3 files are commonly used to store audio tracks, podcasts, lectures, ' +
		'sermons, and audiobooks. While the format compressed audio to much smaller file sizes ' +
		'than competing formats, it still provided near-CD quality sound (stereo, 16-bit). The ' +
		'quality of an MP3 file depended (and still does) largely on the bit rate used for ' +
		'compression. The bit rate used is 192kbps.',
	[AudioFormat.AAC]:
		'An AAC file is an audio file similar to an .MP3 file but compressed with Advanced ' +
		'Audio Coding (AAC), a lossy digital audio compression standard. The lossy ' +
		'compression maintains quality nearly indistinguishable from the original audio ' +
		'source, making it optimal for compressing music data. AAC offers several performance ' +
		'improvements over MP3. Some features include a higher coding efficiency for stationary ' +
		'and transient signals, a simpler filterbank, and better handling of frequencies above 16 kHz.',
	[AudioFormat.FLAC]:
		'A FLAC file is an audio file compressed in the Free Lossless Audio Codec (FLAC) ' +
		'format, which is an open-source lossless audio compression format. It is similar to ' +
		'an .MP3 file, but is compressed without any loss in quality or loss of any original ' +
		'audio data. FLAC reduces the size of digital audio by approximately 60 percent and is ' +
		'a widely supported format across the most popular platforms.',
	[AudioFormat.M4A]:
		'An M4A file is an audio file that may store various types of audio content, such as ' +
		'songs, podcasts, and audiobooks. It is saved in the MPEG-4 format and encoded ' +
		'with either the Advanced Audio Coding (AAC) codec or the Apple Lossless Audio Codec (ALAC).',
	[AudioFormat.OPUS]:
		'An OPUS file is an audio file created in the Opus format, a lossy audio format developed ' +
		'for Internet streaming. It uses both SILK (used by Skype) and CELT (from Xiph.Org) codecs ' +
		'and supports variable bit rates from 6 kb/s to 510 kb/s. OPUS files are most commonly ' +
		'contained using the Ogg audio container format. Thus, the files are sometimes referred to as ' +
		'Ogg Opus files. The Opus codec is used for Voice over IP (VoIP), video conferencing, in-game ' +
		'chat. Since the Opus codec is primarily used for streaming, files with the .opus extension that ' +
		'are encoded with the Opus codec are not common.',
	[AudioFormat.WAV]:
		'A WAV file is an audio file saved in the WAVE format, a standard digital audio file format ' +
		'utilized for storing waveform data. WAV files may contain audio recordings with different sampling ' +
		'rates and bitrates but are often saved in a 44.1 kHz, 16-bit, stereo format, which is the standard ' +
		'format used for CD audio. The WAVE format is based on the Resource Interchange File Format (RIFF), ' +
		'a file container format primarily used to save video and sound.'
};
