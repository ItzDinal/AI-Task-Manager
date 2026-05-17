import UpcomingTaskItem from "./UpcomingTaskItem.jsx";
import WidgetHeader from "./WidgetHeader.jsx";

const upcomingTasks = [
  {
    id: 1,
    title: "UI Dashboard Review",
    dueDate: "May 18",
    priority: "High",
    status: "In Progress",
    category: "Design",
  },
  {
    id: 2,
    title: "Backend API Integration",
    dueDate: "May 20",
    priority: "Medium",
    status: "Pending",
    category: "Backend",
  },
  {
    id: 3,
    title: "Mobile Responsiveness Fix",
    dueDate: "May 22",
    priority: "Low",
    status: "Completed",
    category: "Frontend",
  },
];

// Upcoming tasks side widget for quick task prioritization.
function UpcomingTasks() {
  return (
    <section className="flex flex-col gap-4 rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
      <WidgetHeader title="Upcoming Tasks" />
      <div className="flex flex-col gap-2">
        {upcomingTasks.map((task) => (
          <UpcomingTaskItem key={task.id} task={task} />
        ))}
      </div>
    </section>
  );
}

export default UpcomingTasks;
