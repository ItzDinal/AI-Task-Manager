import AIAssistantWidget from "../ai/AIAssistantWidget.jsx";
import MiniCalendar from "../calendar/MiniCalendar.jsx";
import TopPriorityTasks from "../widgets/TopPriorityTasks.jsx";
import UpcomingTasks from "../widgets/UpcomingTasks.jsx";

// Right-side dashboard widget panel.
function RightPanel() {
  return (
    <aside className="min-w-0 space-y-4">
      <MiniCalendar />
      <UpcomingTasks />
      <TopPriorityTasks />
      <AIAssistantWidget />
    </aside>
  );
}

export default RightPanel;
