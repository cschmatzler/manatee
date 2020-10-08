<script context="module" lang="ts">
    import { API_ENDPOINT } from "../../util/api";

    export async function preload(page, session) {
        const { id } = page.params;

        const categoryRes = await this.fetch(`${API_ENDPOINT}/category/${id}`);
        const category = (await categoryRes.json()).category;

        const materialsRes = await this.fetch(
            `${API_ENDPOINT}/category/${id}/materials`
        );
        const materials = (await materialsRes.json()).materials;

        return { category, materials };
    }
</script>

<script lang="ts">
    import type { Category } from "../../types/category";

    import Header from "../../components/Header.svelte";
    import Wrapper from "../../components/Wrapper.svelte";
    import TableRow from "./_CategoryTableRow.svelte";
    import MaterialTableRow from "./_MaterialTableRow.svelte";
    import TwoColumnForm from "../../components/form/TwoColumnForm.svelte";

    export let category: Category;
    export let materials;

    export let material_name: string;

    async function addMaterial() {
        fetch(`${API_ENDPOINT}/category/${category.id}/materials`, {
            method: "POST",
            body: JSON.stringify({
                name: material_name,
            }),
            headers: {
                "Content-Type": "application/json",
            },
        }).then((response) => {
            if (response.status === 201) {
                reloadMaterials();
                material_name = "";
            }
        });
    }

    function deleteMaterial(event) {
        const id = event.detail.id;

        fetch(`${API_ENDPOINT}/category/${category.id}/material/${id}`, {
            method: "DELETE",
        }).then((response) => {
            if (response.status === 204) {
                materials = materials.filter((material) => material.id !== id);
            }
        });
    }

    async function reloadMaterials() {
        const materialsRes = await fetch(
            `${API_ENDPOINT}/category/${category.id}/materials`
        );

        materials = (await materialsRes.json()).materials;
    }
</script>

<Header><span slot="title">{category.name}</span></Header>
<Wrapper>
    <TwoColumnForm title="Neues Material" description="">
        <div class="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
            <div class="sm:col-span-4">
                <label
                    for="material_name"
                    class="block text-sm font-medium leading-5 text-gray-700">
                    Name
                </label>
                <div class="mt-1 flex rounded-md shadow-sm">
                    <input
                        bind:value={material_name}
                        id="material_name"
                        class="flex-1 form-input block w-full min-w-0 rounded-none rounded-r-md transition duration-150 ease-in-out sm:text-sm sm:leading-5" />
                </div>
            </div>
        </div>
        <div class="mt-8 border-t border-gray-200 pt-5">
            <div class="flex justify-end">
                <span class="ml-3 inline-flex rounded-md shadow-sm">
                    <button
                        on:click|preventDefault={addMaterial}
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
        <h3 class="text-lg leading-6 font-medium text-gray-900">
            {category.name}
        </h3>
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
                    class="px-6 py-3 bg-cool-gray-50 text-right text-xs leading-4 font-medium text-cool-gray-500 uppercase tracking-wider" />
            </tr>
        </thead>
        <tbody class="bg-white divide-y divide-cool-gray-200">
            {#each materials as material}
                <MaterialTableRow {material} on:message={deleteMaterial} />
            {/each}
        </tbody>
    </table>
</Wrapper>
