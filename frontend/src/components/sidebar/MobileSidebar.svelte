<script lang="ts">
    import type { Category } from "../../types/category";

    import { createEventDispatcher } from "svelte";

    import Close from "../icons/Close.svelte";
    import Logo from "./Logo.svelte";
    import Navigation from "./Navigation.svelte";

    export let segment: string;

    export let categories: Category[];

    const dispatch = createEventDispatcher();

    function toggleSidebar() {
        dispatch("message", {});
    }
</script>

<div class="lg:hidden">
    <div class="fixed inset-0 flex z-40">
        <div class="fixed inset-0">
            <div class="absolute inset-0 bg-cool-gray-600 opacity-75" />
        </div>

        <div
            class="relative flex-1 flex flex-col max-w-xs w-full pt-5 pb-4 bg-white">
            <div class="absolute top-0 right-0 -mr-14 p-1">
                <button
                    on:click={toggleSidebar}
                    class="flex items-center justify-center h-12 w-12 rounded-full focus:outline-none focus:bg-cool-gray-600"
                    aria-label="Close sidebar">
                    <Close />
                </button>
            </div>
            <Logo />
            <Navigation {segment} {categories} />
        </div>
    </div>
</div>
