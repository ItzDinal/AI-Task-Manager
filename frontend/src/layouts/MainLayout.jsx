import { NavLink, Outlet } from "react-router-dom";

const navItems = [
  { label: "Dashboard", to: "/dashboard" },
  { label: "Tasks", to: "/tasks" },
  { label: "Focus", to: "/focus" },
  { label: "Analytics", to: "/analytics" },
  { label: "Daily Plan", to: "/daily-plan" },
];

const MainLayout = () => {
  return (
    <div className="min-h-screen bg-slate-100">
      <div className="mx-auto flex min-h-screen max-w-[1400px] border-x border-slate-200 bg-white">
        <aside className="w-64 border-r border-slate-200 bg-white p-4">
          <h1 className="mb-6 text-lg font-bold text-slate-900">AI Task Manager</h1>
          <nav className="space-y-1">
            {navItems.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive }) =>
                  `block rounded-lg px-3 py-2 text-sm transition ${
                    isActive ? "bg-blue-50 font-semibold text-blue-700" : "text-slate-600 hover:bg-slate-100"
                  }`
                }
              >
                {item.label}
              </NavLink>
            ))}
          </nav>
        </aside>

        <div className="flex min-h-screen flex-1 flex-col">
          <header className="flex h-16 items-center justify-between border-b border-slate-200 px-5">
            <p className="text-sm font-semibold text-slate-800">Productivity Workspace</p>
            <input
              type="text"
              placeholder="Search tasks..."
              className="h-10 w-72 rounded-lg border border-slate-300 px-3 text-sm outline-none focus:border-blue-500"
            />
          </header>
          <main className="flex-1 bg-slate-50 p-5">
            <Outlet />
          </main>
        </div>
      </div>
    </div>
  );
};

export default MainLayout;
