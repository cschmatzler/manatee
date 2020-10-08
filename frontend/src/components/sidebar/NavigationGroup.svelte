<script lang="ts">
    export let title: string;

    let expanded: boolean = false;
    function toggleExpanded() {
        expanded = !expanded;
    }
</script>

<div>
    <button
        on:click={toggleExpanded}
        class="mt-1 group w-full flex items-center pr-2 py-2 text-md leading-5 font-medium rounded-md bg-white text-gray-600 hover:bg-gray-50 hover:text-gray-900 focus:outline-none focus:text-gray-900 focus:bg-gray-50 transition ease-in-out duration-150">
        <svg
            class:text-gray-300={!expanded}
            class:text-gray-400={expanded}
            class:rotate-90={expanded}
            class="mr-2 h-5 w-5 transform group-hover:text-gray-400 group-focus:text-gray-400 transition-colors ease-in-out duration-150"
            viewBox="0 0 20 20">
            <path d="M6 6L14 10L6 14V6Z" fill="currentColor" />
        </svg>
        {title}
    </button>
    {#if expanded}
        <slot />
    {/if}
</div>
