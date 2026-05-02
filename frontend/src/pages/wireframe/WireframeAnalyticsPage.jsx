import AppShell from "../../components/shell/AppShell";

const WireframeAnalyticsPage = () => {
  return (
    <AppShell title="Analytics">
      <div className="space-y-5">
        <div className="grid gap-4 md:grid-cols-3">
          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm"><p className="text-sm text-slate-500">Tasks Completed</p><p className="mt-2 text-3xl font-bold text-slate-800">28</p></div>
          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm"><p className="text-sm text-slate-500">Focus Time</p><p className="mt-2 text-3xl font-bold text-slate-800">12h 45m</p></div>
          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm"><p className="text-sm text-slate-500">Current Streak</p><p className="mt-2 text-3xl font-bold text-slate-800">5 days</p></div>
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
            <h3 className="text-sm font-semibold text-slate-700">Tasks Completed</h3>
            <div className="mt-4 grid h-56 grid-cols-7 items-end gap-2">
              {[3,5,6,6,8,10,12].map((v,i) => <div key={i} className="rounded-t bg-gradient-to-t from-blue-500 to-cyan-400" style={{ height: `${v * 10}px` }} />)}
            </div>
          </div>
          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
            <h3 className="text-sm font-semibold text-slate-700">Focus Time (hrs)</h3>
            <div className="mt-4 h-56 rounded-xl bg-gradient-to-b from-slate-50 via-blue-50 to-slate-100" />
          </div>
        </div>
      </div>
    </AppShell>
  );
};

export default WireframeAnalyticsPage;
