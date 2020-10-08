<script lang="ts">
    import type { Category } from "../../types/category";

    import { goto } from "@sapper/app";

    export let category: Category;

    function viewCategory(id: number) {
        goto(`/categories/${id}`);
    }
</script>

<tr class="bg-white">
    <td
        class="max-w-xs px-6 py-4 whitespace-no-wrap text-sm leading-5 text-cool-gray-900">
        <div class="flex">
            <span
                class="group inline-flex space-x-2 truncate text-sm leading-5">
                <p
                    class="text-cool-gray-500 truncate group-hover:text-cool-gray-900 transition ease-in-out duration-150">
                    {category.name}
                </p>
            </span>
        </div>
    </td>
    <td
        class="px-6 py-4 whitespace-no-wrap text-sm leading-5 text-cool-gray-500">
        {category.material_count}
        Materialien
    </td>

    <td
        class="px-6 py-4 text-right whitespace-no-wrap text-sm leading-5 text-cool-gray-500">
        <span class="order-0 sm:order-1 sm:ml-3 shadow-sm rounded-md">
            <button
                type="button"
                on:click={() => viewCategory(category.id)}
                class="inline-flex items-center px-4 py-2 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:shadow-outline-indigo focus:border-indigo-700 active:bg-purple-700 transition duration-150 ease-in-out">
                Ansehen
            </button>
        </span>
    </td>
</tr>
