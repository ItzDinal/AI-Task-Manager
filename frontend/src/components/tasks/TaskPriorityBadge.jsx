// Priority badge with subtle semantic tones.
function TaskPriorityBadge({ priority }) {
  const styles = {
    High: "border-red-200 bg-red-50 text-red-700",
    Medium: "border-amber-200 bg-amber-50 text-amber-700",
    Low: "border-emerald-200 bg-emerald-50 text-emerald-700",
  };

  return (
    <span className={`inline-flex rounded-full border px-2.5 py-1 text-xs font-medium ${styles[priority] || "border-gray-200 bg-gray-50 text-gray-700"}`}>
      {priority}
    </span>
  );
}

export default TaskPriorityBadge;
