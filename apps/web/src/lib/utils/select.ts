/**
 * Helper type representing the values of an objects key.
 */
type ValueOf<T> = T[keyof T];

/**
 * Convert an object into an array of select options based on its entries.
 * @param obj - the object to convert to select options.
 * @returns array of objects containing value and label entries.
 */
export function toSelectOptions<T extends Record<string, ValueOf<T>>>(
	obj: T
): { value: ValueOf<T>; label: string }[] {
	return Object.entries(obj).map(([key, value]) => ({ value, label: key }));
}
