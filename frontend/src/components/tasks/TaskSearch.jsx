import { Search } from "lucide-react";

// Search input UI for task discovery.
function TaskSearch() {
  return (
    <div className="relative w-full md:max-w-xs">
      <Search size={16} className="pointer-events-none absolute top-1/2 left-3 -translate-y-1/2 text-gray-400" />
      <input
        type="text"
        placeholder="Search tasks"
        className="h-10 w-full rounded-xl border border-gray-200 bg-white py-2 pr-3 pl-9 text-sm text-gray-700 outline-none transition-all duration-200 focus:ring-2 focus:ring-gray-300"
      />
    </div>
  );
}

export default TaskSearch;
