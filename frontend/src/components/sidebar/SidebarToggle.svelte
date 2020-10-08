<script lang="ts">
    import { createEventDispatcher } from "svelte";

    import Menu from "../icons/Menu.svelte";

    const dispatch = createEventDispatcher();

    function toggleSidebar() {
        dispatch("message", {});
    }
</script>

<div
    class="relative z-10 flex-shrink-0 flex h-16 bg-white border-b border-gray-200 lg:border-none lg:hidden">
    <!-- Sidebar toggle -->
    <button
    on:click={toggleSidebar}
    class="px-4 border-r border-cool-gray-200 text-cool-gray-400 focus:outline-none focus:bg-cool-gray-100 focus:text-cool-gray-600"
    aria-label="Open sidebar">
    <Menu />
</button>
</div>
