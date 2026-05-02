import AppShell from "../../components/shell/AppShell";

const WireframeDashboardPage = () => {
  return (
    <AppShell title="Dashboard (Today)">
      <div className="grid gap-5 lg:grid-cols-3">
        <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm lg:col-span-2">
          <h2 className="text-xl font-semibold text-slate-800">Good morning, Dinal</h2>
          <p className="mt-1 text-sm text-slate-600">Let&apos;s make today productive.</p>
        </section>
        <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
          <h3 className="text-sm font-semibold text-slate-700">Today&apos;s Progress</h3>
          <div className="mt-4 h-2.5 w-full rounded-full bg-slate-200">
            <div className="h-2.5 w-[70%] rounded-full bg-gradient-to-r from-blue-500 to-cyan-500" />
          </div>
          <p className="mt-3 text-right text-sm font-semibold text-slate-700">70%</p>
        </section>

        <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm lg:col-span-2">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-semibold text-slate-700">Today&apos;s Top 3 Tasks</h3>
            <span className="text-xs text-slate-500">3 tasks remaining</span>
          </div>
          <ul className="mt-4 space-y-2 text-sm text-slate-700">
            <li className="flex justify-between rounded-xl bg-slate-50 px-3 py-2.5"><span>Study Algorithms</span><span>45 min</span></li>
            <li className="flex justify-between rounded-xl bg-slate-50 px-3 py-2.5"><span>Build Project UI</span><span>60 min</span></li>
            <li className="flex justify-between rounded-xl bg-slate-50 px-3 py-2.5"><span>Exercise</span><span>30 min</span></li>
          </ul>
        </section>

        <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
          <h3 className="text-sm font-semibold text-slate-700">AI Suggestion</h3>
          <p className="mt-3 text-sm leading-6 text-slate-600">Best next task for you: Study Algorithms (45 min)</p>
          <button className="mt-5 w-full rounded-xl bg-blue-600 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-700">START FOCUS</button>
        </section>

        <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm lg:col-span-3">
          <h3 className="text-sm font-semibold text-slate-700">Daily Streak</h3>
          <div className="mt-4 grid grid-cols-7 gap-2 text-center text-xs text-slate-600">
            {['M','T','W','T','F','S','S'].map((d) => <div key={d} className="rounded-lg bg-slate-50 p-2.5">{d}</div>)}
          </div>
        </section>
      </div>
    </AppShell>
  );
};

export default WireframeDashboardPage;
