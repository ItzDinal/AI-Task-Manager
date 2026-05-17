import TaskSearch from "./TaskSearch.jsx";

// Filter and sort controls for the task table (UI-only).
function TaskFilters() {
  return (
    <div className="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
      <TaskSearch />

      <div className="grid grid-cols-1 gap-3 sm:grid-cols-3 lg:w-auto">
        <select className="h-10 rounded-xl border border-gray-200 bg-white px-3 text-sm text-gray-600 outline-none transition-all duration-200 focus:ring-2 focus:ring-gray-300">
          <option>Status: All</option>
          <option>Pending</option>
          <option>In Progress</option>
          <option>Completed</option>
        </select>

        <select className="h-10 rounded-xl border border-gray-200 bg-white px-3 text-sm text-gray-600 outline-none transition-all duration-200 focus:ring-2 focus:ring-gray-300">
          <option>Priority: All</option>
          <option>High</option>
          <option>Medium</option>
          <option>Low</option>
        </select>

        <select className="h-10 rounded-xl border border-gray-200 bg-white px-3 text-sm text-gray-600 outline-none transition-all duration-200 focus:ring-2 focus:ring-gray-300">
          <option>Sort: Latest</option>
          <option>Due Date</option>
          <option>Priority</option>
          <option>Status</option>
        </select>
      </div>
    </div>
  );
}

export default TaskFilters;
