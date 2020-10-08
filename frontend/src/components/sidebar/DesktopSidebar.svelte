<script lang="ts">
    import type { Category } from "../../types/category";

    import Logo from "./Logo.svelte";
    import Navigation from "./Navigation.svelte";

    export let segment: string;

    export let categories: Category[];
</script>

<div class="hidden lg:flex lg:flex-shrink-0">
    <div class="flex flex-col w-64">
        <div class="flex flex-col flex-grow bg-white pt-5 pb-4 overflow-y-auto">
            <Logo />
            <Navigation {segment} {categories} />
        </div>
    </div>
</div>
