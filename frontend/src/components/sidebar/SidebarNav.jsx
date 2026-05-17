import {
  Bot,
  Calendar,
  ChartColumn,
  LayoutDashboard,
  ListTodo,
  Settings,
} from "lucide-react";
import SidebarNavItem from "./SidebarNavItem.jsx";

const navItems = [
  { label: "Dashboard", to: "/dashboard", icon: LayoutDashboard },
  { label: "Tasks", to: "/tasks", icon: ListTodo },
  { label: "Calendar", to: "/daily-plan", icon: Calendar },
  { label: "Analytics", to: "/analytics", icon: ChartColumn },
  { label: "AI Assistant", to: "/focus", icon: Bot },
  { label: "Settings", to: "/dashboard", icon: Settings },
];

// Primary app navigation links.
function SidebarNav() {
  return (
    <section className="space-y-2">
      <p className="px-2 text-xs uppercase tracking-wide text-gray-400">Navigation</p>
      <div className="space-y-2">
        {navItems.map((item) => (
          <SidebarNavItem key={`${item.label}-${item.to}`} to={item.to} icon={item.icon} label={item.label} />
        ))}
      </div>
    </section>
  );
}

export default SidebarNav;
