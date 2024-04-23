import { DEFAULT_DOWNLOAD_OPTIONS } from '@yd/client';

import { writeableStorage } from '~/lib/stores/writeable-storage';

// Store used for managing preferred settings set by the user.
export const settings = writeableStorage('settings', DEFAULT_DOWNLOAD_OPTIONS);
