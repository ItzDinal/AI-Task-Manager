import { Search } from "lucide-react";

// Global search input UI placeholder for tasks, projects, and AI insights.
function NavbarSearch() {
  return (
    <div className="relative w-full max-w-xl">
      <Search size={16} className="pointer-events-none absolute top-1/2 left-3 -translate-y-1/2 text-gray-400" />
      <input
        type="text"
        placeholder="Search tasks, projects, AI insights..."
        className="h-10 w-full rounded-xl border border-transparent bg-gray-100 pr-14 pl-9 text-sm text-gray-700 outline-none transition-all focus:ring-2 focus:ring-gray-300"
      />
      <span className="pointer-events-none absolute top-1/2 right-3 -translate-y-1/2 rounded-md border border-gray-200 bg-white px-2 py-0.5 text-[10px] text-gray-500">
        ⌘K
      </span>
    </div>
  );
}

export default NavbarSearch;
