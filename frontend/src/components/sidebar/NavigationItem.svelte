<script lang="ts">
    import { isPageActive } from "../../util/navigation";

    export let segment: string;
    export let href: string;
</script>

<a
    {href}
    class:bg-gray-100={isPageActive(segment, href)}
    class="group w-full flex items-center pl-7 pr-2 py-2 text-md leading-5 font-medium text-gray-900 rounded-md hover:text-gray-900 hover:bg-gray-100 focus:outline-none focus:bg-gray-200 transition ease-in-out duration-150">
    <slot />
</a>
