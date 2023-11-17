/**
 * Save a file to the users computer by downloading programatically.
 * @param blob - the file as a blob.
 * @param name - the name to save the file as.
 */
export async function saveAs(blob: Blob, name: string): Promise<number> {
	const base64 = await blobToBase64(blob);
	return await browser.downloads.download({
		// Blob type and base64 data for download.
		url: `data:${blob.type};base64,${base64}`,
		filename: cleanFilename(name),
		saveAs: false,
		conflictAction: 'uniquify'
	});
}

/**
 * Covert a blob to a base64 string.
 * @param blob - the blob.
 * @returns string - the blob as a base64 string.
 */
async function blobToBase64(blob: Blob): Promise<string> {
	return new Promise((resolve, reject) => {
		const reader = new FileReader();
		// On error reject with error from FileReader.
		reader.onerror = () => reject(reader.error);
		reader.onloadend = () => {
			const dataUrl = reader.result as string;
			// Remove "data:mime/type;base64," prefix from data url.
			const base64 = dataUrl.substring(dataUrl.indexOf(',') + 1);
			resolve(base64);
		};
		reader.readAsDataURL(blob);
	});
}

/**
 * Clean a string to prevent browser download throwing invalid naming.
 * @param name - name to clean
 * @returns string - cleaned filename
 */
function cleanFilename(name: string): string {
	return name.replace(/[^a-z0-9]/gi, '_');
}
