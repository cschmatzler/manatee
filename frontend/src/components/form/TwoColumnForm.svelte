<script lang="ts">
    export let title: string;
    export let description: string;
</script>

<div class="bg-white shadow px-4 py-5 sm:rounded-lg sm:p-6">
    <div class="md:grid md:grid-cols-3 md:gap-6">
        <div class="md:col-span-1">
            <h3 class="text-lg font-medium leading-6 text-gray-900">{title}</h3>
            <p class="mt-1 text-sm leading-5 text-gray-500">{description}</p>
        </div>
        <div class="mt-5 md:mt-0 md:col-span-2">
            <form>
                <slot />
            </form>
        </div>
    </div>
</div>
