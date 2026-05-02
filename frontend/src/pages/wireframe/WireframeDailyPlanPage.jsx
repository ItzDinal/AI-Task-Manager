import AppShell from "../../components/shell/AppShell";

const rows = [
  ["09:00 AM", "Study Algorithms", "45 min", "High priority and due soon"],
  ["10:00 AM", "Build Project UI", "60 min", "Deep work time"],
  ["11:30 AM", "Break", "15 min", "Recharge your energy"],
  ["11:45 AM", "Exercise", "30 min", "Good for health and focus"],
  ["12:30 PM", "Lunch Break", "60 min", "Take a proper rest"],
  ["01:30 PM", "Read Book", "30 min", "Improve knowledge"],
  ["02:15 PM", "Meditation", "10 min", "Clear your mind"],
];

const WireframeDailyPlanPage = () => {
  return (
    <AppShell title="Daily Plan (AI Powered)">
      <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="mb-4 flex flex-wrap items-center justify-between gap-3">
          <div>
            <h2 className="text-lg font-semibold text-slate-800">Your AI Daily Plan</h2>
            <p className="text-sm text-slate-600">Based on your goals and available time.</p>
          </div>
          <button className="rounded-xl border border-slate-300 px-3 py-2 text-sm font-medium hover:bg-slate-50">Regenerate Plan</button>
        </div>
        <div className="overflow-x-auto rounded-xl border border-slate-200">
          <table className="w-full min-w-[760px] text-left text-sm">
            <thead className="bg-slate-50 text-slate-500">
              <tr><th className="px-4 py-3">Time</th><th className="px-4 py-3">Task</th><th className="px-4 py-3">Duration</th><th className="px-4 py-3">Reason</th></tr>
            </thead>
            <tbody>
              {rows.map((row) => (
                <tr key={row[0] + row[1]} className="border-t border-slate-100">
                  <td className="px-4 py-3">{row[0]}</td><td className="px-4 py-3">{row[1]}</td><td className="px-4 py-3">{row[2]}</td><td className="px-4 py-3">{row[3]}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <button className="mt-5 w-full rounded-xl bg-blue-600 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-700">FOLLOW THIS PLAN</button>
      </section>
    </AppShell>
  );
};

export default WireframeDailyPlanPage;
