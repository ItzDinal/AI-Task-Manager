import AppShell from "../../components/shell/AppShell";

const tasks = [
  ["Study Algorithms", "45 min", "High", "Start with problem 1", "Pending"],
  ["Build Project UI", "60 min", "Medium", "Break into 3 subtasks", "Pending"],
  ["Exercise", "30 min", "Low", "Best for energy", "Pending"],
  ["Read Book", "20 min", "Low", "Read 10 pages", "Pending"],
  ["Meditation", "10 min", "Low", "Good for focus", "Pending"],
];

const WireframeTaskManagementPage = () => {
  return (
    <AppShell title="Task Management">
      <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="mb-5 flex flex-wrap items-center justify-between gap-3">
          <div className="flex gap-2 text-sm">
            <button className="rounded-xl bg-slate-900 px-3 py-1.5 text-white">All</button>
            <button className="rounded-xl px-3 py-1.5 text-slate-500 hover:bg-slate-100">Today</button>
            <button className="rounded-xl px-3 py-1.5 text-slate-500 hover:bg-slate-100">Upcoming</button>
            <button className="rounded-xl px-3 py-1.5 text-slate-500 hover:bg-slate-100">Completed</button>
          </div>
          <button className="rounded-xl border border-slate-300 px-3 py-1.5 text-sm font-medium hover:bg-slate-50">+ Add Task</button>
        </div>
        <div className="overflow-x-auto rounded-xl border border-slate-200">
          <table className="w-full min-w-[860px] text-left text-sm">
            <thead className="bg-slate-50 text-slate-500">
              <tr>
                <th className="px-4 py-3">Task</th><th className="px-4 py-3">Time</th><th className="px-4 py-3">Priority</th><th className="px-4 py-3">AI Suggestion</th><th className="px-4 py-3">Status</th>
              </tr>
            </thead>
            <tbody>
              {tasks.map((task) => (
                <tr key={task[0]} className="border-t border-slate-100">
                  <td className="px-4 py-3">{task[0]}</td><td className="px-4 py-3">{task[1]}</td><td className="px-4 py-3">{task[2]}</td><td className="px-4 py-3">{task[3]}</td><td className="px-4 py-3">{task[4]}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </AppShell>
  );
};

export default WireframeTaskManagementPage;
