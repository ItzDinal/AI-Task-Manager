// Section title block for task management table.
function TaskTableHeader() {
  return (
    <div className="flex items-start justify-between gap-4">
      <div>
        <h2 className="text-lg font-semibold text-gray-900">Task Management</h2>
        <p className="mt-1 text-sm text-gray-500">Track priorities, deadlines, and execution status at a glance.</p>
      </div>
    </div>
  );
}

export default TaskTableHeader;
