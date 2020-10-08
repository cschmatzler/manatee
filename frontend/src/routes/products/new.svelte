<script context="module" lang="ts">
    import { API_ENDPOINT } from "../../util/api";

    export async function preload(page, session) {
        const categoriesRes = await this.fetch(`${API_ENDPOINT}/categories`);
        const categories = (await categoriesRes.json()).categories;

        let materials = [];

        for (const category in categories) {
            if (Object.prototype.hasOwnProperty.call(categories, category)) {
                const element = categories[category];

                const materialsRes = await this.fetch(
                    `${API_ENDPOINT}/category/${element.id}/materials`
                );

                element.materials = (await materialsRes.json()).materials;
            }
        }

        return { categories, materials };
    }
</script>

<script lang="ts">
    import type { Category } from "../../types/category";

    import Header from "../../components/Header.svelte";
    import Wrapper from "../../components/Wrapper.svelte";
    import TwoColumnForm from "../../components/form/TwoColumnForm.svelte";

    let promise;

    export let categories: Category[];

    let expanded: number;
    let lots = [];

    let product_serial: number;
    let lot_number: string;

    let selected = [];

    function toggleMaterial(id: number) {
        expanded = id;
        promise = loadLots(id);
    }

    function toggleLot(id: number, number: string, material: string) {
        if (selected.some((el) => el.id === id)) {
            selected = selected.filter((el) => el !== id);
        } else {
            selected = [...selected, { id, number, material }];
        }
    }

    async function addProduct() {
        const response = await fetch(`${API_ENDPOINT}/products`, {
            method: "POST",
            body: JSON.stringify({
                serial: parseInt(product_serial),
                lots: selected,
            }),
            headers: {
                "Content-Type": "application/json",
            },
        });

        if (response.status === 201) {
            product_serial = null;
            selected = [];
        }
    }

    async function addLot(material: number) {
        const response = await fetch(
            `${API_ENDPOINT}/material/${material}/lots`,
            {
                method: "POST",
                body: JSON.stringify({
                    number: lot_number,
                }),
                headers: {
                    "Content-Type": "application/json",
                },
            }
        );

        if (response.status === 201) {
            promise = loadLots(material);
            lot_number = "";
        }
    }

    async function loadLots(material: number) {
        let object = {
            material,
        };

        const lotsRes = await fetch(
            `${API_ENDPOINT}/material/${material}/lots`
        );

        return (await lotsRes.json()).lots;
    }
</script>

<Header><span slot="title">Neues Produkt</span></Header>
<Wrapper>
    <TwoColumnForm title="Allgemein" description="">
        <div class="grid grid-cols-6 gap-6">
            <div class="col-span-3 sm:col-span-2">
                <label
                    for="product_serial"
                    class="block text-sm font-medium leading-5 text-gray-700">
                    Seriennummer
                </label>
                <div class="mt-1 flex rounded-md shadow-sm">
                    <input
                        bind:value={product_serial}
                        id="product_serial"
                        class="form-input flex-1 block w-full rounded-md transition duration-150 ease-in-out sm:text-sm sm:leading-5"
                        placeholder="1"
                        pattern="[0-9]" />
                </div>
            </div>
        </div>
    </TwoColumnForm>
</Wrapper>
{#each categories as category}
    <Wrapper>
        <TwoColumnForm title={category.name} description="">
            <div class="group space-y-3">
                {#each category.materials as material (material.id)}
                    <div class="grid grid-cols-1 gap-6">
                        <div class="col-span-3 sm:col-span-2">
                            <span class="w-full rounded-md shadow-sm">
                                <button
                                    on:click={() => toggleMaterial(material.id)}
                                    type="button"
                                    class:bg-gray-300={expanded === material.id}
                                    class="w-full inline-flex items-center px-4 py-2 border border-gray-300 text-sm leading-5 font-medium rounded-md text-gray-700 bg-white hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:text-gray-800 active:bg-gray-50 transition ease-in-out duration-150">
                                    {material.name}
                                </button>
                            </span>
                        </div>
                    </div>
                    {#if expanded === material.id}
                        {#await promise then lots}
                            {#each lots as lot (lot.id)}
                                {#if !lot.exhausted}
                                    <div class="grid grid-cols-4 gap-6">
                                        <div class="col-span-3 sm:col-span-2">
                                            <span
                                                class="w-full rounded-md shadow-sm">
                                                <button
                                                    on:click={() => toggleLot(lot.id, lot.number, material.name)}
                                                    type="button"
                                                    class:bg-gray-100={selected.includes(lot.id)}
                                                    class="w-full inline-flex items-center px-4 py-2 border border-gray-300 text-sm leading-5 font-medium rounded-md text-gray-700 bg-white hover:text-gray-500 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:text-gray-800 active:bg-gray-50 transition ease-in-out duration-150">
                                                    {lot.number}
                                                </button>
                                            </span>
                                        </div>
                                    </div>
                                {/if}
                            {/each}
                        {/await}
                        <form>
                            <div class="grid grid-cols-3 gap-6">
                                <div class="col-span-2">
                                    <label
                                        for="lot_number"
                                        class="block text-sm font-medium leading-5 text-gray-700">
                                        Neue Charge
                                    </label>
                                    <div class="mt-1 flex rounded-md shadow-sm">
                                        <input
                                            bind:value={lot_number}
                                            id="lot_number"
                                            class="form-input flex-1 block w-full rounded-md transition duration-150 ease-in-out sm:text-sm sm:leading-5"
                                            placeholder="Chargennummer" />
                                    </div>
                                </div>
                                <div class="col-span-1">
                                    <span
                                        class="w-full inline-flex rounded-md shadow-sm mt-6">
                                        <button
                                            on:click|preventDefault={addLot(material.id)}
                                            type="button"
                                            class="w-full inline-flex items-center px-4 py-2 border border-gray-300 text-sm leading-5 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700 transition duration-150 ease-in-out">
                                            Speichern
                                        </button>
                                    </span>
                                </div>
                            </div>
                        </form>
                    {/if}
                {/each}
            </div>
        </TwoColumnForm>
    </Wrapper>
{/each}

{selected}

<Wrapper>
    <TwoColumnForm title="Zusammenfassung" description="">
        {#each selected as lot}{lot.id} - {lot.number} - {lot.material}{/each}
        <div class="mt-8 border-t border-gray-200 pt-5">
            <div class="flex justify-end">
                <span class="ml-3 inline-flex rounded-md shadow-sm">
                    <button
                        on:click|preventDefault={addProduct}
                        type="submit"
                        class="inline-flex justify-center py-2 px-4 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700 transition duration-150 ease-in-out">
                        Speichern
                    </button>
                </span>
            </div>
        </div>
    </TwoColumnForm>
</Wrapper>
