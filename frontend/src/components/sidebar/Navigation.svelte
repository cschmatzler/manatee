<script lang="ts">
    import type { Category } from "../../types/category";

    import NavigationItem from "./NavigationItem.svelte";
    import NavigationGroup from "./NavigationGroup.svelte";

    export let segment: string;

    export let categories: Category[];
</script>

<style>
</style>

<nav>
    <div class="mt-5 overflow-y-auto">
        <nav class="px-2 space-y-1">
            <!--<NavigationItem href="/" {segment}>Start</NavigationItem>-->

            <NavigationGroup title="Produkte">
                <!--<NavigationItem href="/products" {segment}>
                    Übersicht
                </NavigationItem>-->
                <NavigationItem href="/products/page/1" {segment}>
                    Liste
                </NavigationItem>
                <NavigationItem href="/products/new" {segment}>
                    Neues Produkt
                </NavigationItem>
            </NavigationGroup>
            <NavigationGroup title="Materialien">
                <NavigationItem href="/categories" {segment}>
                    Gruppen
                </NavigationItem>
                {#each categories as category}
                    <NavigationItem href="/categories/{category.id}" {segment}>
                        {category.name}
                    </NavigationItem>
                {/each}
            </NavigationGroup>
        </nav>
    </div>
</nav>
