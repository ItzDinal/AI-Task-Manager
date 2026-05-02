const Topbar = ({ title }) => {
  return (
    <header className="flex h-16 items-center justify-between border-b border-slate-200 bg-white px-6">
      <div>
        <p className="text-xs font-medium uppercase tracking-[0.14em] text-slate-400">AI Task Manager</p>
        <h1 className="text-sm font-semibold text-slate-800">{title}</h1>
      </div>
      <div className="flex items-center gap-3">
        <input
          type="text"
          placeholder="Search tasks..."
          className="h-10 w-72 rounded-xl border border-slate-300 bg-slate-50 px-3 text-sm outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-500/30"
        />
        <button className="rounded-xl border border-slate-200 bg-white px-3 py-2 text-xs font-medium text-slate-600 hover:bg-slate-50">Bell</button>
        <button className="rounded-xl border border-slate-200 bg-white px-3 py-2 text-xs font-medium text-slate-600 hover:bg-slate-50">User</button>
      </div>
    </header>
  );
};

export default Topbar;
