import { Moon } from "lucide-react";

// Theme mode toggle placeholder for future dark/light preference.
function ThemeToggle() {
  return (
    <button
      type="button"
      aria-label="Toggle theme"
      className="inline-flex h-10 w-10 items-center justify-center rounded-xl text-gray-600 transition duration-200 hover:bg-gray-100"
    >
      <Moon size={18} />
    </button>
  );
}

export default ThemeToggle;
