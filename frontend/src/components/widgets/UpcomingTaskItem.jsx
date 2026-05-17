import TaskDateLabel from "./TaskDateLabel.jsx";
import TaskPriorityIndicator from "./TaskPriorityIndicator.jsx";

// Single upcoming task row in compact widget format.
function UpcomingTaskItem({ task }) {
  const statusTone = {
    "In Progress": "bg-blue-50 text-blue-700",
    Pending: "bg-slate-100 text-slate-700",
    Completed: "bg-emerald-50 text-emerald-700",
  }[task.status] || "bg-slate-100 text-slate-700";

  return (
    <div className="flex items-start justify-between gap-3 rounded-xl p-3 transition-all duration-200 hover:bg-gray-50">
      <div className="min-w-0">
        <div className="flex items-center gap-2">
          <TaskPriorityIndicator priority={task.priority} />
          <p className="truncate font-medium text-gray-900">{task.title}</p>
        </div>
        <p className="mt-1 text-xs text-gray-500">{task.category}</p>
        <div className="mt-1">
          <TaskDateLabel dueDate={task.dueDate} />
        </div>
      </div>

      <span className={`shrink-0 rounded-full px-2 py-1 text-xs ${statusTone}`}>{task.status}</span>
    </div>
  );
}

export default UpcomingTaskItem;
