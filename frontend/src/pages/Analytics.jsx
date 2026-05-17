const Analytics = () => {
  return (
    <div className="space-y-4">
      <div className="grid gap-4 md:grid-cols-3">
        <div className="rounded-xl border border-slate-200 bg-white p-5"><p className="text-sm text-slate-500">Tasks Completed</p><p className="mt-2 text-3xl font-bold">28</p></div>
        <div className="rounded-xl border border-slate-200 bg-white p-5"><p className="text-sm text-slate-500">Focus Time</p><p className="mt-2 text-3xl font-bold">12h 45m</p></div>
        <div className="rounded-xl border border-slate-200 bg-white p-5"><p className="text-sm text-slate-500">Current Streak</p><p className="mt-2 text-3xl font-bold">5 days</p></div>
      </div>
    </div>
  );
};

export default Analytics;
