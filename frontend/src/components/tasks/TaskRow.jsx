import TaskActions from "./TaskActions.jsx";
import TaskPriorityBadge from "./TaskPriorityBadge.jsx";
import TaskStatusBadge from "./TaskStatusBadge.jsx";

// Single task row rendered in table or mobile-card mode.
function TaskRow({ task, variant = "table" }) {
  if (variant === "card") {
    return (
      <div className="rounded-xl border border-gray-200 bg-gray-50 p-4 transition-all duration-200 hover:bg-gray-100">
        <div className="flex items-start justify-between gap-3">
          <div className="flex items-start gap-3">
            <input type="checkbox" className="mt-1 h-4 w-4 rounded border-gray-300 text-black" />
            <div>
              <p className="font-semibold text-gray-900">{task.title}</p>
              <p className="text-xs text-gray-400">{task.category}</p>
            </div>
          </div>
          <TaskActions />
        </div>

        <div className="mt-3 grid grid-cols-2 gap-3 text-xs text-gray-500">
          <div>
            <p className="uppercase tracking-wide text-gray-400">Due</p>
            <p className="mt-1 text-sm text-gray-700">{task.dueDate}</p>
          </div>
          <div>
            <p className="uppercase tracking-wide text-gray-400">Assignee</p>
            <p className="mt-1 text-sm text-gray-700">{task.assignee}</p>
          </div>
          <div>
            <p className="uppercase tracking-wide text-gray-400">Priority</p>
            <div className="mt-1">
              <TaskPriorityBadge priority={task.priority} />
            </div>
          </div>
          <div>
            <p className="uppercase tracking-wide text-gray-400">Status</p>
            <div className="mt-1">
              <TaskStatusBadge status={task.status} />
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <tr>
      <td className="rounded-l-xl bg-gray-50 px-4 py-4 align-middle transition-all duration-200 hover:bg-gray-100">
        <div className="flex items-start gap-3">
          <input type="checkbox" className="mt-1 h-4 w-4 rounded border-gray-300 text-black" />
          <div>
            <p className="font-semibold text-gray-900">{task.title}</p>
            <p className="text-xs text-gray-400">{task.category}</p>
          </div>
        </div>
      </td>
      <td className="bg-gray-50 px-4 py-4 align-middle text-sm text-gray-600 transition-all duration-200 hover:bg-gray-100">{task.dueDate}</td>
      <td className="bg-gray-50 px-4 py-4 align-middle transition-all duration-200 hover:bg-gray-100">
        <TaskPriorityBadge priority={task.priority} />
      </td>
      <td className="bg-gray-50 px-4 py-4 align-middle transition-all duration-200 hover:bg-gray-100">
        <TaskStatusBadge status={task.status} />
      </td>
      <td className="bg-gray-50 px-4 py-4 align-middle text-sm text-gray-600 transition-all duration-200 hover:bg-gray-100">{task.assignee}</td>
      <td className="rounded-r-xl bg-gray-50 px-4 py-4 align-middle transition-all duration-200 hover:bg-gray-100">
        <TaskActions />
      </td>
    </tr>
  );
}

export default TaskRow;
