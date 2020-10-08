<script context="module" lang="ts">
    import { API_ENDPOINT } from "../../util/api";

    export async function preload(page, session) {
        const categoriesRes = await this.fetch(`${API_ENDPOINT}/categories`);
        const categories = (await categoriesRes.json()).categories;

        return { categories };
    }
</script>

<script lang="ts">
    import type { Category } from "../../types/category";

    import Header from "../../components/Header.svelte";
    import Wrapper from "../../components/Wrapper.svelte";
    import TableRow from "./_CategoryTableRow.svelte";
    import TwoColumnForm from "../../components/form/TwoColumnForm.svelte";

    export let categories: Category[];
    export let category_name: string;

    async function addCategory() {
        fetch(`${API_ENDPOINT}/categories`, {
            method: "POST",
            body: JSON.stringify({
                name: category_name,
            }),
            headers: {
                "Content-Type": "application/json",
            },
        }).then((response) => {
            if (response.status === 201) {
                reloadCategories();
                category_name = "";
            }
        });
    }

    async function reloadCategories() {
        const categoriesRes = await fetch(`${API_ENDPOINT}/categories`);

        categories = (await categoriesRes.json()).categories;
    }
</script>

<Header>
    <span slot="title">Gruppen</span>
    <div slot="actions">
        <span class="order-0 sm:order-1 sm:ml-3 shadow-sm rounded-md">
            <button
                type="button"
                class="inline-flex items-center px-4 py-2 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:shadow-outline-indigo focus:border-indigo-700 active:bg-purple-700 transition duration-150 ease-in-out">
                Neue Gruppe
            </button>
        </span>
    </div>
</Header>
<Wrapper>
    <TwoColumnForm title="Neue Gruppe" description="">
        <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
            <div class="sm:col-span-4">
                <label
                    for="category_name"
                    class="block text-sm font-medium leading-5 text-gray-700">
                    Name
                </label>
                <div class="mt-1 flex rounded-md shadow-sm">
                    <input
                        bind:value={category_name}
                        id="category_name"
                        class="flex-1 form-input block w-full min-w-0 rounded-none rounded-r-md transition duration-150 ease-in-out sm:text-sm sm:leading-5" />
                </div>
            </div>
        </div>

        <div class="mt-8 border-t border-gray-200 pt-5">
            <div class="flex justify-end">
                <span class="ml-3 inline-flex rounded-md shadow-sm">
                    <button
                        on:click|preventDefault={addCategory}
                        type="submit"
                        class="inline-flex justify-center py-2 px-4 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700 transition duration-150 ease-in-out">
                        Hinzufuegen
                    </button>
                </span>
            </div>
        </div>
    </TwoColumnForm>
</Wrapper>

<Wrapper>
    <div class="bg-white px-6 py-6">
        <h3 class="text-lg leading-6 font-medium text-gray-900">Gruppen</h3>
    </div>
    <table
        class="min-w-full divide-y divide-cool-gray-200 sm:border-t sm:border-gray-200">
        <thead>
            <tr>
                <th
                    class="px-6 py-3 bg-cool-gray-50 text-left text-xs leading-4 font-medium text-cool-gray-500 uppercase tracking-wider">
                    Name
                </th>
                <th
                    class="px-6 py-3 bg-cool-gray-50 text-left text-xs leading-4 font-medium text-cool-gray-500 uppercase tracking-wider">
                    Materialien
                </th>
                <th
                    class="px-6 py-3 bg-cool-gray-50 text-right text-xs leading-4 font-medium text-cool-gray-500 uppercase tracking-wider" />
            </tr>
        </thead>
        <tbody class="bg-white divide-y divide-cool-gray-200">
            {#each categories as category}
                <TableRow {category} />
            {/each}
        </tbody>
    </table>
</Wrapper>
