import EmptyTasksState from "./EmptyTasksState.jsx";
import TaskFilters from "./TaskFilters.jsx";
import TaskRow from "./TaskRow.jsx";
import TaskTableHeader from "./TaskTableHeader.jsx";

const tasks = [
  {
    id: 1,
    title: "Design Dashboard UI",
    category: "Design",
    dueDate: "May 18",
    priority: "High",
    status: "In Progress",
    assignee: "Dinal",
  },
  {
    id: 2,
    title: "Connect Authentication API",
    category: "Backend",
    dueDate: "May 20",
    priority: "Medium",
    status: "Pending",
    assignee: "Alex",
  },
  {
    id: 3,
    title: "Fix Mobile Responsiveness",
    category: "Frontend",
    dueDate: "May 22",
    priority: "Low",
    status: "Completed",
    assignee: "Sam",
  },
];

// Core task table section with filters, rows, and empty state fallback.
function TaskTable() {
  const hasTasks = tasks.length > 0;

  return (
    <section className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
      <div className="space-y-4">
        <TaskTableHeader />
        <TaskFilters />

        {hasTasks ? (
          <>
            <div className="hidden overflow-x-auto md:block">
              <table className="w-full border-separate border-spacing-y-3">
                <thead>
                  <tr>
                    <th className="px-4 text-left text-sm uppercase tracking-wide text-gray-400">Task</th>
                    <th className="px-4 text-left text-sm uppercase tracking-wide text-gray-400">Due Date</th>
                    <th className="px-4 text-left text-sm uppercase tracking-wide text-gray-400">Priority</th>
                    <th className="px-4 text-left text-sm uppercase tracking-wide text-gray-400">Status</th>
                    <th className="px-4 text-left text-sm uppercase tracking-wide text-gray-400">Assigned</th>
                    <th className="px-4 text-right text-sm uppercase tracking-wide text-gray-400">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {tasks.map((task) => (
                    <TaskRow key={task.id} task={task} />
                  ))}
                </tbody>
              </table>
            </div>

            <div className="space-y-3 md:hidden">
              {tasks.map((task) => (
                <TaskRow key={`mobile-${task.id}`} task={task} variant="card" />
              ))}
            </div>
          </>
        ) : (
          <EmptyTasksState />
        )}
      </div>
    </section>
  );
}

export default TaskTable;
