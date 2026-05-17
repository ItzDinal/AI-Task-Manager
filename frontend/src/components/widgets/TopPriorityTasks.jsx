import FocusModeButton from "./FocusModeButton.jsx";
import PriorityTaskItem from "./PriorityTaskItem.jsx";
import WidgetHeader from "./WidgetHeader.jsx";

const topPriorityTasks = [
  {
    id: 1,
    title: "Complete AI Dashboard Design",
    priority: "Critical",
    dueDate: "Today",
    status: "In Progress",
    category: "Design",
  },
  {
    id: 2,
    title: "Submit Project Proposal",
    priority: "High",
    dueDate: "Tomorrow",
    status: "Pending",
    category: "Planning",
  },
  {
    id: 3,
    title: "Fix Authentication Bug",
    priority: "High",
    dueDate: "May 20",
    status: "Review",
    category: "Backend",
  },
];

// Priority-focused widget highlighting urgent tasks.
function TopPriorityTasks() {
  return (
    <section className="flex flex-col gap-4 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm transition-all duration-200 ease-in-out hover:shadow-md">
      <WidgetHeader title="Top Priority" actionLabel="View All" />
      <div className="flex flex-col gap-3">
        {topPriorityTasks.map((task) => (
          <PriorityTaskItem key={task.id} task={task} />
        ))}
      </div>
      <FocusModeButton />
    </section>
  );
}

export default TopPriorityTasks;
