import { NavLink } from "react-router-dom";

const navItems = [
  { label: "Dashboard", to: "/dashboard" },
  { label: "Tasks", to: "/tasks" },
  { label: "Focus Mode", to: "/focus" },
  { label: "Daily Plan", to: "/daily-plan" },
  { label: "Analytics", to: "/analytics" },
  { label: "Calendar", to: "/calendar" },
  { label: "Settings", to: "/settings" },
];

const Sidebar = () => {
  return (
    <aside className="flex w-64 flex-col border-r border-slate-200 bg-white/95 backdrop-blur">
      <div className="border-b border-slate-200 px-5 py-4">
        <p className="text-xs font-medium uppercase tracking-[0.16em] text-slate-400">Workspace</p>
        <p className="mt-1 text-base font-bold text-slate-800">AI Task Manager</p>
      </div>
      <nav className="flex-1 space-y-1 px-3 py-3">
        {navItems.map((item) => (
          <NavLink
            key={item.label}
            to={item.to}
            className={({ isActive }) =>
              `block rounded-xl px-3 py-2.5 text-sm transition ${
                isActive
                  ? "bg-blue-50 font-semibold text-blue-700 ring-1 ring-blue-100"
                  : "text-slate-600 hover:bg-slate-100"
              }`
            }
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
      <button className="m-3 rounded-xl border border-slate-200 bg-slate-50 px-3 py-2 text-left text-xs font-medium text-slate-500 hover:bg-slate-100">
        Collapse
      </button>
    </aside>
  );
};

export default Sidebar;
