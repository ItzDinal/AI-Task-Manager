// Compact priority indicator for task urgency.
function TaskPriorityIndicator({ priority }) {
  const tone = {
    High: "bg-red-400",
    Medium: "bg-amber-400",
    Low: "bg-emerald-400",
  }[priority] || "bg-gray-400";

  return <span className={`inline-block h-2.5 w-2.5 rounded-full ${tone}`} />;
}

export default TaskPriorityIndicator;
