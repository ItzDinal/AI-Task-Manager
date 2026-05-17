import WelcomeHeader from "./WelcomeHeader.jsx";
import StatsGrid from "../stats/StatsGrid.jsx";
import TaskTable from "../tasks/TaskTable.jsx";

// Main dashboard content region placeholder.
function MainContent() {
  return (
    <section className="min-w-0 space-y-4 sm:space-y-6">
      <WelcomeHeader />
      <StatsGrid />
      <TaskTable />
    </section>
  );
}

export default MainContent;
