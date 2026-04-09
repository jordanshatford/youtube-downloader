type ObjectLike = Record<string, string>;
type SelectOption = { value: string; label: string };
type SelectGroup = { options: SelectOption[]; label: string };

/**
 * Convert an object into an array of select options based on its entries.
 * @param obj - the object to convert to select options.
 * @returns array of objects containing value and label entries.
 */
export function toSelectOptions(obj: ObjectLike): SelectOption[] {
	return Object.entries(obj).map(([key, value]) => ({ value, label: key }));
}

/**
 * Convert an object into an array of select groups based on its keys and entries.
 * @param obj - the object to convert to select groups.
 * @returns array of objects containing options and label entries.
 */
export function toSelectGroups(obj: Record<string, ObjectLike>): SelectGroup[] {
	return Object.entries(obj).map(([key, value]) => ({
		options: toSelectOptions(value),
		label: key
	}));
}

/**
 * Convert a selected option into a value to display, falling back if nothing is selected.
 * @param options - the available select options.
 * @param selected - the currently selected option.
 * @returns string representing what to display as selected.
 */
export function toSelectedTextFromOptions(options: SelectOption[], selected?: unknown): string {
	return options.find((o) => o?.value === selected)?.label || 'Select a value';
}

/**
 * Convert a selected option into a value to display, falling back if nothing is selected.
 * @param groups - the available select groups.
 * @param selected - the currently selected option.
 * @returns string representing what to display as selected.
 */
export function toSelectedTextFromGroup(groups: SelectGroup[], selected?: unknown): string {
	const group = groups.find((g) => g.options.find((o) => o.value === selected));
	const options = group?.options ?? [];
	return toSelectedTextFromOptions(options, selected);
}
