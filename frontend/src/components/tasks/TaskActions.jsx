import { MoreHorizontal, Pencil, Trash2 } from "lucide-react";

// Row-level action buttons placeholder.
function TaskActions() {
  return (
    <div className="flex items-center justify-end gap-1">
      <button type="button" aria-label="Edit task" className="inline-flex h-8 w-8 items-center justify-center rounded-lg text-gray-500 transition-all duration-200 hover:bg-gray-200 hover:text-gray-700">
        <Pencil size={14} />
      </button>
      <button type="button" aria-label="Delete task" className="inline-flex h-8 w-8 items-center justify-center rounded-lg text-gray-500 transition-all duration-200 hover:bg-gray-200 hover:text-gray-700">
        <Trash2 size={14} />
      </button>
      <button type="button" aria-label="More options" className="inline-flex h-8 w-8 items-center justify-center rounded-lg text-gray-500 transition-all duration-200 hover:bg-gray-200 hover:text-gray-700">
        <MoreHorizontal size={14} />
      </button>
    </div>
  );
}

export default TaskActions;
