// Priority level badge with urgency-aware muted styling.
function PriorityIndicator({ priority }) {
  const styles = {
    Critical: "bg-red-100 text-red-600",
    High: "bg-orange-100 text-orange-600",
  };

  return (
    <span className={`rounded-full px-2 py-1 text-xs font-medium ${styles[priority] || "bg-gray-100 text-gray-600"}`}>
      {priority}
    </span>
  );
}

export default PriorityIndicator;
