<script lang="ts">
	import type { ButtonSize, ButtonVariant } from '$uilib/components/ui/button/index.js';
	import { buttonVariants } from '$uilib/components/ui/button/index.js';
	import { cn } from '$uilib/utils.js';
	import { AlertDialog as AlertDialogPrimitive } from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		variant = 'default',
		size = 'default',
		...restProps
	}: AlertDialogPrimitive.ActionProps & {
		variant?: ButtonVariant;
		size?: ButtonSize;
	} = $props();
</script>

<AlertDialogPrimitive.Action
	bind:ref
	data-slot="alert-dialog-action"
	class={cn(buttonVariants({ variant, size }), 'cn-alert-dialog-action', className)}
	{...restProps}
/>
