import { Plus } from "lucide-react";

// Primary quick action button for task creation.
function QuickActionButton() {
  return (
    <button
      type="button"
      className="inline-flex h-10 w-10 items-center justify-center rounded-xl bg-black text-white transition-all duration-200 ease-in-out motion-safe:transform-gpu motion-safe:hover:scale-[1.02] hover:bg-gray-800 hover:shadow-sm sm:w-auto sm:gap-2 sm:px-4"
      aria-label="Create new task"
    >
      <Plus size={16} />
      <span className="hidden sm:inline">New Task</span>
    </button>
  );
}

export default QuickActionButton;
