import { ClipboardList } from "lucide-react";

// Empty state placeholder for no-task scenarios.
function EmptyTasksState() {
  return (
    <div className="rounded-2xl border border-dashed border-gray-300 bg-gray-50 p-8 text-center">
      <div className="mx-auto inline-flex rounded-xl bg-white p-3 text-gray-500 shadow-sm">
        <ClipboardList size={18} />
      </div>
      <p className="mt-3 text-sm font-medium text-gray-700">No tasks found</p>
      <p className="mt-1 text-xs text-gray-500">Try adjusting filters or add a new task to get started.</p>
      <button type="button" className="mt-4 rounded-xl bg-black px-4 py-2 text-sm font-medium text-white transition-all duration-200 hover:bg-gray-800">
        + Create Task
      </button>
    </div>
  );
}

export default EmptyTasksState;
