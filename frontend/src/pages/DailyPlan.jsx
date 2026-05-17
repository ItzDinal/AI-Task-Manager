const DailyPlan = () => {
  return (
    <section className="rounded-xl border border-slate-200 bg-white p-5">
      <div className="mb-4 flex items-center justify-between">
        <div>
          <h2 className="text-lg font-semibold text-slate-800">Your AI Daily Plan</h2>
          <p className="text-sm text-slate-600">Based on your goals and availability.</p>
        </div>
        <button className="rounded-lg border border-slate-300 px-3 py-2 text-sm">Regenerate Plan</button>
      </div>
      <ul className="space-y-2 text-sm text-slate-700">
        <li className="rounded-lg bg-slate-50 px-3 py-2">09:00 AM - Study Algorithms (45 min)</li>
        <li className="rounded-lg bg-slate-50 px-3 py-2">10:00 AM - Build Project UI (60 min)</li>
        <li className="rounded-lg bg-slate-50 px-3 py-2">11:30 AM - Break (15 min)</li>
      </ul>
    </section>
  );
};

export default DailyPlan;
