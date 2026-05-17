// Compact status/progress badge for priority tasks.
function TaskProgressBadge({ status }) {
  const styles = {
    "In Progress": "bg-blue-50 text-blue-700",
    Pending: "bg-slate-100 text-slate-700",
    Review: "bg-violet-50 text-violet-700",
  };

  return (
    <span className={`rounded-full px-2 py-1 text-xs font-medium ${styles[status] || "bg-slate-100 text-slate-700"}`}>
      {status}
    </span>
  );
}

export default TaskProgressBadge;
