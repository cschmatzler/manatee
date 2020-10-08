<script context="module" lang="ts">
    import { API_ENDPOINT } from "../../../util/api";

    export async function preload(page, session) {
        const { number } = page.params;
        const offset = (number - 1) * 20;
        const limit = 20;

        const countRes = await this.fetch(`${API_ENDPOINT}/products/count`);
        const count = (await countRes.json()).count;

        const productsRes = await this.fetch(
            `${API_ENDPOINT}/products?offset=${offset}&limit=20`
        );
        const products = (await productsRes.json()).products;

        return { number, offset, limit, count, products };
    }
</script>

<script lang="ts">
    import type { Product } from "../../../types/product";

    import { goto } from "@sapper/app";

    import Wrapper from "../../../components/Wrapper.svelte";
    import Header from "../../../components/Header.svelte";
    import TableRow from "./_TableRow.svelte";

    export let number: number;
    export let offset: number;
    export let limit: number;
    export let count: number;
    export let products: Product[];

    function paginationUpper(): number {
        if (offset + limit > count) {
            return count;
        }
        return offset + limit;
    }

    function paginationShowPrevious(): boolean {
        return number > 1;
    }
    function paginationShowNext(): boolean {
        return count > offset + limit;
    }

    function previousPage() {
        goto(`/products/page/${number - 1}`);
    }
    function nextPage() {
        goto(`/products/page/${number + 1}`);
    }
</script>

<svelte:head>
    <title>Produkte</title>
</svelte:head>

<Header>
    <span slot="title">Produkte</span>
    <div slot="actions">
        <span class="order-0 sm:order-1 sm:ml-3 shadow-sm rounded-md">
            <button
                type="button"
                class="inline-flex items-center px-4 py-2 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:shadow-outline-indigo focus:border-indigo-700 active:bg-purple-700 transition duration-150 ease-in-out">
                Neues Produkt
            </button>
        </span>
    </div>
</Header>
<Wrapper>
    <div class="bg-white px-6 py-6">
        <h3 class="text-lg leading-6 font-medium text-gray-900">Produkte</h3>
    </div>
    <table class="min-w-full divide-y divide-cool-gray-200">
        <thead>
            <tr>
                <th
                    class="px-6 py-3 bg-cool-gray-50 text-left text-xs leading-4 font-medium text-cool-gray-500 uppercase tracking-wider">
                    Seriennummer
                </th>
                <th
                    class="px-6 py-3 bg-cool-gray-50 text-left text-xs leading-4 font-medium text-cool-gray-500 uppercase tracking-wider">
                    Kunde
                </th>
                <th
                    class="hidden px-6 py-3 bg-cool-gray-50 text-left text-xs leading-4 font-medium text-cool-gray-500 uppercase tracking-wider md:block">
                    Status
                </th>
                <th
                    class="px-6 py-3 bg-cool-gray-50 text-right text-xs leading-4 font-medium text-cool-gray-500 uppercase tracking-wider">
                    Datum
                </th>
            </tr>
        </thead>
        <tbody class="bg-white divide-y divide-cool-gray-200">
            {#each products as product}
                <TableRow {product} />
            {/each}
        </tbody>
    </table>
    <nav
        class="bg-white px-4 py-3 flex items-center justify-between border-t border-cool-gray-200 sm:px-6">
        <div class="hidden sm:block">
            <p class="text-sm leading-5 text-cool-gray-700">
                Zeige
                <span class="font-medium">{offset + 1}</span>
                bis
                <span class="font-medium">{paginationUpper()}</span>
                von
                <span class="font-medium">{count}</span>
                Produkten
            </p>
        </div>
        <div class="flex-1 flex justify-between sm:justify-end">
            <button
                on:click={previousPage}
                class:hidden={!paginationShowPrevious()}
                class="relative inline-flex items-center px-4 py-2 border border-cool-gray-300 text-sm leading-5 font-medium rounded-md text-cool-gray-700 bg-white hover:text-cool-gray-500 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 active:bg-cool-gray-100 active:text-cool-gray-700 transition ease-in-out duration-150">
                Vorherige
            </button>
            <button
                on:click={nextPage}
                class:hidden={!paginationShowNext()}
                class=" ml-3 relative inline-flex items-center px-4 py-2 border border-cool-gray-300 text-sm leading-5 font-medium rounded-md text-cool-gray-700 bg-white hover:text-cool-gray-500 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 active:bg-cool-gray-100 active:text-cool-gray-700 transition ease-in-out duration-150">
                Nächste
            </button>
        </div>
    </nav>
</Wrapper>
