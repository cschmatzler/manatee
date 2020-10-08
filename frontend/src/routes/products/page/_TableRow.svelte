<script lang="ts">
    import { Product } from "../../../types/product";

    import { formatDate } from "../../../util/date";

    export let product: Product;
</script>

<tr class="bg-white">
    <td
        class="max-w-xs px-6 py-4 whitespace-no-wrap text-sm leading-5 text-cool-gray-900">
        <div class="flex">
            <a
                href="/products/{product.id}"
                class="group inline-flex space-x-2 truncate text-sm leading-5">
                <p
                    class="text-cool-gray-500 truncate group-hover:text-cool-gray-900 transition ease-in-out duration-150">
                    {product.serial}
                </p>
            </a>
        </div>
    </td>
    <td
        class="px-6 py-4 whitespace-no-wrap text-sm leading-5 text-cool-gray-500" />
    <td
        class="hidden px-6 py-4 whitespace-no-wrap text-sm leading-5 text-cool-gray-500 md:block">
        <!--
        <span
            class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium leading-4 bg-green-100 text-green-800 capitalize" />-->
    </td>
    <td
        class="px-6 py-4 text-right whitespace-no-wrap text-sm leading-5 text-cool-gray-500">
        {formatDate(product.created)}
    </td>
</tr>
