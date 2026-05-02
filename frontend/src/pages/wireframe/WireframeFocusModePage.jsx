import AppShell from "../../components/shell/AppShell";

const WireframeFocusModePage = () => {
  return (
    <AppShell title="Focus Mode">
      <section className="mx-auto max-w-2xl rounded-2xl border border-slate-200 bg-white p-8 text-center shadow-sm">
        <div className="flex items-center justify-between text-xs text-slate-500">
          <button className="rounded-lg border border-slate-200 px-2.5 py-1">Exit Focus</button>
          <button className="rounded-lg border border-slate-200 px-2.5 py-1">Music</button>
        </div>
        <h2 className="mt-7 text-3xl font-semibold text-slate-800">Study Algorithms</h2>
        <p className="mt-2 text-sm text-slate-600">Stay focused. You can do this.</p>
        <div className="mx-auto mt-8 flex h-56 w-56 items-center justify-center rounded-full border-[6px] border-slate-300 text-5xl font-medium text-slate-800">24:59</div>
        <button className="mt-4 text-sm font-medium text-slate-600">Pause</button>
        <div className="mx-auto mt-8 max-w-sm text-left text-sm text-slate-600">
          <div className="mb-2 flex justify-between"><span>Focus Progress</span><span>60%</span></div>
          <div className="h-2.5 rounded-full bg-slate-200"><div className="h-2.5 w-[60%] rounded-full bg-gradient-to-r from-blue-500 to-cyan-500" /></div>
        </div>
        <button className="mt-8 w-full rounded-xl bg-blue-600 py-2.5 font-semibold text-white transition hover:bg-blue-700">COMPLETE TASK</button>
      </section>
    </AppShell>
  );
};

export default WireframeFocusModePage;
