/** @type {import('tailwindcss').Config} */

module.exports = {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
        "*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: "#1e40af", // blue-900
                    foreground: "#ffffff",
                },
                secondary: {
                    DEFAULT: "#64748b", // slate-500
                    foreground: "#ffffff",
                },
                destructive: {
                    DEFAULT: "#dc2626", // red-600
                    foreground: "#ffffff",
                },
                muted: {
                    DEFAULT: "#f3f4f6", // gray-100
                    foreground: "#1f2937", // gray-800
                },
                accent: {
                    DEFAULT: "#10b981", // emerald-500
                    foreground: "#ffffff",
                },
                border: "#e5e7eb", // gray-200
                input: "#f9fafb", // gray-50
                ring: "#3b82f6", // blue-500
                background: "#ffffff",
                foreground: "#000000",
                popover: {
                    DEFAULT: "#f9fafb",
                    foreground: "#111827",
                },
                card: {
                    DEFAULT: "#ffffff",
                    foreground: "#1f2937",
                },
            },
            borderRadius: {
                lg: "0.5rem",
                md: "0.375rem",
                sm: "0.25rem",
            },
        },
    },
    plugins: [],
};
