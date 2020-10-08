export function isPageActive(segment: string, href: string): boolean {
    switch (segment) {
        case undefined:
            return href === "/";
        case "products":
            return href === "/products";
    }

    return false;
}
