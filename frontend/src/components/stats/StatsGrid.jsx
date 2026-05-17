import { AlertTriangle, CheckCircle2, Clock3, LayoutList } from "lucide-react";
import StatCard from "./StatCard.jsx";

const statsData = [
  {
    title: "Total Tasks",
    value: "24",
    subtitle: "All active and planned tasks",
    trend: "positive",
    trendText: "+12% from last week",
    icon: LayoutList,
    tone: "neutral",
  },
  {
    title: "Completed Tasks",
    value: "18",
    subtitle: "Tasks finished this week",
    trend: "positive",
    trendText: "+8% from last week",
    icon: CheckCircle2,
    tone: "positive",
  },
  {
    title: "In Progress Tasks",
    value: "4",
    subtitle: "Currently in focus cycles",
    trend: "neutral",
    trendText: "Steady this week",
    icon: Clock3,
    tone: "neutral",
  },
  {
    title: "Overdue Tasks",
    value: "2",
    subtitle: "Needs attention today",
    trend: "warning",
    trendText: "-1 from yesterday",
    icon: AlertTriangle,
    tone: "warning",
  },
];

// Responsive stat summary grid for top-level dashboard insights.
function StatsGrid() {
  return (
    <section className="grid grid-cols-1 gap-6 sm:grid-cols-2 xl:grid-cols-4">
      {statsData.map((stat) => (
        <StatCard
          key={stat.title}
          icon={stat.icon}
          tone={stat.tone}
          title={stat.title}
          value={stat.value}
          trend={stat.trend}
          trendText={stat.trendText}
          subtitle={stat.subtitle}
        />
      ))}
    </section>
  );
}

export default StatsGrid;
