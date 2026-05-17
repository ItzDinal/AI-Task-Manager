import PriorityIndicator from "./PriorityIndicator.jsx";
import TaskProgressBadge from "./TaskProgressBadge.jsx";

// Single high-priority task row focused on urgency and clarity.
function PriorityTaskItem({ task }) {
  return (
    <div className="rounded-xl border border-gray-200 p-4 transition-all duration-200 hover:bg-gray-50">
      <div className="flex items-start justify-between gap-3">
        <div className="min-w-0">
          <p className="font-semibold text-gray-900">{task.title}</p>
          <p className="mt-1 text-xs text-gray-500">{task.category}</p>
        </div>
        <TaskProgressBadge status={task.status} />
      </div>

      <div className="mt-3 flex items-center justify-between gap-2">
        <PriorityIndicator priority={task.priority} />
        <p className="text-sm text-gray-400">Due {task.dueDate}</p>
      </div>
    </div>
  );
}

export default PriorityTaskItem;
