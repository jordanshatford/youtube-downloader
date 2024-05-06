/**
 * Save a file to the users computer by downloading programatically.
 * @param blob - the file as a blob.
 * @param name - the name to save the file as.
 */
export function saveAs(blob: Blob, name: string) {
	// Create anchor tag referencing the blob
	const url = window.URL.createObjectURL(blob);
	const a = document.createElement('a');
	a.href = url;
	a.download = name;
	// Append anchor and click to download
	document.body.appendChild(a);
	a.click();
	// Cleanup
	a.remove();
	window.URL.revokeObjectURL(url);
}
