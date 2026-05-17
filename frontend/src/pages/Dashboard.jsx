const Dashboard = () => {
  return (
    <div className="grid gap-4 lg:grid-cols-3">
      <section className="rounded-xl border border-slate-200 bg-white p-5 lg:col-span-2">
        <h2 className="text-xl font-semibold text-slate-800">Good morning</h2>
        <p className="mt-1 text-sm text-slate-600">Let&apos;s make today productive.</p>
      </section>
      <section className="rounded-xl border border-slate-200 bg-white p-5">
        <h3 className="text-sm font-semibold text-slate-700">Today&apos;s Progress</h3>
        <div className="mt-3 h-2 rounded-full bg-slate-200">
          <div className="h-2 w-[70%] rounded-full bg-blue-500" />
        </div>
      </section>
    </div>
  );
};

export default Dashboard;
