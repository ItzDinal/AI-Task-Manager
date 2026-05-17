import { ChevronDown } from "lucide-react";

// User account summary and dropdown trigger placeholder.
function UserMenu() {
  return (
    <button
      type="button"
      className="inline-flex h-10 items-center gap-2 rounded-xl px-2 text-gray-700 transition duration-200 hover:bg-gray-100"
    >
      <span className="flex h-8 w-8 items-center justify-center rounded-full bg-gray-200 text-xs font-semibold text-gray-700">AC</span>
      <span className="hidden text-sm font-medium md:inline">Alex</span>
      <ChevronDown size={16} className="text-gray-500" />
    </button>
  );
}

export default UserMenu;
