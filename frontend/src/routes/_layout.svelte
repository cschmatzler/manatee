<script context="module" lang="ts">
    import { API_ENDPOINT } from "../util/api";

    export async function preload(page, session) {
        const categoriesRes = await this.fetch(`${API_ENDPOINT}/categories`);
        const categories = (await categoriesRes.json()).categories;

        return { categories };
    }
</script>

<script lang="ts">
    import type { Category } from "../types/category";

    import DesktopSidebar from "../components/sidebar/DesktopSidebar.svelte";
    import MobileSidebar from "../components/sidebar/MobileSidebar.svelte";
    import SidebarToggle from "../components/sidebar/SidebarToggle.svelte";

    export let segment: string;

    export let categories: Category[];

    let showSidebar = false;
    function toggleSidebar(): void {
        showSidebar = !showSidebar;
    }
</script>

<style>
</style>

<template>
    <div class="h-screen flex overflow-hidden bg-cool-gray-100">
        {#if showSidebar}
            <MobileSidebar {segment} {categories} on:message={toggleSidebar} />
        {/if}
        <DesktopSidebar {segment} {categories} />

        <div class="flex-1 overflow-auto focus:outline-none" tabindex="0">
            <SidebarToggle on:message={toggleSidebar} />

            <main class="flex-1 relative pb-8 z-0 overflow-y-auto">
                <slot />
            </main>
        </div>
    </div>
</template>
