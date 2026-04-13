import type { Version } from '@yd/client';
import { getVersions } from '@yd/client';

const APP_VERSION = { component: 'Application', version: __APP_VERSION__ };

class VersionsStore {
	public state = $state<Version[]>([]);

	public async init() {
		try {
			const { data: state } = await getVersions();
			if (state) {
				this.state = state;
			}
		} catch (e) {
			console.error('Failed to get initial versions state ', e);
			return;
		}
	}

	public items: Version[] = $derived(
		[APP_VERSION, ...this.state].sort((a, b) => a.component.localeCompare(b.component))
	);

	public reset() {
		this.state = [];
	}
}

export const versions = new VersionsStore();
