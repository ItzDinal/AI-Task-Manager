import AppShell from "../../components/shell/AppShell";

const fieldClass = "mt-1 w-full rounded-xl border border-slate-300 bg-slate-50 px-3 py-2 text-sm outline-none transition focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-500/30";

const WireframeAddTaskPage = () => {
  return (
    <AppShell title="Add / Edit Task">
      <div className="flex min-h-[70vh] items-center justify-center">
        <section className="w-full max-w-xl rounded-2xl border border-slate-200 bg-white p-6 shadow-lg shadow-slate-300/40">
          <div className="mb-5 flex items-center justify-between">
            <h2 className="text-lg font-semibold text-slate-800">Add New Task</h2>
            <button className="rounded-lg px-2 py-1 text-slate-400 hover:bg-slate-100">X</button>
          </div>
          <form className="space-y-4">
            <div>
              <label className="text-sm font-medium text-slate-600">Task Title</label>
              <input className={fieldClass} placeholder="e.g. Learn React" />
            </div>
            <div>
              <label className="text-sm font-medium text-slate-600">Description (Optional)</label>
              <textarea className={`${fieldClass} h-24`} placeholder="Add details..." />
            </div>
            <div className="grid gap-3 sm:grid-cols-2">
              <div>
                <label className="text-sm font-medium text-slate-600">Time Needed</label>
                <select className={fieldClass}><option>45 min</option></select>
              </div>
              <div>
                <label className="text-sm font-medium text-slate-600">Priority</label>
                <select className={fieldClass}><option>High</option></select>
              </div>
            </div>
            <div className="grid gap-3 sm:grid-cols-2">
              <div>
                <label className="text-sm font-medium text-slate-600">Category</label>
                <select className={fieldClass}><option>Study</option></select>
              </div>
              <label className="mt-8 flex items-center gap-2 text-sm text-slate-600">
                <input type="checkbox" className="h-4 w-4 rounded border-slate-300 text-blue-600" /> Add to today
              </label>
            </div>
            <button type="button" className="w-full rounded-xl bg-blue-600 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-700">ADD TASK</button>
          </form>
        </section>
      </div>
    </AppShell>
  );
};

export default WireframeAddTaskPage;
