<script lang="ts">
	import type { ButtonSize, ButtonVariant } from '$uilib/components/ui/button/index.js';
	import { buttonVariants } from '$uilib/components/ui/button/index.js';
	import { cn } from '$uilib/utils.js';
	import { AlertDialog as AlertDialogPrimitive } from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		variant = 'outline',
		size = 'default',
		...restProps
	}: AlertDialogPrimitive.CancelProps & {
		variant?: ButtonVariant;
		size?: ButtonSize;
	} = $props();
</script>

<AlertDialogPrimitive.Cancel
	bind:ref
	data-slot="alert-dialog-cancel"
	class={cn(buttonVariants({ variant, size }), 'cn-alert-dialog-cancel', className)}
	{...restProps}
/>
