const Tasks = () => {
  return (
    <section className="rounded-xl border border-slate-200 bg-white p-5">
      <div className="mb-4 flex items-center justify-between">
        <h2 className="text-lg font-semibold text-slate-800">Task Management</h2>
        <button className="rounded-lg bg-blue-600 px-3 py-2 text-sm font-semibold text-white hover:bg-blue-700">Add Task</button>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full min-w-[680px] text-left text-sm">
          <thead className="text-slate-500">
            <tr className="border-b border-slate-200">
              <th className="py-2">Task</th><th>Time</th><th>Priority</th><th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-slate-100"><td className="py-3">Study Algorithms</td><td>45 min</td><td>High</td><td>Pending</td></tr>
            <tr className="border-b border-slate-100"><td className="py-3">Build Project UI</td><td>60 min</td><td>Medium</td><td>Pending</td></tr>
          </tbody>
        </table>
      </div>
    </section>
  );
};

export default Tasks;
