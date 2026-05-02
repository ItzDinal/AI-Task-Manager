import AppShell from "../../components/shell/AppShell";

const WireframeSummaryPage = () => {
  return (
    <AppShell title="End of Day Summary">
      <section className="mx-auto max-w-3xl rounded-2xl border border-slate-200 bg-white p-8 text-center shadow-sm">
        <h2 className="text-3xl font-semibold text-slate-800">Great work today!</h2>
        <p className="mt-2 text-slate-600">You completed 80% of your tasks.</p>
        <div className="mx-auto mt-8 flex h-40 w-40 items-center justify-center rounded-full border-[6px] border-blue-200 bg-blue-50 text-4xl font-bold text-blue-700">80%</div>
        <p className="mt-3 text-sm text-slate-600">Day Completed</p>
        <div className="mt-7 grid gap-3 sm:grid-cols-3">
          <div className="rounded-xl border border-slate-200 bg-slate-50 p-4"><p className="text-xs text-slate-500">Tasks Done</p><p className="mt-1 text-xl font-bold text-slate-800">4/5</p></div>
          <div className="rounded-xl border border-slate-200 bg-slate-50 p-4"><p className="text-xs text-slate-500">Focus Time</p><p className="mt-1 text-xl font-bold text-slate-800">3h 20m</p></div>
          <div className="rounded-xl border border-slate-200 bg-slate-50 p-4"><p className="text-xs text-slate-500">Streak</p><p className="mt-1 text-xl font-bold text-slate-800">5 days</p></div>
        </div>
        <p className="mt-8 text-slate-600">Small progress is still progress. See you tomorrow.</p>
      </section>
    </AppShell>
  );
};

export default WireframeSummaryPage;
