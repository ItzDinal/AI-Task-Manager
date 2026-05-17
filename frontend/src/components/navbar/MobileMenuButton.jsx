import { Menu } from "lucide-react";

// Mobile-only trigger placeholder for future sidebar drawer integration.
function MobileMenuButton() {
  return (
    <button
      type="button"
      aria-label="Open sidebar menu"
      className="inline-flex h-10 w-10 items-center justify-center rounded-xl border border-gray-200 text-gray-600 transition duration-200 hover:bg-gray-100 lg:hidden"
    >
      <Menu size={18} />
    </button>
  );
}

export default MobileMenuButton;
